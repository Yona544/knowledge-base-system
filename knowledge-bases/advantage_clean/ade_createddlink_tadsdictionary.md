---
title: Ade Createddlink Tadsdictionary
slug: ade_createddlink_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_createddlink_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 9f644f82c346263de827e7cd27faa146613fec98
---

# Ade Createddlink Tadsdictionary

CreateDDLink

TAdsDictionary.CreateDDLink

Advantage TDataSet Descendant

| TAdsDictionary.CreateDDLink  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Creates a link to another data dictionary from the current database connection), optionally making the link a global link that is available to all users connected to the database.

Syntax

procedure TAdsDictionary.CreateDDLink( strLinkAlias : string;

strLinkedDDPath : string;

strUserName : string;

strPassword : string;

Options : TAdsLinkOptions );

 

TAdsLinkOption = ( loGlobal, loAuthenticateActiveUser, loPathIsStatic );

TAdsLinkOptions = set of TAdsLinkOption;

Parameters

| strLinkAlias (I) | Name of the link to create. This name is used in SQL statements to reference the tables associated with the linked data dictionary. |
| strLinkedDDPath (I) | Path to the data dictionary that will be linked to the current connection. The path can be either a full UNC path or a relative path based on the connection path of the current connection. |
| strUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| strPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| Options (I) | Set of TAdsLinkOption specifying the properties of the link.  loGlobal: Specifies the link alias as available to all users connecting to this data dictionary. All information needed to re-create this link is stored in the data dictionary. By default, this option is turned off, and the link created is local to the current connection.  loAuthenticateActiveUser: Specifies that the user name and password of the current connection is used for authenticating to the linked data dictionary as well. This option is off by default so the strUserName and strPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  loPathIsStatic: This option can be specified in conjunction with the loGlobal option. It determines whether the relative or full path of the linked data dictionary is stored in the current database. If the loPathIsStatic option is specified, the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path be supplied in the strLinkedDDPath parameter when this option is specified. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if a local or global link with an identical alias already exists on the current connection. If creating a global link, this error will be returned if the link name is already used for other objects, such as tables, views or stored procedures, in the database. |

Remarks

This function creates a named link to another data dictionary on the current connection. The name can then be used in SQL statements to reference tables in the linked data dictionary. The permissions to the tables in the linked data dictionary are determined by the user name that is used to authenticate into the linked data dictionary.

If the link alias is made global, the link alias is available to all authorized users of the database. Access to the link can be controlled by granting or revoking user or group permissions to the link alias.

CREATE LINK permissions are required to create a new link in the data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

This is an example of creating a global link to a data dictionary. After opening the master data dictionary, a global link to the archive data dictionary is created. The link authenticates the active user in the linked data dictionary before allowing access to the tables contained in the archive data dictionary.

procedure CreateGlobalLink;

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

 

oDictionary.CreateDDLink( 'LinkA',

'Archive.add',

'',

'',

[loAuthenticateActiveUser, loGlobal] );

 

oDictionary.IsConnected := False;

 

FreeAndNil( oDictionary );

 

end;

See Also

[DropDDLink](ade_dropddlink_tadsdictionary.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.md)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.md)
