---
title: Ade Getusergroupproperty
slug: ade_getusergroupproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getusergroupproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8bdba5c29759f479ba8cfcba93c6563fa70e09c4
---

# Ade Getusergroupproperty

GetUserGroupProperty

TAdsDictionary.GetUserGroupProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetUserGroupProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure GetUserGroupProperty( strGroupName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 ); virtual;

Parameters

| strGroupName (I) | Name of the database user group object to retrieve the associated property. |
| usPropertyID (I) | Index of a database user group property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen (I/O) | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property stored in the buffer. |

Remarks

GetUserGroupProperty retrieves one property associated with the specified user group. User group properties are only available to users that belong to the specified group or to users with administrative permissions for the group. When connected as the administrator (ADSSYS user account), properties from any user groups can be retrieved. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the description of the user group in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | Returns the user defined property for the specified user group. |

Example

procedure GetUserGroupPropertyExample;

var

oAdsDictionary : TAdsDictionary;

oGroupNameList : TStringList;

usLength : UNSIGNED16;

pucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

oAdsDictionary.CreateUserGroup( 'NewGroup',

'The newest group.' );

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.AddUserToGroup( 'NewGroup',

'NewUser' );

 

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

 

oAdsDictionary.GetUserGroupProperty( 'NewGroup',

ADS\_DD\_COMMENT,

@pucProperty,

usLength );

 

 

oGroupNameList := TStringList.Create;

oAdsDictionary.GetGroupNames( oGroupNameList );

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[CreateUserGroup](ade_createusergroup.md)

[AddUserToGroup](ade_addusertogroup.md)

[GetGroupNames](ade_getgroupnames.md)
