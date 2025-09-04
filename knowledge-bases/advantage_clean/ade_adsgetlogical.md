---
title: Ade Adsgetlogical
slug: ade_adsgetlogical
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetlogical.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6e1e8fdcbb48427597fc2f47671efd8fa9140514
---

# Ade Adsgetlogical

AdsGetLogical

TAdsTable.AdsGetLogical

Advantage TDataSet Descendant

| TAdsTable.AdsGetLogical  Advantage TDataSet Descendant |  |  |  |  |

Retrieves a logical value from the given field.

Syntax

function AdsGetLogical( strFieldName : String ) : Boolean;

Parameter

| strFieldName | Name of field to retrieve. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsBoolean. See your Delphi documentation for more information about this native Delphi method.

Description

The value returned will be either True (1) or False (0). AdsGetLogical also returns False if the logical field contains a NULL value. To determine if a False return type is NULL or assigned to False, call [AdsIsEmpty](ade_adsisempty.md) or [AdsGetString](ade_adsgetstring.md) on the numeric field.

Example

bValue := AdsTable1.FieldByName( IsMarried ).AsBoolean;

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsSetLogical](ade_adssetlogical.md)
