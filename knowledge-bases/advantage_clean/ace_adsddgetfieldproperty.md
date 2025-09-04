---
title: Ace Adsddgetfieldproperty
slug: ace_adsddgetfieldproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetfieldproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: bb14730b2b1e535ab02a0e799bee5309452389a4
---

# Ace Adsddgetfieldproperty

AdsDDGetFieldProperty

AdsDDGetFieldProperty

Advantage Client Engine

| AdsDDGetFieldProperty  Advantage Client Engine |  |  |  |  |

Retrieves a property of a field of a database table from the data dictionary.

Syntax

UNSIGNED32 AdsDDGetFieldProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucFieldName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table in the database with the specified field. |
| pucFieldName (I) | Name of the field in the table with the specified property. |
| usPropertyID (I) | Index of the field property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| \*pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed by pvProperty. On output, returns the length of property copied into the buffer. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid field property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

AdsDDGetFieldProperty retrieves one field property of the specified table from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the field description in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined field property in pvProperty. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE | The function returns the default field value that will be set when a new record is added into the table. The default field value is returned as a NULL terminated string in the pvProperty. If no default field value is defined for the specified field, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data encoded as ANSI text. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE\_W | The function returns the default field value that will be set when a new record is added into the table. The default field value is returned as a NULL terminated string in the pvProperty. If no default field value is defined for the specified field, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data encoded as UTF-16 text. |
| ADS\_DD\_FIELD\_CAN\_NULL | The function returns a flag that indicates whether a NULL value is allowed for the specified field in the table. The flag is returned as a 2-byte (UNSIGNED16) number in pvProperty. The number is non-zero if a NULL value is allowed. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_FIELD\_MIN\_VALUE | The function returns the minimum allowed value of the specified field in the table. The minimum value is returned as a NULL terminated expression in pvProperty. If there is no minimum required value for the specified field, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data encoded as ANSI text. |
| ADS\_DD\_FIELD\_MIN\_VALUE\_W | The function returns the minimum allowed value of the specified field in the table. The minimum value is returned as a NULL terminated expression in pvProperty. If there is no minimum required value for the specified field, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data encoded UTF-16 text. |
| ADS\_DD\_FIELD\_MAX\_VALUE | The function returns the maximum allowed valued of the specified field in the table. The maximum value is returned as a NULL terminated expression in pvProperty. If the field is not limited by a maximum value, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as ANSI encoded text. |
| ADS\_DD\_FIELD\_MAX\_VALUE\_W | The function returns the maximum allowed valued of the specified field in the table. The maximum value is returned as a NULL terminated expression in pvProperty. If the field is not limited by a maximum value, the function returns an AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as UTF-16 encoded text. |
| ADS\_DD\_FIELD\_VALIDATION\_MSG | The function returns the error message that will be returned if a new field value or a modified field value failed to meet the constraints of the field. The constraints of the field include whether the field can have a NULL value, the required minimum value of the field, and the maximum allowed value of the field. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_FIELD\_LENGTH | The function returns in pvProperty a 2 byte (UNSIGNED16) integer that is the length of the specified field. |
| ADS\_DD\_FIELD\_TYPE | The function returns in pvProperty a 2 byte (UNSIGNED16) integer that is the data type of the specified field. See [AdsGetFieldType](ace_adsgetfieldtype.md) for information of Advantage field types. |
| ADS\_DD\_FIELD\_DECIMAL | The function returns in pvProperty a 2 byte (UNSIGNED16) integer that is the number of decimals the specified field. |
| ADS\_DD\_FIELD\_OPTIONS | The function returns in pvProperty a 4 bytes (UNSIGNED32) integer that is a bitmask with various field properties. Currently, the bitmask values include: ADS\_DD\_FIELD\_OPT\_VFP\_BINARY (indicates it is a VFP field created with the NOCPTRANS option), and ADS\_DD\_FIELD\_OPT\_VFP\_NULLABLE (indicates it is a nullable VFP field). |

Example 1

After making a connection to the database, find out whether the "Company Name" field in the "Customer Information" table can have a NULL value.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( usFieldCanNull );

AdsDDGetFieldProperty( hDD, "Customer Information", "Company Name", ADS\_DD\_FIELD\_CAN\_NULL,

&usFieldCanNull, &usBuffSize ) ;

AdsDisconnect( hDD );

Example 2

After making a database connection as an anonymous user, retrieve the default field value of the "Zip Code" field in the "Customer Information" table.

AdsConnect60( "n:\\MyData\\MyData.ADD", ADS\_REMOTE\_SERVER, NULL, NULL, ADS\_DEFAULT,

&hConn ));

usBufferSize = (UNSIGNED16)sizeof( acDefaultZipCode );

AdsDDGetFieldProperty( hConn, "Customer Information", "Zip Code", ADS\_DD\_FIELD\_DEFAULT\_VALUE,

acDefaultZipCode, &usBuffSize ) ;

AdsDisconnect( hConn );

See Also

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.md)

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[AdsConnect60](ace_adsconnect60.md)

[system.columns](master_system_columns.md)
