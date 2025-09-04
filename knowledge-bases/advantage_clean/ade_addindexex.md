---
title: Ade Addindexex
slug: ade_addindexex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addindexex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1c0cb4238f418d5ceef3edb76434ccaeb9452e9e
---

# Ade Addindexex

AddIndexEx

TAdsDataSet.AddIndexEx

Advantage TDataSet Descendant

| TAdsDataSet.AddIndexEx  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Creates a new index for the table.

Syntax

type TIndexOptions = set of (ixPrimary, ixUnique, ixDescending, ixCaseInsensitive, ixExpression);

 

procedure AddIndexEx( strFileName : string; strIndexName : string; strFields: string; poOptions : TIndexOptions );

Description

AddIndexEx behaves the same as the [TAdsDataSet.AddIndex](ade_addindex.md) method, except AddIndexEx allows the caller to specify the index file the new index tag will belong to.

Use AddIndexEx when you find it necessary to create a non-auto-open index.

The most common use of AddIndexEx is to create temporary index files when using an Advantage Data Dictionary. Indexes created by users without administrative rights are not included in the data dictionary, which makes it necessary for the caller to specify the index file the new index tag will belong to.
