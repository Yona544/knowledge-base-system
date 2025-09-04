AdsCheckExistence




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsCheckExistence

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsCheckExistence  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsCheckExistence Advantage TDataSet Descendant ade\_Adscheckexistence Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsCheckExistence  Advantage TDataSet Descendant |  |  |  |  |

Checks for existence of a file.

Syntax

function AdsCheckExistence( strFileName : String ) : Boolean;

Parameter

|  |  |
| --- | --- |
| strFileName | File name to check the existence of. |

Description

Checks for existence of a file (any file, not just a table) named strFilename. How the existence check is done by Advantage depends on many factors. These factors include whether or not you are using a [database connection](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)) or [free connection](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)), whether you are checking for a table that is already open, or checking for a table or some other file. It also depends on the Advantage server type to which you are connected. Those server type variations are discussed below:

Advantage Internet Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a [database connection](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1))), or if that table is already open on the current connection, this function will return True. Otherwise, it is assumed the specified file does not exist, and False is returned.

Advantage Database Server and Advantage Local Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a [database connection](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1))), or if that table is already open on the current connection, this function will return True. Otherwise, a non-Advantage, low-level file access function is called from the client to check for existence of the specified file. If checking for file existence of a file on a server, this function cannot override normal access rights imposed by that server. If the client has access rights to the specified file, and it exists, True will be returned. If the specified file does not exist, or if the client does not have access rights to the specified file that does exist, this function will return False.

Example

{ determine if an image file exists on a remote Advantage server }

AdsSettings1.AdsServerTypes := [stADS\_REMOTE];

AdsTable1.AdsConnection := AdsConnection1;

AdsConnection1.ConnectPath := 'x:\data';

AdsTable1.Active := TRUE;

bDoesExist := AdsTable1.AdsCheckExistence( 'x:\data\picture.jpg' );

 

{ determine if an image file exists on a remote Advantage Database Sever when using an alias }

AdsSettings1.AdsServerTypes := [stADS\_AIS];

AdsConnection1.AliasName := 'MyAlias';

AdsTable1.AdsConnection := AdsConnection1;

AdsTable1.AdsCheckExistence( AdsConnection1.GetConnectionPath + AdsTable1.TableName );

See Also

None.