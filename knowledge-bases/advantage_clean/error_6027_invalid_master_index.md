---
title: Error 6027 Invalid Master Index
slug: error_6027_invalid_master_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6027_invalid_master_index.htm
source: Advantage CHM
tags:
  - error
checksum: ca62e011bf9c67bad933c0fae8e96b9802860883
---

# Error 6027 Invalid Master Index

6027 Invalid master index

6027 Invalid master index

Advantage Error Guide

| 6027 Invalid master index  Advantage Error Guide |  |  |  |  |

Problem: A tag that already existed in a CDX was being reindexed using a master index, but the master index was the tag being reindexed.

Solution: If reindexing an existing tag such that a master index is involved (e.g., the tag is a subindex), make sure the active index order is not set to the index that is to be reindexed.
