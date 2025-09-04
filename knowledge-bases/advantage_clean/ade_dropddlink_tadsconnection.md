---
title: Ade Dropddlink Tadsconnection
slug: ade_dropddlink_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_dropddlink_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3f0a962fe84950db1df35ba2025bad0f29f1cbd8
---

# Ade Dropddlink Tadsconnection

DropDDLink

TAdsConnection.DropDDLink

Advantage TDataSet Descendant

| TAdsConnection.DropDDLink  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Removes either a local link or a global link from the current connection.

Syntax

procedure TAdsConnection.DropDDLink( strLinkedDD : string;

bDropGlobal : boolean);

Parameters

| strLinkedDD (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| bDropGlobal (I) | True to remove the global link alias from the data dictionary. If this parameter is True, the strLinkedDD parameter must specify the link alias in the data dictionary. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error may be returned if the bDropGlobal parameter is True and the specified link cannot be found in the data dictionary. |

Remarks

This function can be used to either drop an active link from the current connection or remove a global link from the data dictionary. Since the database server maintains information on the active links, dropping active links from the current connection will free some resources consumed by the server.

DROP permissions on the link are required to drop a link from the data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database. The implicit link is then dropped.

procedure CreateAndUseLink;

var

oConnection : TAdsConnection;

oQuery : TAdsQuery;

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

 

oQuery.Open;

 

oQuery.Close;

 

oConnection.DropDDLink( 'n:\MyData\archive1\', False );

 

oConnection.IsConnected := False;

 

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

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.md)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.md)
