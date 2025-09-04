AdsGetIndexName




Advantage Database Server 12  

TAdsTable.AdsGetIndexName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetIndexName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetIndexName Advantage TDataSet Descendant ade\_Adsgetindexname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetIndexName  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the name of the index order of the default index or the given Advantage Client Engine index handle.

Syntax

function AdsGetIndexName( hIndexHandle : ADSHANDLE ) : String;

Parameter

|  |  |
| --- | --- |
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

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetIndexFilename](ade_adsgetindexfilename.htm)

[AdsGetIndexHandle](ade_adsgetindexhandle.htm)

[AdsGetIndexHandleByOrder](ade_adsgetindexhandlebyorder.htm)

[AdsOpenIndex](ade_adsopenindex.htm)