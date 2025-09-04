---
title: Ade Getlinkproperty Tadsdictionary
slug: ade_getlinkproperty_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getlinkproperty_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b271fb429cd963e33e88b0d233ab87f4cb62dce8
---

# Ade Getlinkproperty Tadsdictionary

GetLinkProperty

TAdsDictionary.GetLinkProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetLinkProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves one link property into the supplied buffer from the data dictionary.

Syntax

procedure TAdsDictionary.GetLinkProperty( strLinkname : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16);

Parameters

| strLinkName (I) | Name of the link object in the database. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Remarks

GetLinkProperty retrieves a property of a global (permanent) link object from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and usPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_LINK\_PATH | The function returns the full path of the linked data dictionary file as a NULL terminated string in pvProperty. The length returned in usPropertyLen is the length of the paths string including the NULL terminator. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_LINK\_OPTIONS | The function returns the options of the link when it is activated. This property is a 4-byte integer representing the bit field with the options ORed together. \*pusPropertyLen must be 4 on input when calling this function with this property ID. See [CreateDDLink](ade_createddlink_tadsdictionary.md) for more information on link options. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_LINK\_USERNAME | The function returns the user name that will be used to authenticate to the linked data dictionary when the link is activated. This property is returned as a NULL terminated string. The usPropertyLen returns the length of the string including the NULL terminator. This property may not be set if the link options specifies that the current users authentication information is to be used for authentication into the linked data dictionary. It also may not be set if an anonymous user is to be used to authenticate into the linked data dictionary. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |

Example

After making an ADSSYS connection to the "MASTER" database, retrieve the link path to the "ARCHIVE" database.

procedure GetLinkPropertyExample;

var

oDictionary : TAdsDictionary;

pucProperty : array [ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

usLength : UNSIGNED16;

 

begin

 

 

oDictionary := TAdsDictionary.Create( nil );

 

oDictionary.ConnectPath := 'n:\MyData\Master.add';

oDictionary.AdsServerTypes := [stADS\_REMOTE];

oDictionary.UserName := 'AdsSys';

oDictionary.Password := 'SuperSecret';

oDictionary.LoginPrompt := False;

 

oDictionary.IsConnected := True;

 

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

 

oDictionary.GetLinkProperty( 'LinkA',

ADS\_DD\_LINK\_PATH,

@pucProperty,

usLength );

 

oDictionary.IsConnected := FALSE;

 

oDictionary.Free;

 

end;

See Also

[CreateDDLink](ade_createddlink_tadsdictionary.md)

[DropDDLink](ade_dropddlink_tadsdictionary.md)

[GrantPermissions](ade_grantpermissions_tadsdictionary.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)
