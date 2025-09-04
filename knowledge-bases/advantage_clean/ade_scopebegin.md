---
title: Ade Scopebegin
slug: ade_scopebegin
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_scopebegin.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4f94b71b41044509c3c491652e75b4d9b5ccb37c
---

# Ade Scopebegin

ScopeBegin

TAdsTable/TAdsQuery.ScopeBegin

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.ScopeBegin  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Specifies the text of the beginning scope for a dataset.

Syntax

property ScopeBegin: string;

Description

Use ScopeBegin to specify an indexed dataset filter. When ScopeBegin is applied to a dataset, only those records following the ScopeBegin are available to an application. ScopeBegin contains the string that is the value for the index. For example, the following ScopeBegin string displays only those records and following where the indexed State field is anything after CA. Programmatically set:

AdsTable1.ScopeBegin := CA;

To set a scope on indexes built on date, time, or timestamp fields, the date and time values must be formatted as text. The date should be formatted according to [DateFormat](ade_dateformat.md). For example, to set a scope on a date index, an application might use "2/25/1997" as the value. To set a scope on a timestamp index, the value could be "2/25/1997 3:25pm".

ScopeBegin can be used in conjunction with [ScopeEnd](ade_scopeend.md).

Note Ranges are implemented internally as scopes. Ranges provide a very useful means to automatically produce the value necessary to set the scope. For this reason, use of ranges is easier and more versatile.
