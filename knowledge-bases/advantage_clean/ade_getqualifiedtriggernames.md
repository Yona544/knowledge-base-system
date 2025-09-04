---
title: Ade Getqualifiedtriggernames
slug: ade_getqualifiedtriggernames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getqualifiedtriggernames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d984b0f957ca5d09506aa51d51bbafb0ca0c024d
---

# Ade Getqualifiedtriggernames

GetQualifiedTriggerNames

TAdsDictionary.GetQualifiedTriggerNames

Advantage TDataSet Descendant

| TAdsDictionary.GetQualifiedTriggerNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetQualifiedTriggerNames( poTriggerNames : TStringList );

TAdsDictionary.GetQualifiedTriggerNames( strTableName : string;

poTriggerNames : TStringList );

Parameters

| strTableName (I) | The name of the table to retrieve triggers for. |
| poTriggerNames (O) | The list of trigger names. |

Remarks

This method will retrieve the name of all triggers in a database, or if strTableName is specified, then only the name of triggers associated with that table will be returned.

This method retrieves the qualified name of a trigger object. The qualified name includes the table name prefix, followed by two colon characters ( :: ), followed by the trigger name.

See Also

[GetTriggerNames](ade_gettriggernames.md)

[GetDatabaseTriggerNames](ade_getdatabasetriggernames.md)
