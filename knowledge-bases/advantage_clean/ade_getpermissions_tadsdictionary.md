---
title: Ade Getpermissions Tadsdictionary
slug: ade_getpermissions_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getpermissions_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: abf03d870c238b87ff35277db52fe766ca9c4b6f
---

# Ade Getpermissions Tadsdictionary

GetPermissions

TAdsDictionary.GetPermissions

Advantage TDataSet Descendant

| TAdsDictionary.GetPermissions  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Returns the set of permissions granted to a users or a user groups for a database object.

Syntax

function TAdsDictionary.GetPermissions( strGrantee : string;

usObjectType : UNSIGNED16;

strObjectName : string;

strParentName : string;

bReturnInherited : boolean ) : TAdsPermissionTypes;

Parameters

| strGrantee (I) | Name of a user or a user group for whom the permissions have been granted. |
| usObjectType (I) | Type of the database object that is specified by the strObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_LINK\_OBJECT. |
| strObjectName (I) | Name of the database object to retrieve the granted permissions for. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure or a link alias. |
| strParentName (I) | Name of the database object that is the parent or owner of the object specified by strObjectName. If usObjectType is ADS\_DD\_COLUMN\_OBJECT, this parameter specifies the name of the database table that owns the column specified by the strObjectName parameter. For other object types, the parameter can be empty and it is ignored. |
| bReturnInherited (I) | TRUE or FALSE. If TRUE and strGrantee specifies a user in the database, the function will return the users effective permission to the object, i.e. the users permissions plus any permissions the user inherits from user groups that the user belongs to. If FALSE, only the permissions that are specifically granted to the user or the user group are returned. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The name specified by the strObjectName, strParentName or strGrantee could not be found in the database. |

Remarks

GetPermissions returns a set of permissions granted to a user or a user group on a specific object in the database. The possible values contained in the returned set are ptRead, ptUpdate, ptExecute, ptInherit, ptInsert, ptDelete, and ptLinkAccess. See [GrantPermissions](ade_grantpermissions_tadsdictionary.md) for more information on the types of permissions that can be granted to users and user groups.

Note The permissions properties can only be retrieved by a user with administrative permissions for the specified object. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Example

procedure CheckPermissions;

var

oAdsDictionary : TAdsDictionary;

Permissions : TAdsPermissions;

begin

 

{\* Create the dictionary component and connect to a dictionary. \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

oAdsDictionary.ConnectPath :='n:\MyData\myData.ADD';

oAdsDictionary.UserName := 'ADSSYS';

oAdsDictionary.LoginPrompt := False;

 

oAdsDictionary.IsConnected := True;

 

{\* Retrieve the effective permissions for user rsmith on the 'employees' table. \*}

Permissions := oAdsDictionary.GetPermissions( 'rsmith',

ADS\_DD\_TABLE\_OBJECT,

'Employees',

'',

True );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[AddUser](ade_adduser.md)

[CreateUserGroup](ade_createusergroup.md)

[AddUserToGroup](ade_addusertogroup.md)

[RemoveUserFromGroup](ade_removeuserfromgroup.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[GetPermissions](ade_getpermissions_tadsdictionary.md)
