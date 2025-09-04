---
title: Ade Params
slug: ade_params
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_params.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f3c9bdf222131cc4725d813fe32eca6dae11dc2b
---

# Ade Params

Params

TAdsQuery.Params

Advantage TDataSet Descendant

| TAdsQuery.Params  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

The Advantage Params property is used much like the Delphi TQuery.Params property. There are, however, subtle differences. When a date or timestamp parameter value is being supplied in a string format, then the date must be in either the SQL 92 standard format of CCYY-MM-DD or in the global date format (see [TAdsSettings.DateFormat](ade_dateformat.md)).

Example

AdsQuery1.ParamByName( DateVal ).AsString = 1999-02-14;

The date format in the Delphi ShortDateFormat may not be used. If the string is in the Delphi ShortDateFormat, set the field as a date as in this example:

AdsQuery1.ParamByName('DateVal').AsDateTime := StrToDate( 2/14/99 );
