---
title: Ade Getnumactiveddlinks Tadsconnection
slug: ade_getnumactiveddlinks_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getnumactiveddlinks_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 23ffc1aff470cf70c83a3a2fa0b4fb6ddb9fc0a8
---

# Ade Getnumactiveddlinks Tadsconnection

GetNumActiveDDLinks

TAdsConnection.GetNumActiveDDLinks

Advantage TDataSet Descendant

| TAdsConnection.GetNumActiveDDLinks  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

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

[CreateDDLink](ade_createddlink_tadsconnection.md)

[DropDDLink](ade_dropddlink_tadsconnection.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.md)
