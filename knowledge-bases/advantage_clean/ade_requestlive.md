---
title: Ade Requestlive
slug: ade_requestlive
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_requestlive.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 77bff22ce7b3d4cd810befe994f7f5d6fd7b5f9f
---

# Ade Requestlive

RequestLive

TAdsQuery.RequestLive

Advantage TDataSet Descendant

| TAdsQuery.RequestLive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Specifies whether an application expects to receive an updateable result set from Advantage when the query executes.

Syntax

property RequestLive: Boolean;

Description

Set RequestLive to specify whether or not Advantage should attempt to return an updateable result set to the application. RequestLive is False by default, meaning that a query always returns a read-only result set.

Set RequestLive to True to request an updateable result set. Setting RequestLive to True does not guarantee that an updateable result set is returned by Advantage. Advantage returns an updateable result set (via a dynamic cursor) only if the SELECT syntax of the query conforms to the syntax requirements for a live result set.

If RequestLive is True, but the syntax does not conform to the requirements, Advantage returns a static cursor and read-only result set.

With Advantage, the RequestLive property only allows you to request an updateable vs. a read-only result set. It does not allow you to request a dynamic (live) cursor vs. a static cursor. For example, if RequestLive is set to False, and the SELECT statement results in a dynamic cursor, the dynamic cursor will be treated as read-only by the Advantage TDataSet Descendant. If you wish to force a cursor to be static, specify the {static} escape clause in your SELECT statement. For example, 'SELECT {static} \* FROM table' will always result in a static (and read-only) cursor being returned by Advantage.

After activating the TAdsQuery, inspect the CanModify property to determine whether the request for a live result set was successful.
