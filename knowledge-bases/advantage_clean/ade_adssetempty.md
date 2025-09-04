---
title: Ade Adssetempty
slug: ade_adssetempty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssetempty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 12e4ef3ff032c24b3b665cbef8edcdbbb8d0340c
---

# Ade Adssetempty

AdsSetEmpty

TAdsTable.AdsSetEmpty

Advantage TDataSet Descendant

| TAdsTable.AdsSetEmpty  Advantage TDataSet Descendant |  |  |  |  |

Sets the given field to its NULL value when using ADTs or to its empty value when using DBFs.

Syntax

procedure AdsSetEmpty( strFieldName : String );

Parameter

| strFieldName | Name of field to set to empty/null. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.Clear. See your Delphi documentation for more information about this native Delphi method.

Description

Null and empty values vary by field type. AdsSetEmpty ensures that the value set in the field is what Advantage expects as a NULL value for ADTs or an empty value for DBFs.

Example

AdsTable1.FieldByName( LastName ).Clear;

See Also

[AdsIsEmpty](ade_adsisempty.md)

[AdsSetField](ade_adssetfield.md)
