---
title: Ade Modifylink
slug: ade_modifylink
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_modifylink.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8471be13dc71654dd93396891727d3e898f08d4e
---

# Ade Modifylink

ModifyLink

TAdsDictionary.ModifyLink

Advantage TDataSet Descendant

| TAdsDictionary.ModifyLink  Advantage TDataSet Descendant |  |  |  |  |

Modifies an existing global data dictionary link.

Syntax

procedure TAdsDictionary.ModifyLink( strLinkAlias : string;

strLinkedDDPath : string;

strUserName : string;

strPassword : string;

Options : TAdsLinkOptions );

 

TAdsLinkOption = ( loGlobal, loAuthenticateActiveUser, loPathIsStatic );

TAdsLinkOptions = set of TAdsLinkOption;

Parameters

| strLinkAlias (I) | Name of the existing global link. |
| strLinkedDDPath (I) | Path to the data dictionary that will be linked to the connection passed in the hDBConn parameter. The path can be either a full UNC path or a relative path based on the connection path of the current connection. |
| strUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| strPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| Options (I) | Set of TAdsLinkOptions specifying the properties of the link.  loAuthenticateActiveUser: Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. This option is off by default so the strUserName and strPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  loPathIsStatic: Specifies whether the relative or full path of the linked data dictionary is stored in the current database. If the loPathIsStatic option is specified, the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the strLinkedDDPath parameter when this option is specified. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the global link with the given alias cannot be found. |

Remarks

This function modifies an existing global link to another data dictionary on the current connection. The primary benefit of using this API instead of deleting and re-creating the link is that it maintains existing permissions on the link object. This API can only be used to modify global links; local link objects cannot be modified.

Example

This is an example of creating then modifying a global link to a data dictionary. After opening the master data dictionary, a global link to archive data dictionary is created. The link is then changed to not authenticate the active user in the archive data dictionary.

procedure ModifyGlobalLink;

var

poDictionary : TAdsDictionary;

begin

 

poDictionary := TAdsDictionary.Create( nil );

 

try

 

poDictionary.ConnectPath := 'n:\MyData\Master.add';

poDictionary.AdsServerTypes := [stADS\_REMOTE];

poDictionary.UserName := 'AdsSys';

poDictionary.Password := 'SuperSecret';

poDictionary.LoginPrompt := False;

 

poDictionary.IsConnected := True;

 

poDictionary.CreateDDLink( 'LinkA',

'Archive.add',

'',

'',

[loAuthenticateActiveUser, loGlobal] );

 

poDictionary.ModifyLink( 'LinkA',

'Archive.add',

'AdsSys',

'BeerIsGood',

[] );

 

finally

poDictionary.IsConnected := False;

 

FreeAndNil( poDictionary );

end;

 

end;

See Also

[CreateDDLink](ade_createddlink_tadsdictionary.md)

[DropDDLink](ade_dropddlink_tadsdictionary.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.md)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.md)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.md)
