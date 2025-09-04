ModifyLink




Advantage Database Server 12  

TAdsDictionary.ModifyLink

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.ModifyLink  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.ModifyLink Advantage TDataSet Descendant ade\_Modifylink Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

|  |  |
| --- | --- |
| strLinkAlias (I) | Name of the existing global link. |
| strLinkedDDPath (I) | Path to the data dictionary that will be linked to the connection passed in the hDBConn parameter. The path can be either a full UNC path or a relative path based on the connection path of the current connection. |
| strUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| strPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| Options (I) | Set of TAdsLinkOptions specifying the properties of the link.  loAuthenticateActiveUser: Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. This option is off by default so the strUserName and strPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  loPathIsStatic: Specifies whether the relative or full path of the linked data dictionary is stored in the current database. If the loPathIsStatic option is specified, the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the strLinkedDDPath parameter when this option is specified. |

Special Return Codes

|  |  |
| --- | --- |
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

[CreateDDLink](ade_createddlink_tadsdictionary.htm)

[DropDDLink](ade_dropddlink_tadsdictionary.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[RevokePermissions](ade_revokepermissions_tadsdictionary.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.htm)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.htm)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.htm)