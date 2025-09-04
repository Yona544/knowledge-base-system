GetActiveDDLinkInfo




Advantage Database Server 12  

TAdsConnection.GetActiveDDLinkInfo

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetActiveDDLinkInfo  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetActiveDDLinkInfo Advantage TDataSet Descendant ade\_Getactiveddlinkinfo\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetActiveDDLinkInfo  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Retrieves the detail information about an active link on the current connection.

Syntax

procedure TAdsConnection.GetActiveDDLinkInfo( iLinkNum : integer;

poList : TStrings);

Parameters

|  |  |
| --- | --- |
| iLinkNum (I) | The ordinal number of the link to retrieve detail information about starting from 1. |
| poList (I/O) | A descendant of the TStrings class to hold the returned information. |

Remarks

This function is used to retrieve the detail information about an active link on the current connection. The information returned is the link alias, if there is one, the user name used to authenticate into the linked data dictionary, and the path of the linked data dictionary.

Example

This procedure will drop all active links on the current connection.

procedure DropAllLinks;

var

oConnection : TAdsConnection;

oLinkInfo : TStringList;

begin

 

try

{\* Create the components \*}

oConnection := TAdsConnection.Create( nil );

oLinkInfo := TStringList.Create;

 

{\* Connect to the Master Data Dictionary \*}

oConnection.ConnectPath := 'n:\MyData\Master.add';

oConnection.AdsServerTypes := [stADS\_REMOTE];

oConnection.UserName := 'JohnDoe';

oConnection.Password := 'anonymous';

oConnection.IsConnected := True;

 

while ( oConnection.GetNumActiveDDLinks > 0 ) do

begin

 

oLinkInfo.Clear;

oConnection.GetActiveDDLinkInfo( 1, oLinkInfo );

 

{\* Use AliasName to Drop the link if one exists \*}

if ( oLinkInfo.Strings[0] <> '' ) then

begin

oConnection.DropDDLink( oLinkInfo.Strings[0], False );

end

else {\* Use the Alias Path to the drop the link \*}

begin

oConnection.DropDDLink( oLinkInfo.Strings[2], False );

end

 

 

end;

 

 

finally

 

if ( Assigned( oLinkInfo ) ) then

begin

FreeAndNil( oLinkInfo );

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

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.htm)