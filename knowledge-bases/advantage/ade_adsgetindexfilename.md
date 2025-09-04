AdsGetIndexFilename




Advantage Database Server 12  

TAdsTable.AdsGetIndexFilename

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetIndexFilename  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetIndexFilename Advantage TDataSet Descendant ade\_Adsgetindexfilename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetIndexFilename  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the full filename of this index order.

Syntax

type TAdsFilenameOptions = ( foBASENAME, foBASENAMEANDEXT, foFULLPATHNAME );

 

function AdsGetIndexFilename( eOption : TAdsFilenameOptions ) : String;

Parameter

|  |  |
| --- | --- |
| eOption | Specifies the portion of the file name desired. Valid options are foBASENAME (retrieve the name of the file without the extension), foBASENAMEANDEXT, (retrieve the name of the file with the extension), foFULLPATHNAME (retrieve the fully qualified UNC file name). |

Description

AdsGetIndexFilename returns the UNC file name of the index file containing the indicated index order.

If foFULLPATHNAME is given as the option, the fully qualified UNC path name is returned regardless of how the file was opened. For example, even if the file was opened with a drive letter style path (e.g., f:\data\file.idx), a UNC filename will be returned by this routine (e.g., \\server\volume\data\file.idx). The UNC path can include connection path information such as the port number if it was included in the connection path.  Also note that if the connection path used a server-side alias, then that alias will be in the path as opposed to the actual folder on the server.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

strFileName := AdsTable1.AdsGetIndexFileName( foFULLPATHNAME );

{ strFileName equals }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetIndexName](ade_adsgetindexname.htm)

[AdsGetTableFilename](ade_adsgettablefilename.htm)

[AdsOpenIndex](ade_adsopenindex.htm)