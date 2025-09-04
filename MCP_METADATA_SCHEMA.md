# MCP Server Metadata Schema for Intelligent Tool Selection

## Overview

This document defines the enhanced metadata schema for MCP servers that enables AI systems to intelligently select the most appropriate tool for user queries. The schema provides rich contextual information about each server's capabilities, specialties, and use cases.

## Schema Structure

### Required Fields
- `description`: Human-readable description of the server's purpose and capabilities
- `capabilities`: Object containing domains, specialties, query types, and output formats
- `use_cases`: Object with best_for and not_suitable_for arrays plus example_queries
- `tool_relationships`: Object defining how this tool relates to other tools

### Optional Fields
- `version`: Semantic version of the tool/knowledge base
- `lastUpdated`: Date when the knowledge base was last updated

## Complete Schema Definition

```json
{
  "server-name": {
    "type": "sse|stdio",
    "url": "endpoint-url",
    "description": "Brief description of server purpose and capabilities",
    "capabilities": {
      "domains": [
        "primary_domain",
        "secondary_domain",
        "related_domain"
      ],
      "specialties": [
        "specific_feature_1", 
        "specific_feature_2",
        "specific_operation_type"
      ],
      "query_types": [
        "how_to_guides",
        "reference_lookup", 
        "troubleshooting",
        "code_examples",
        "best_practices",
        "configuration_help",
        "performance_analysis"
      ],
      "output_formats": [
        "explanations",
        "code_examples", 
        "step_by_step",
        "citations"
      ]
    },
    "use_cases": {
      "best_for": [
        "Specific use case 1",
        "Specific use case 2",
        "Domain-specific operations"
      ],
      "not_suitable_for": [
        "Operations outside domain",
        "General programming questions",
        "Unrelated technology questions"
      ],
      "example_queries": [
        "Sample question this tool handles well",
        "Another example query",
        "Typical use case question"
      ]
    },
    "tool_relationships": {
      "provides_support_to": [
        "related-tool-name-1",
        "related-tool-name-2"
      ],
      "notes": "Description of how other tools can leverage this one"
    },
    "alwaysAllow": ["tool1", "tool2", "tool3"],
    "autoApprove": []
  }
}
```

## Field Definitions

### `domains`
Array of high-level technology domains this server specializes in:
- Use lowercase with underscores: `advantage_database`, `sql`, `performance_tuning`
- Should be broad enough for general categorization
- Typical domains: `database_operations`, `web_development`, `system_administration`

### `specialties`  
Array of specific features, operations, or concepts this server excels at:
- More specific than domains: `upsert_merge_operations`, `indexing_optimization`
- Should match terminology used in actual documentation
- Focus on unique capabilities or complex operations

### `query_types`
Array of question/request types this server handles well:
- `how_to_guides`: Step-by-step instructions
- `reference_lookup`: Syntax, parameters, API documentation
- `troubleshooting`: Error diagnosis and resolution
- `code_examples`: Working code samples and demos
- `best_practices`: Recommended approaches and patterns
- `configuration_help`: Setup and configuration guidance
- `performance_analysis`: Optimization and tuning advice

### `output_formats`
Array of response formats this server can provide:
- `explanations`: Detailed textual explanations
- `code_examples`: Formatted code snippets
- `step_by_step`: Numbered procedure lists
- `citations`: Source references and documentation links

### `use_cases`
Specific guidance for when to use (or not use) this server:

#### `best_for`
Array of specific scenarios where this server excels:
- Should be detailed and specific to the domain
- Include actual use cases from real-world scenarios
- Focus on unique value propositions

#### `not_suitable_for`
Array of scenarios where this server should NOT be used:
- Helps AI systems avoid inappropriate tool selection
- Prevents wasted queries on irrelevant servers
- Improves overall system efficiency

#### `example_queries`
Array of actual questions this server handles well:
- Use realistic user language and phrasing
- Cover different query types and complexity levels
- Help AI systems understand typical usage patterns

### `tool_relationships`
Defines how this tool interacts with other tools in the ecosystem:

#### `provides_support_to`
Array of tool names that might leverage this tool:
- Enables tool-to-tool communication
- Supports composite operations across multiple tools
- Facilitates building complex workflows

## Database-Specific Template

For database knowledge base servers, use this specialized template:

