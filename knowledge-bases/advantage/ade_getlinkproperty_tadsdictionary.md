GetLinkProperty




Advantage Database Server 12  

TAdsDictionary.GetLinkProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetLinkProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetLinkProperty Advantage TDataSet Descendant ade\_Getlinkproperty\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetLinkProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves one link property into the supplied buffer from the data dictionary.

Syntax

procedure TAdsDictionary.GetLinkProperty( strLinkname : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16);

Parameters

|  |  |
| --- | --- |
| strLinkName (I) | Name of the link object in the database. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Remarks

GetLinkProperty retrieves a property of a global (permanent) link object from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and usPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_LINK\_PATH | The function returns the full path of the linked data dictionary file as a NULL terminated string in pvProperty. The length returned in usPropertyLen is the length of the paths string including the NULL terminator. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
| ADS\_DD\_LINK\_OPTIONS | The function returns the options of the link when it is activated. This property is a 4-byte integer representing the bit field with the options ORed together. \*pusPropertyLen must be 4 on input when calling this function with this property ID. See [CreateDDLink](ade_createddlink_tadsdictionary.htm) for more information on link options. This property can only be retrieved by users with administrative permissions. See Advantage Data Dictionary User Permissions for more information. |
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

[CreateDDLink](ade_createddlink_tadsdictionary.htm)

[DropDDLink](ade_dropddlink_tadsdictionary.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[RevokePermissions](ade_revokepermissions_tadsdictionary.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)