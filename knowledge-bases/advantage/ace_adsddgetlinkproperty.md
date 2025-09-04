AdsDDGetLinkProperty




Advantage Database Server 12  

AdsDDGetLinkProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetLinkProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetLinkProperty Advantage Client Engine ace\_Adsddgetlinkproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetLinkProperty  Advantage Client Engine |  |  |  |  |

Retrieves a particular property of a link object from the data dictionary.

Syntax

UNSIGNED32 AdsDDGetLinkProperty( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucLinkName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucLinkName (I) | Name of the link object in the database. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | The value supplied in usPropertyID is not a valid link property. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by pusPropertyLen. The required buffer length is returned in pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and pusPropertylen. |

Remarks

AdsDDGetLinkProperty retrieves a property of a global (permanent) link object from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and pusPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_LINK\_PATH | The function returns the full path of the linked data dictionary file as a NULL terminated string in pvProperty. The length returned in pusPropertyLen is the length of the paths string including the NULL terminator. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_LINK\_OPTIONS | The function returns the options of the link when it is activated. This property is a 4-byte integer representing the bit field with the options ORed together. pusPropertyLen must be 4 on input when calling this function with this property ID. See [AdsDDCreateLink](ace_adsddcreatelink.htm) for more information on link options. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_LINK\_USERNAME | The function returns the user name that will be used to authenticate to the linked data dictionary when the link is activated. This property is returned as a NULL terminated string. The pusPropertyLen returns the length of the string including the NULL terminator. This property may not be set if the link option specifies that the current users authentication information is to be used for authentication into the linked data dictionary. It also may not be set if an anonymous user is to be used to authenticate into the linked data dictionary. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |

Example

After making a connection to the "MASTER" database, retrieve the information about the link to the "ARCHIVE" database.

UNSIGNED8 aucLinkUserName[ADS\_MAX\_USER\_NAME+1]

UNSIGNED8 aucLinkPath[ADS\_MAX\_PATH+1];

UNSIGNED16 usBuffLen;

UNSIGNED32 ulLinkOptions;

UNSIGNED32 ulRetVal;

ADSHANDLE hAdminConn;

 

 

ulRetVal = AdsConnect60( "\\\\MyServer\\MyShare\\Data\\Master.ADD",

"ADSSYS", "SysPass", ADS\_DEFAULT, &hAdminConn );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

// Get the link options

usBuffLen = sizeof( ulLinkOptions );

ulRetVal = AdsDDGetLinkProperty( hAdminConn, "ARCHIVE", ADS\_DD\_LINK\_OPTIONS,

&ulLinkOptions, &usBuffLen );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

 

// Get the link user name

usBuffLen = sizeof( aucLinkUserName );

ulRetVal = AdsDDGetLinkProperty( hAdminConn, "ARCHIVE", ADS\_DD\_LINK\_USERNAME,

aucLinkUserName, &usBuffLen );

if ( ulRetVal = AE\_PROPERTY\_NOT\_SET )

aucLinkUserName[0] = 0;

else if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

// Get the link path

usBuffLen = sizeof(aucLinkPath);

ulRetVal = AdsDDGetLinkProperty( hAdminConn, "ARCHIVE", ADS\_DD\_LINK\_PATH,

aucLinkPath, &usBuffLen );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

// disconnect

ulRetVal = AdsDisconnect( hAdminConn );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

See Also

[AdsDDCreateLink](ace_adsddcreatelink.htm)

[AdsDDDropLink](ace_adsdddroplink.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[system.links](master_system_links.htm)