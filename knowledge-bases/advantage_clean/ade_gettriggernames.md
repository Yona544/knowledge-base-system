---
title: Ade Gettriggernames
slug: ade_gettriggernames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettriggernames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 158838f3fc8d307d06f885d30760455154323d3d
---

# Ade Gettriggernames

GetTriggerNames

TAdsDictionary.GetTriggerNames

Advantage TDataSet Descendant

| TAdsDictionary.GetTriggerNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetTriggerNames( poTriggerNames : TStringList );

 

TAdsDictionary.GetTriggerNames( strTableName : string;

poTriggerNames : TStringList );

Parameters

| strTableName (I) | The name of the table to retrieve triggers for. |
| poTriggerNames (O) | The list of trigger names names. |

Remarks

This method will retrieve the name of all triggers in a database. If strTableName is specified then only the name of triggers associated with that table will be returned.

See Also

[GetQualifiedTriggerNames](ade_getqualifiedtriggernames.md)

[GetDatabaseTriggerNames](ade_getdatabasetriggernames.md)
