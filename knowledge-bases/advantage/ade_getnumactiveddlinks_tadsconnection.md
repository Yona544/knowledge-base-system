GetNumActiveDDLinks




Advantage Database Server 12  

TAdsConnection.GetNumActiveDDLinks

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetNumActiveDDLinks  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetNumActiveDDLinks Advantage TDataSet Descendant ade\_Getnumactiveddlinks\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetNumActiveDDLinks  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Retrieves the number of links active on the current connection.

Syntax

function TAdsConnection.GetNumActiveDDLinks : integer;

Remarks

This function is used to retrieve the number of active links on the current connection. A global link that is stored in the data dictionary is not active until it is used in an SQL statement on the current connection.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database so the AdsGetNumActiveLinks should return 1 in the output.

procedure NumberOfActiveLinks;

var

oConnection : TAdsConnection;

oQuery : TAdsQuery;

iLinkCount : integer;

begin

 

try

{\* Create the components \*}

oConnection := TAdsConnection.Create( nil );

oQuery := TAdsQuery.Create( nil );

 

{\* Connect to the Master Data Dictionary \*}

oConnection.ConnectPath := 'n:\MyData\Master.add';

oConnection.AdsServerTypes := [stADS\_REMOTE];

oConnection.UserName := 'JohnDoe';

oConnection.Password := 'anonymous';

oConnection.IsConnected := True;

 

 

{\* SQL Statement creates implicit link. \*}

oQuery.DatabaseName := oConnection.Name;

 

oQuery.SQL.Clear;

oQuery.SQL.Add( 'SELECT Max(LastDate) FROM "n:\MyData\archive1\".Table1' );

 

oQuery.ExecSQL;

 

{\* Get the number of active links \*}

iLinkCount := oConnection.GetNumActiveDDLinks;

 

 

finally

 

if ( Assigned( oQuery ) ) then

begin

FreeAndNil( oQuery );

end;

 

if ( Assigned( oConnection ) ) then

begin

FreeAndNil( oConnection );

end

end;

end;

See Also

[CreateDDLink](ade_createddlink_tadsconnection.htm)

[DropDDLink](ade_dropddlink_tadsconnection.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[RevokePermissions](ade_revokepermissions_tadsdictionary.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.htm)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.htm)