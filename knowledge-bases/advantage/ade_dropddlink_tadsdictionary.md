DropDDLink




Advantage Database Server 12  

TAdsDictionary.DropDDLink

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.DropDDLink  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.DropDDLink Advantage TDataSet Descendant ade\_Dropddlink\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.DropDDLink  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Removes either a local link or a global link from the current connection.

Syntax

procedure TAdsDictionary.DropDDLink( strLinkedDD : string;

bDropGlobal : boolean);

Parameters

|  |  |
| --- | --- |
| strLinkedDD (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| bDropGlobal (I) | True to remove the global link alias from the data dictionary. If this parameter is True, the strLinkedDD parameter must specify the link alias in the data dictionary. |

Special Return Codes

|  |  |
| --- | --- |
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

[CreateDDLink](ade_createddlink_tadsdictionary.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[RevokePermissions](ade_revokepermissions_tadsdictionary.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.htm)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.htm)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.htm)