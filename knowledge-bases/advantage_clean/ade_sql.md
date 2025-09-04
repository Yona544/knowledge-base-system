---
title: Ade Sql
slug: ade_sql
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_sql.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8d45391a82ca404bf1dec02b962303678090b5bd
---

# Ade Sql

SQL

TAdsQuery.SQL

Advantage TDataSet Descendant

| TAdsQuery.SQL  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

The Advantage SQL parameter is used much like the Delphi TQuery.SQL property. There are, however, subtle differences. When a date or timestamp parameter value is being supplied in a string format, then the date must be in either the SQL 92 standard format of CCYY-MM-DD or in the global date format (see [TAdsSettings.DateFormat](ade_dateformat.md)).

Example

AdsQuery1.SQL.Add( select \* from DataFile where DateField < 1999-02-14 );

The date format in the Delphi ShortDateFormat may not be used. If the string is in the Delphi ShortDateFormat, then you may consider replace the date constant with a named parameter and supplying the parameter value as date value as in this example:

AdsQuery1.SQL.Add( select \* from DataFile where DateField < :DateVal);

AdsQuery1.ParamByName('DateVal').AsDateTime := StrToDate( 2/14/99 );
