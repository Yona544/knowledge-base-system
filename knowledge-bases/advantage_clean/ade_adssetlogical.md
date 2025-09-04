---
title: Ade Adssetlogical
slug: ade_adssetlogical
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetlogical.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 7ce6662f13777b18bfe06aeada9bfc51fbb98bf2
---

# Ade Adssetlogical

AdsSetLogical

TAdsTable.AdsSetLogical

Advantage TDataSet Descendant

| TAdsTable.AdsSetLogical  Advantage TDataSet Descendant |  |  |  |  |

Stores the given logical value in the given field.

Syntax

procedure AdsSetLogical( strFieldName : String; bValue : Boolean );

Parameters

| strFieldName | Name of field to set. |

| bValue | Store this value in the field ( False/True ) . |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.AsBoolean. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetLogical can set the value of the logical field to True or False. To set a logical field to NULL, use [AdsSetEmpty](ade_adssetempty.md).

Example

AdsTable1.FieldByName( IsMarried ).AsBoolean := TRUE;

See Also

[AdsGetLogical](ade_adsgetlogical.md)

[AdsSetField](ade_adssetfield.md)
