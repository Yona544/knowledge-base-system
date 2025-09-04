---
title: Ade Dropddlink Tadsdictionary
slug: ade_dropddlink_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_dropddlink_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 65cddd93165d6f673c11824d77b82b5c2bd3037a
---

# Ade Dropddlink Tadsdictionary

DropDDLink

TAdsDictionary.DropDDLink

Advantage TDataSet Descendant

| TAdsDictionary.DropDDLink  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Removes either a local link or a global link from the current connection.

Syntax

procedure TAdsDictionary.DropDDLink( strLinkedDD : string;

bDropGlobal : boolean);

Parameters

| strLinkedDD (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| bDropGlobal (I) | True to remove the global link alias from the data dictionary. If this parameter is True, the strLinkedDD parameter must specify the link alias in the data dictionary. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error may be returned if the bDropGlobal parameter is True and the specified link cannot be found in the data dictionary. |

Remarks

This function can be used to either drop an active link from the current connection or remove a global link from the data dictionary. Since the database server maintains information on the active links, dropping active links from the current connection will free some resources consumed by the server.

DROP permissions on the link are required to drop a link from the data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

The following example drops a global data dictionary link.

procedure DropGlobalLink;

var

oDictionary : TAdsDictionary;

begin

 

oDictionary := TAdsDictionary.Create( nil );

 

oDictionary.ConnectPath := 'n:\MyData\Master.add';

oDictionary.AdsServerTypes := [stADS\_REMOTE];

oDictionary.UserName := 'AdsSys';

oDictionary.Password := 'SuperSecret';

oDictionary.LoginPrompt := False;

 

oDictionary.IsConnected := True;

 

oDictionary.DropDDLink( 'LinkA',

True );

 

oDictionary.IsConnected := False;

 

FreeAndNil( oDictionary );

 

end;

See Also

[CreateDDLink](ade_createddlink_tadsdictionary.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.md)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.md)
