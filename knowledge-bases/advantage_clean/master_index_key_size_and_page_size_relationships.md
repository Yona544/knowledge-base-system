---
title: Master Index Key Size And Page Size Relationships
slug: master_index_key_size_and_page_size_relationships
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_index_key_size_and_page_size_relationships.htm
source: Advantage CHM
tags:
  - master
checksum: 70efba04f819ce7885da648140caca1720010c65
---

# Master Index Key Size And Page Size Relationships

Index Key Size and Page Size Relationships

Index Key Size and Page Size Relationships

Advantage Concepts

| Index Key Size and Page Size Relationships  Advantage Concepts |  |  |  |  |

The following formulas show the relationship between index key size K and index file page size P. For a discussion about index page sizes and key sizes, please see [Index Page Size](master_index_page_size.md).

The symbol PO refers to page overhead. In most cases, the overhead is 12. If an ADI index is encrypted with [AES encryption](master_encryption.md), then an extra 8 bytes are needed in the page for storing additional information. So if using AES encryption, PO=20.

The minimum required page size for a given key is: P = ( K + 8 ) \* 2 + PO

To guarantee at least three keys per page for better balancing: P >= ( K + 8 ) \* 3 + PO

For a given page size, the maximum key size supported is: K = (( P - PO ) / 2 ) - 8

For a given page size, optimal balancing is given by: K <= (( P - PO ) / 3 ) - 8

If a key size is 400 bytes, for example, then the page size must be at least 828 bytes in order to be able to build the index and should be at least 1236 bytes for better balancing. It probably makes sense to round the page size up to the next power of 2 for best I/O performance. Thus, the best page size for a 400-byte key is probably 2048 bytes. Note that although the required page size is based on the non-compressed key size, each physical index page may contain a large number of compressed keys.

Given a page size of 512 bytes, the largest possible key size for an index in that file is 242 bytes. For a page size of 8192, the maximum key size is 4082 bytes.

As a general rule, the following table shows what might be a good way to partition index orders into separate index files based on the key sizes. This assumes AES encryption is not being used.

| Key Size | Index File Page Size |
| 1 - 158 | 512 |
| 159 - 329 | 1024 |
| 330 - 670 | 2048 |
| 671 - 1353 | 4096 |
| 1354 - 4082 | 8192 |
