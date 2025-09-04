---
title: Master System Publicationarticles 2
slug: master_system_publicationarticles_2
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_publicationarticles_2.htm
source: Advantage CHM
tags:
  - master
checksum: 0e7d78ea948872636cdb7115a2657a50aa149b84
---

# Master System Publicationarticles 2

system.ansi\_publicationarticles

system.ansi\_publicationarticles

Advantage SQL Engine

| system.ansi\_publicationarticles  Advantage SQL Engine |  |  |  |  |

Contains one row for each publication article in the database. This view can also be referenced as system.articles.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Article name. |
| Parent | Character | 200 | The publication this article belongs to. |
| Ident\_Columns | Memo | Variable | This is the semicolon-delimited list of columns that are used to identify the record at the target database. |
| Filter | Memo | Variable | The replication filter that is used to determine if an updated record should be replicated. |
| Include\_Columns | Memo | Variable | The vertical filter that specifies which columns to replicate. |
| Exclude\_Columns | Memo | Variable | The vertical filter that specifies which columns to exclude from replication. |
| Update\_Merge | Logical | 1 | Flag that indicates if the article uses SQL MERGE statements when performing UPDATEs at the target. |
| Insert\_Merge | Logical | 1 | Flag that indicates if the article uses SQL MERGE statements when performing INSERTs at the target. |
