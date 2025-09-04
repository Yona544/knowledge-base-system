---
title: Ade Adsgetmemodatatype
slug: ade_adsgetmemodatatype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetmemodatatype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 33fbba99f446f418153a827bad9ad8343e78fda4
---

# Ade Adsgetmemodatatype

AdsGetMemoDataType

TAdsTable.AdsGetMemoDataType

Advantage TDataSet Descendant

| TAdsTable.AdsGetMemoDataType  Advantage TDataSet Descendant |  |  |  |  |

Returns the specific type of data stored in a DBF memo field.

Syntax

type TAdsMemoDataTypes = (mdtMEMO, mdtBINARY, mdtIMAGE );

 

function AdsGetMemoDataType( strFieldName : String ) : TAdsMemoDataTypes;

Parameter

| strFieldName | Name of the field to check the memo type. |

Description

AdsGetMemoDataType returns the specific type of data stored in a DBF memo field. A type of mdtIMAGE indicates that an image is stored in the DBF memo field. mdtBINARY indicates that some kind of generic binary data is in the DBF memo field. If the DBF field is a standard character memo, the function will return mdtMEMO for pusType. ADT tables cannot store binary and image data in standard character memo fields, so mdtMEMO will always be returned.

Example

AdsTable1.Next;

if ( AdsTable1.AdsGetMemoDataType( 'Notes' ) = mdtMEMO ) then

begin

DBMemo1.DataField := 'Notes';

end;

See Also

[AdsGetBinary](ade_adsgetbinary.md)

[AdsGetBinaryLength](ade_adsgetbinarylength.md)

[AdsGetMemoLength](ade_adsgetmemolength.md)

[AdsGetString](ade_adsgetstring.md)

[AdsSetBinary](ade_adssetbinary.md)
