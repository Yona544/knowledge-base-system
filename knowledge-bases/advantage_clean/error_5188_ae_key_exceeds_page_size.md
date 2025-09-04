---
title: Error 5188 Ae Key Exceeds Page Size
slug: error_5188_ae_key_exceeds_page_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5188_ae_key_exceeds_page_size.htm
source: Advantage CHM
tags:
  - error
checksum: 004159659c16219201f74aa7584bf092b31f34fb
---

# Error 5188 Ae Key Exceeds Page Size

5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE

5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE

Advantage Error Guide

| 5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE  Advantage Error Guide |  |  |  |  |

The index key size is too large for the page file size. If you are creating a new index order in an existing index file, Advantage will attempt to automatically rebuild the index with a large enough page size for the new index being built. If it cannot do this, it will be necessary to reindex the file with a larger page size. If you are creating an index order in a new index file, then you should either specify a larger page size or allow Advantage to compute the default page size.

See [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for the specific equations.
