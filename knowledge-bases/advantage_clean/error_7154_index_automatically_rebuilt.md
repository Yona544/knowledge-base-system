---
title: Error 7154 Index Automatically Rebuilt
slug: error_7154_index_automatically_rebuilt
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7154_index_automatically_rebuilt.htm
source: Advantage CHM
tags:
  - error
checksum: 9bd21578a967c0d64dcc79ebf88b943b77bfb2ca
---

# Error 7154 Index Automatically Rebuilt

7154 Index Automatically Rebuilt

7154 Index Automatically Rebuilt

Advantage Error Guide

| 7154 Index Automatically Rebuilt  Advantage Error Guide |  |  |  |  |

A 7154 error indicates an index file was not closed properly the last time it was opened. The server detected this state and automatically re-indexed the file.

This can happen if you use a file system command to copy an index file while Advantage has the file open. Advantage may have portions of the file cached, and if this cache has not been flushed to disk you can not make copies of the file until Advantage closes it. Any copies you make will need to be re-indexed before they are opened again by Advantage. If this situation arises, Advantage will detect it and automatically re-index and log the 7154 error.
