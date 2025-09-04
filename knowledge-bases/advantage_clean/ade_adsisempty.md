---
title: Ade Adsisempty
slug: ade_adsisempty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisempty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0e741624623adcfc604a31932a6f08b6c38513c2
---

# Ade Adsisempty

AdsIsEmpty

TAdsTable.AdsIsEmpty

Advantage TDataSet Descendant

| TAdsTable.AdsIsEmpty  Advantage TDataSet Descendant |  |  |  |  |

Determines if a given field is empty (null).

Syntax

function AdsIsEmpty( strFieldName : String ) : Boolean;

Parameter

| strFieldName | Name of field to query. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: TField.IsNull. See your Delphi documentation for more information about this native Delphi method.

Description

Use AdsIsEmpty to determine if the indicated field is NULL for ADTs or empty for DBFs. The NULL/empty value can vary between data types. Therefore, AdsIsEmpty can be used to be certain whether the current field value is NULL/empty.

Example

bEmpty := AdsTable1.FieldByName( Salary ).IsNull;

See Also

[AdsSetEmpty](ade_adssetempty.md)

[AdsSetField](ade_adssetfield.md)
