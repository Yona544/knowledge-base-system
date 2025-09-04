---
title: Ade Adsgetindexname
slug: ade_adsgetindexname
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetindexname.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 16072c347956ef07fc9ec97b2c45343c831d9871
---

# Ade Adsgetindexname

AdsGetIndexName

TAdsTable.AdsGetIndexName

Advantage TDataSet Descendant

| TAdsTable.AdsGetIndexName  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the name of the index order of the default index or the given Advantage Client Engine index handle.

Syntax

function AdsGetIndexName( hIndexHandle : ADSHANDLE ) : String;

Parameter

| hIndexHandle | 0 for the default index, or the Advantage Client Engine index handle. |

Description

For NTX and IDX files, this function will return the base of the file name (up to 8 characters). For CDX indexes, this function will return the tag name (up to 10 characters). For ADI indexes, this function will return the tag name (up to 128 characters).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

 

hHandle := AdsTable1.AdsGetIndexHandle( 'Tag1' );

strFileName := AdsTable1.AdsGetIndexName( hHandle );

{strFileName equals 'TAG1' }

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetIndexFilename](ade_adsgetindexfilename.md)

[AdsGetIndexHandle](ade_adsgetindexhandle.md)

[AdsGetIndexHandleByOrder](ade_adsgetindexhandlebyorder.md)

[AdsOpenIndex](ade_adsopenindex.md)
