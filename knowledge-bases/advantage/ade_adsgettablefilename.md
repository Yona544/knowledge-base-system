AdsGetTableFileName




Advantage Database Server 12  

TAdsTable.AdsGetTableFileName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetTableFileName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetTableFileName Advantage TDataSet Descendant ade\_Adsgettablefilename Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetTableFileName  Advantage TDataSet Descendant |  |  |  |  |

Returns the table name as the base name, the base name with extension, or the full path name (UNC format).

Syntax

type TAdsFilenameOptions = ( foBASENAME, FOBASENAMEANDEXT, foFULLPATHNAME );

 

function AdsGetTableFileName( eOption : TAdsFilenameOptions ) : String;

Parameter

|  |  |
| --- | --- |
| eOption | Option of what the file name should look like for return. |

Description

If the foFULLPATHNAME is given as the option, then the fully qualified UNC path name is returned regardless of how the file was opened. For example, even if the file was opened with a drive letter style path (e.g., f:\data\file.dbf), a UNC file name will be returned by this routine (e.g., \\server\volume\data\file.dbf). The UNC path can include connection path information such as the port number if it was included in the connection path.  Also note that if the connection path used a server-side alias, then that alias will be in the path as opposed to the actual folder on the server.

Example

AdsTable1.TableName := 'Employee';

AdsTable1.Active := TRUE;

 

strFileName := AdsTable1.AdsGetTableFilename( foFullPathName );

{ strFileName equals \\server\share\path\Employee.ADT }

See Also

[AdsCreateTable](ade_adscreatetable.htm)

[AdsGetIndexFilename](ade_adsgetindexfilename.htm)