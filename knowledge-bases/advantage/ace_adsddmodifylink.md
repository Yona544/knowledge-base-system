AdsDDModifyLink




Advantage Database Server 12  

AdsDDModifyLink

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDModifyLink  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDModifyLink Advantage Client Engine ace\_Adsddmodifylink Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDModifyLink  Advantage Client Engine |  |  |  |  |

Modifies an existing global data dictionary link.

Syntax

UNSIGNED32 AdsDDModifyLink( ADSHANDLE hDBConn,

UNSIGNED8 \*pucLinkAlias,

UNSIGNED8 \*pucLinkedDDPath,

UNSIGNED8 \*pucUserName,

UNSIGNED8 \*pucPassword,

UNSIGNED32 ulOptions );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucLinkAlias (I) | Name of the existing global link. |
| pucLinkedDDPath (I) | Path to the data dictionary that will be linked to the connection passed in the hDBConn parameter. The path can be either a full UNC path or a relative path based on the connection path of hDBConn. |
| pucUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the ADS\_LINK\_AUTH\_ACTIVE\_USER option is specified in the ulOptions parameter. |
| pucPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the ADS\_LINK\_AUTH\_ACTIVE\_USER option is specified in the ulOptions parameter. |
| ulOptions (I) | Bit field for defining options for this link. The options can be ORed together. For example, ADS\_LINK\_PATH\_IS\_STATIC | ADS\_LINK\_AUTH\_ACTIVE\_USER. The options are:  ADS\_DEFAULT: If no options are needed, this value (0) can be used.  ADS\_LINK\_AUTH\_ACTIVE\_USER: Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. This option is off by default so the pucUserName and pucPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  ADS\_LINK\_PATH\_IS\_STATIC: Specifies whether the relative or full path of the linked data dictionary is stored in the current database. If the ADS\_LINK\_PATH\_IS\_STATIC option is specified, the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the pucLinkedDDPath parameter when this option is specified. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the global link with the given alias cannot be found. |

Remarks

This function modifies an existing global link to another data dictionary on the current connection. The primary benefit to using this API over deleting and re-creating the link is that it maintains existing permissions on the link object. This API can only be used to modify global links; local link objects cannot be modified.

ALTER permissions on the link are required to modify data dictionary link properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

See Also

[AdsDDCreateLink](ace_adsddcreatelink.htm)

[AdsDDDropLink](ace_adsdddroplink.htm)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.htm)

[AdsGetNumActiveLinks](ace_adsgetnumactivelinks.htm)

[AdsGetActiveLinkInfo](ace_adsgetactivelinkinfo.htm)

[sp\_ModifyLink](master_sp_modifylink.htm)