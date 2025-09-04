---
title: Ade Adsgetkeylength
slug: ade_adsgetkeylength
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetkeylength.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ef4c62db1be6adba01cd32f0c7bfefe5514bdd41
---

# Ade Adsgetkeylength

AdsGetKeyLength

TAdsTable.AdsGetKeyLength

Advantage TDataSet Descendant

| TAdsTable.AdsGetKeyLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the key size in bytes of the given index order.

Syntax

function AdsGetKeyLength : Word;

Description

Returns the number of bytes in each physical key in the index file. If the index key evaluates to a variable-length expression, this function will return zero for the length.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

wKeyLength := AdsTable1.AdsGetKeyLength;

{ wKeyLength equals 20 }

See Also

[AdsExtractKey](ade_adsextractkey.md)

[AdsGetKeyType](ade_adsgetkeytype.md)
