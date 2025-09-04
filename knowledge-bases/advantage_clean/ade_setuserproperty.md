---
title: Ade Setuserproperty
slug: ade_setuserproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_setuserproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6b4b2936a296aed20cf58ff3b1807b381fc2da6f
---

# Ade Setuserproperty

SetUserProperty

TAdsDictionary.SetUserProperty

Advantage TDataSet Descendant

| TAdsDictionary.SetUserProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Sets one property associated with a database user in the data dictionary.

Syntax

procedure SetUserProperty( strUserName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16 ); virtual;

Parameters

| strUserName (I) | Name of the database user object to set the associated property. |
| usPropertyID (I) | Index of a database user property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Remarks

SetUserProperty sets one user property associated with the specified user. The new property overwrites the existing property in the data dictionary.

ALTER permissions on the user are required to modify data dictionary user properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the user. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the user description is removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined user property. If pvProperty is NULL, the user defined user property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server or the Advantage Local Server. |
| ADS\_DD\_USER\_PASSWORD | Sets a new password for this user. The user password is used by the Advantage Database Server or the Advantage Local Server to authenticate a user when he makes a connection to the database. See AdsConnect60 for more information on database connections. pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. To allow the user to connect without a password, specify NULL or an empty string as pvProperty. The maximum length of the password not including the NULL terminator is 20 characters. If usPropertyLen is longer than 21, the first 20 character will be used as the password. ADS\_DD\_USER\_PASSWORD can be used to set the administrator password by specifying the ADSSYS as the user name. |
| ADS\_DD\_ENABLE\_INTERNET | This property enables/disables the Internet access for the user. If it is disabled, the user will be allowed to connect from the Internet. pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. For more information see [Advantage Internet Server](master_advantage_internet_server.md). |
| ADS\_DD\_LOGINS\_DISABLED | This property enables/disables the database login for the user. If it is enabled, the user will not be allowed to login to the database. The default setting is disabled (the user is allowed to login). pvProperty is expected to be a pointer to a 2-byte (UNSIGNED16) integer. usPropertyLen is expected to be 2. Expected values are True and False. |

Note When the database is created, it is default to allow anonymous user to make database connection with no user name and no password. Setting the ADS\_DD\_LOG\_IN\_REQUIRED database property to True will disable the anonymous user connections and improve the database security. See SetDatabaseProperty for more information.

Example

procedure SetUserPropertyExample;

var

oAdsDictionary : TAdsDictionary;

oGroupNameList : TStringList;

oUserNameList : TStringList;

oUsersInGroupList : TStringList;

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

 

oAdsDictionary.SetUserGroupProperty( 'NewGroup',

ADS\_DD\_COMMENT,

pChar( 'A better comment.' ),

18 );

 

oAdsDictionary.AddTable( 'customers',

'd:\demo\customers.adt',

'',

'New Table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.SetUserProperty( 'NewUser',

ADS\_DD\_USER\_PASSWORD,

pChar( 'foobar' ),

7 );

 

oAdsDictionary.SetObjectAccessRights( 'customers',

'NewUser',

'RW' );

 

oAdsDictionary.AddUserToGroup( 'NewGroup',

'NewUser' );

 

oUserNameList := TStringList.Create;

oAdsDictionary.GetUserNames( oUserNameList );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetUserProperty( 'NewUser',

ADS\_DD\_TABLES\_RIGHTS,

@pucProperty,

usLength );

 

oUsersInGroupList := TStringList.Create;

oAdsDictionary.GetUsersFromGroup( 'NewGroup', oUsersInGroupList );

 

 

oAdsDictionary.RemoveUserFromGroup( 'NewGroup', 'NewUser' );

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.RemoveUser( 'NewUser' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;
