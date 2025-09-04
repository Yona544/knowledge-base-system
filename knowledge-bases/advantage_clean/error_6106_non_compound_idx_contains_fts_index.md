---
title: Error 6106 Non Compound Idx Contains Fts Index
slug: error_6106_non_compound_idx_contains_fts_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6106_non_compound_idx_contains_fts_index.htm
source: Advantage CHM
tags:
  - error
checksum: fee79883a67d436dcb8e25096aae84bc5a9dec0c
---

# Error 6106 Non Compound Idx Contains Fts Index

6106 Non-compound IDX contains FTS index

6106 Non-compound IDX contains FTS index

Advantage Error Guide

| 6106 Non-compound IDX contains FTS index  Advantage Error Guide |  |  |  |  |

Problem: The Advantage Clipper RDD attempted to open a non-compound index (IDX) file that contains a full text search (FTS) index. The Advantage Clipper RDD does not support IDX index files with FTS indexes.

Solution: Use compound index (CDX) files.
