/*
 Minimal MCP server: pinecone-kb
Tools:
   - search_kb { query, topk=5, filterJson? }
   - get_doc { path_md }
   - synthesize_answer { query, topk=6, filterJson?, maxTokens=700, temperature=0.2 }
*/

import { Server } from "@modelcontextprotocol/sdk";
import { Pinecone } from "pinecone";
import { config } from "dotenv";
import OpenAI from "openai";
import natural from "natural";
import fs from "fs";
import path from "path";
config();

// Shared helpers
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const PINECONE_API_KEY = process.env.PINECONE_API_KEY;
const PINECONE_ENVIRONMENT = process.env.PINECONE_ENVIRONMENT || "us-east-1"; // <-- assuming the Python line listed here.
const INDEX_NAME = process.env.PINECONE_INDEX || "advantage-v2";
const EMBED_MODEL = process.env.EMBED_MODEL || "text-embedding-3-small";
const LLM_MODEL = process.env.LLM_MODEL || "gpt-4o-mini";

const openai = new OpenAI({ apiKey: OPENAI_API_KEY });
const pc = new Pinecone({ apiKey: PINECONE_API_KEY });
const index = typeof pc.Index === "function" ? pc.Index(INDEX_NAME) : pc.index(INDEX_NAME);

// Simple hashing TF-IDF for sparse (use same as in Python pipeline)
const stopwords = new Set(natural.stopwords);
function textToSparse(query) {
  // Simple bag-of-words indices, illustrative only (hybrid quality may differ from Python HashingVectorizer。
  // For production, consider a shared hashing scheme across ingest/search (e.g., precomputed mapping).
  const terms = query.toLowerCase().split(/\W+/).filter(t => t && !stopwords.has(t));
  const map = new Map();
  for (const t of terms) map.set(t, (map.get(t) || 0) + 1);
  // Pinecone sparse expects indices & values; treat hashed ind as t’s string hash (convert to int).
  const indices = [], values = [];
  for (const [k, v] of map.entries()) {
    const hash = Math.abs(natural.Metaphone.process(k).split("").reduce((a, c) => a + c.charCodeAt(0), 0));
    indices.push(hash % 262144); // 2^18 as in Python
    values.push(v);
  }
  return { indices, values };
}

async function embedOne(text) {
  const resp = await openai.embeddings.create({ model: EMBED_MODEL, input: [text] });
  return resp.data[0].embedding; 
}

function makeCitation(path_md, anchor) {
  if (!path_md) return "";
  return anchor ? `${path_md}#${anchor}` : path_md;
}

function makeIngestText(title, heading_path, content) {
  const hp = Array.isArray(heading_path) ? heading_path.filter(Boolean).join(" > ") : "";
  return [`Title: ${title || ""}`, hp ? `Section: ${hp}` : "", "", content || ""].join("\n");
}

const server = new Server({
  name: "pinecone-kb",
  version: "1.0.0",
  tools: {
    // search_kb tool
    search_kb: {
      description: "Hybrid search Advantage KB with optional JSON metadata filter",
      inputSchema:  {
        type: "object",
        properties: {
          query: { type: "string" },
          topk: { type: "number", default: 5 },
          filterJson: { type: "string" }
        },
        required: ["query"]
      },
      handler: async ({ query, topk = 5, filterJson }) => {
        const dense = await embedOne(query);
        let sparse = null;
        try {
          sparse = textToSparse(query);
        } catch (_) { /* fallback to dense-only */ }

        let filter = undefined;
        if (filterJson) {
          try { filter = JSON.parse(filterJson); } catch { /* ignore */ }
        }

        const result = await index.query({
          vector: dense,
          ...(sparse ? { sparseVector: sparse } : {}),
          topK: topk,
          includeMetadata: true,
          filter
        });

        const matches = (result.matches || []).map(m => {
          const md = m.metadata || {};
          return {
            score: m.score,
            title: md.title,
            citation: makeCitation(md.path_md, md.anchor),
            path_md: md.path_md,
            anchor: md.anchor,
            heading_path: md.heading_path,
            content: md.content
          };
        });
        return { results: matches };

      }
    },

    // get_doc tool
    get_doc: {
      description: "Fetch a cleaned MD doc by path_md from local filesystem",
      inputSchema:  {
        type: "object",
        properties: { path_md: { type: "string" } },
        required: ["path_md"]
      }, handler: async ({ path_md }) => {
        const p = path.join(process.cwd(), "knowledge-bases", "advantage_clean", path_md);
        if (!fs.existsSync(p)) return { error: `Not found: ${path_md}` };
        const text = fs.readFileSync(p, "utf-8");
        return { path_md, text };
      }
    },

    // synthesize_answer tool
    synthesize_answer: {
      description: "Answer a question using hybrid search and return text with inline citations",
      inputSchema:  {
        type: "object", properties: {
          query: { type: "string" },
          topk: { type: "number", default: 6 },
          filterJson: { type: "string" },
          maxTokens: { type: "number", default: 700 },
          temperature: { type: "number", default: 0.2 }
        }, required: ["query"]
      }, handler: async ({ query, topk = 6, filterJson, maxTokens = 700, temperature = 0.2 }) => {
        const dense = await embedOne(query);
        let sparse = null;
        try { sparse = textToSparse(query); } catch (_) { /* dense-only */ }

        let filter = undefined;
        if (filterJson) {
          try { filter = JSON.parse(filterJson); } catch { /* ignore */ }
        }

        const result = await index.query({
          vector: dense,
          ...(sparse ? { sparseVector: sparse } : {}),
          topK: topk,
          includeMetadata: true,
          filter
        });

        const passages = (result.matches || []).map((m, i) => {
          const md = m.metadata || {};
          return {
            n: i + 1,
            title: md.title || "",
            citation: makeCitation(md.path_md, md.anchor),
            content: (md.content || "").trim()
          };
        });

        const ctx = passages.map(p => `[${p.n}] ${p.title} — ${p.citation}\n${p.content}`).join("\n\n");
        const messages = [
          { role: "system", content:
            "Answer ONLY from the provided context. Use inline citations like [n]. End with a Sources list." },
          { role: "user", content:
            `Question:\n${query}\n\nContext:\n${ctx}\n\nInstructions:\n- Use inline citations like [1], [2].\n- If missing in context, say so.\n- End with a Sources list.\n` }
        ];

        try {
          const resp = await openai.chat.completions.create({ model: LLM_MODEL, messages, temperature, max_tokens: maxTokens });
          const answer = resp.choices?.[0]?.message?.content?.trim() || "";
          return { answer, passages };
        } catch (e) {
          // fallback: return top passages if LLM fails
          const fallback = [
            "No model-composed answer generated. Showing top passages:\n",
            ...passages.map(p => `[${p.n}] ${p.title} — ${p.citation}\n${p.content.slice(0, 800)}`),
            "",
            "Sources:",
            ...passages.map(p => `[${p.n}] ${p.citation}`)
          ].join("\n");
          return { answer: fallback, passages };
        }
      }
    }
  }
});

server.start().then(() => {
  console.log("pinecone-kb MCP server listening on stdio");
});