```json
"[database-name]-database-expert-[deployment]": {
  "description": "Expert knowledge base for [Database Name] - comprehensive SQL, configuration, and troubleshooting support",
  "capabilities": {
    "domains": [
      "[database_name]_database",
      "sql",
      "database_operations",
      "performance_tuning",
      "database_administration",
      "data_modeling"
    ],
    "specialties": [
      "[database_specific_feature_1]",
      "[database_specific_feature_2]",
      "transaction_management",
      "stored_procedures",
      "indexing_optimization"
    ],
    "query_types": [
      "how_to_guides",
      "reference_lookup",
      "troubleshooting",
      "code_examples",
      "best_practices",
      "configuration_help",
      "performance_analysis"
    ],
    "output_formats": ["explanations", "code_examples", "step_by_step", "citations"]
  },
  "use_cases": {
    "best_for": [
      "[Database Name] specific SQL syntax and operations",
      "[Database-specific feature] operations",
      "Database performance optimization and troubleshooting",
      "[Database Name]-specific configuration and administration"
    ],
    "not_suitable_for": [
      "Other database systems",
      "General programming questions unrelated to databases",
      "Frontend development or UI/UX questions",
      "Non-database server administration"
    ],
    "example_queries": [
      "How to perform [operation] in [Database Name]?",
      "What is the [statement] syntax in [Database Name]?",
      "How to optimize [feature] performance in [Database Name]?"
    ]
  },
  "tool_relationships": {
    "provides_support_to": [
      "[database-name]-database-connector",
      "sql-query-executor"
    ],
    "notes": "This documentation tool can be referenced by database connection tools that need [Database Name]-specific SQL syntax"
  }
}
```

## Implementation Examples

### Advantage Database Expert
```json
"advantage-database-expert-local": {
  "description": "Expert knowledge base for Advantage Database Server - comprehensive SQL, configuration, and troubleshooting support",
  "capabilities": {
    "domains": ["advantage_database", "sql", "database_operations", "performance_tuning"],
    "specialties": ["upsert_merge_operations", "indexing_optimization", "transaction_management"],
    "query_types": ["how_to_guides", "reference_lookup", "troubleshooting", "code_examples"],
    "output_formats": ["explanations", "code_examples", "step_by_step", "citations"]
  },
  "use_cases": {
    "best_for": [
      "Advantage Database Server specific SQL syntax and operations",
      "MERGE statement and upsert operations in Advantage"
    ],
    "example_queries": [
      "How to perform an upsert in Advantage Database?",
      "What is the MERGE syntax in Advantage SQL?"
    ]
  }
}
```

### Future SAP Database Expert (Example)
```json
"sap-database-expert-local": {
  "description": "Expert knowledge base for SAP HANA Database - SQL, performance optimization, and administration support",
  "capabilities": {
    "domains": ["sap_hana", "sql", "database_operations", "performance_tuning"],
    "specialties": ["column_store_operations", "sap_specific_functions", "hana_optimization"],
    "query_types": ["how_to_guides", "reference_lookup", "troubleshooting", "code_examples"],
    "output_formats": ["explanations", "code_examples", "step_by_step", "citations"]
  },
  "use_cases": {
    "best_for": [
      "SAP HANA specific SQL syntax and operations",
      "Column store optimization techniques"
    ],
    "example_queries": [
      "How to optimize column store performance in SAP HANA?",
      "What are SAP-specific SQL functions?"
    ]
  }
}
```

## Benefits for Tool Selection

### For AI Systems
1. **Domain Matching**: Match user query domains to server capabilities
2. **Specialty Scoring**: Rank servers based on specific expertise areas
3. **Use Case Filtering**: Eliminate inappropriate servers early
4. **Example-Based Learning**: Use example queries to improve matching accuracy

### For Developers
1. **Clear Documentation**: Each server's purpose is explicitly defined
2. **Maintenance Guidance**: Know what each server should and shouldn't handle
3. **Expansion Planning**: Template structure for adding new knowledge bases
4. **Tool Integration**: Understand how tools can work together

### For Users
1. **Better Results**: Queries routed to most appropriate servers
2. **Faster Responses**: Avoid querying irrelevant servers
3. **Consistent Experience**: Similar servers behave predictably
4. **Clear Expectations**: Know what each tool is designed for

This metadata schema transforms generic MCP servers into intelligent, self-describing tools that enable sophisticated tool selection and orchestration.