CreateDDLink




Advantage Database Server 12  

TAdsConnection.CreateDDLink

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.CreateDDLink  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.CreateDDLink Advantage TDataSet Descendant ade\_Createddlink\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.CreateDDLink  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Creates a link to another data dictionary from the current [database connection](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)), optionally making the link a global link that is available to all users connected to the database.

Syntax

procedure TAdsConection.CreateDDLink( strLinkAlias : string;

strLinkedDDPath : string;

strUserName : string;

strPassword : string;

Options : TAdsLinkOptions );

 

TAdsLinkOption = ( loGlobal, loAuthenticateActiveUser, loPathIsStatic );

TAdsLinkOptions = set of TAdsLinkOption;

Parameters

|  |  |
| --- | --- |
| strLinkAlias (I) | Name of the link to create. This name is used in SQL statements to reference the tables associated with the linked data dictionary. |
| strLinkedDDPath (I) | Path to the data dictionary that will be linked to the connection passed in the current connection. The path can be either a full UNC path or a relative path based on the connection path of the current connection. |
| strUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| strPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the loAuthenticateActiveUser option is specified in the Options parameter. |
| Options (I) | Set of TAdsLinkOption specifying the properties of the link.  loGlobal: Specifies the link alias as available to all users connecting to this data dictionary. All information needed to re-create this link is stored in the data dictionary. By default, this option is turned off, and the link created is local to the current connection.  loAuthenticateActiveUser: Specifies that the user name and password of the current connection is used for authenticating to the linked data dictionary as well. This option is off by default so the strUserName and strPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  loPathIsStatic: This option can be specified in conjunction with the loGlobal option. It determines whether the relative or full path of the linked data dictionary is stored in the current database. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | This error will be returned if a local or global link with an identical alias already exists on the current connection. If creating a global link, this error will be returned if the link name is already used for other objects, such as tables, views or stored procedures, in the database. |

Remarks

This function creates a named link to another data dictionary on the current connection. The name can then be used in SQL statements to reference tables in the linked data dictionary. The permissions to the tables in the linked data dictionary are determined by the user name that is used to authenticate into the linked data dictionary.

If the link alias is made global, the link alias is available to all authorized users of the database. Access to the link can be controlled by granting or revoking user or group permissions to the link alias.

CREATE LINK permissions are required to create a new global link in the data dictionary. Non-global (local) links require no permissions to be created. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After connecting to the master data dictionary, a temporary link is created to the archive data dictionary, and the date of the last archive is updated.

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

 

{\* Create a link to the Archive Data Dictionary \*}

oConnection.CreateDDLink( 'LinkB',

'Archive.add',

'',

'',

[loAuthenticateActiveUser] );

 

{\* Update the archive date in the control table. \*}

oQuery.DatabaseName := oConnection.Name;

 

oQuery.SQL.Clear;

oQuery.SQL.Add( 'UPDATE control SET ArchiveDate = ' );

oQuery.SQL.Add( ' ( SELECT MAX( LastDate ) from LinkB.archive ) ' );

 

oQuery.ExecSQL;

 

oConnection.DropDDLink( 'LinkB', False );

 

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

[DropDDLink](ade_dropddlink_tadsconnection.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[RevokePermissions](ade_revokepermissions_tadsdictionary.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)

[GetLinkProperty](ade_getlinkproperty_tadsdictionary.htm)

[GetNumActiveDDLinks](ade_getnumactiveddlinks_tadsconnection.htm)

[GetActiveDDLinkInfo](ade_getactiveddlinkinfo_tadsconnection.htm)