---
title: Ade Adsgetmemolength
slug: ade_adsgetmemolength
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetmemolength.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6c3b5679bada946c712cdbb20e09627c71617e24
---

# Ade Adsgetmemolength

AdsGetMemoLength

TAdsTable.AdsGetMemoLength

Advantage TDataSet Descendant

| TAdsTable.AdsGetMemoLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the length of the specified memo field of the current record.

Syntax

function AdsGetMemoLength( strFieldName : String ) : Longint;

Parameter

| strFieldName | Name of memo field. |

Description

AdsGetMemoLength returns the length of the specified memo field in characters.  For Unicode memo fields of type ADS\_NMEMO this is the number of 16-bit code units.  For memo fields of type ADS\_MEMO, the length in characters is the same as the length in bytes. AdsGetMemoLength will not support binary object fields. Use AdsGetBinaryLength for binary fields.

Example

lMemoLength := AdsTable1.AdsGetMemoLength( Notes );

See Also

[AdsGetField](ade_adsgetfield.md)

[AdsGetFieldLength](ade_adsgetfieldlength.md)

[AdsGetFieldType](ade_adsgetfieldtype.md)

[AdsGetMemoDataType](ade_adsgetmemodatatype.md)

[AdsGetString](ade_adsgetstring.md)
