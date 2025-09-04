---
title: Ade Bookmark
slug: ade_bookmark
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_bookmark.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f7d92e69b0841f72a7605d987bcff193b075a153
---

# Ade Bookmark

Bookmark

TAdsTable/TAdsQuery.Bookmark

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.Bookmark  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Specifies the current bookmark in the dataset.

Syntax

type TBookmarkStr: string;

 

property Bookmark: TBookmarkStr;

Description

Bookmark gets or sets the current bookmark in a dataset. A bookmark provides a convenient way to mark a location in a dataset so that an application can easily return to that location quickly. The string contains the record number.

Note The bookmark is the record number of the physical record. This can cause some problems with bookmark validation of a deleted record, and that record number reused due to record reuse associated to the Advantage Data Tables.
