---
title: Ace Adsddsetfieldproperty
slug: ace_adsddsetfieldproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetfieldproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3b589744bf001b678a96959481537eb4e74f4e5f
---

# Ace Adsddsetfieldproperty

AdsDDSetFieldProperty

AdsDDSetFieldProperty

Advantage Client Engine

| AdsDDSetFieldProperty  Advantage Client Engine |  |  |  |  |

Sets a property of a field of a database table in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetFieldProperty( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucFieldName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen,

UNSIGNED16 usValidateOption,

UNSIGNED8 \*pucFailTable );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table with the specified field. |
| pucFieldName (I) | Name of the field in the table to set the property. |
| usPropertyID (I) | Index of a field property to set. See Remarks for possible values. |
| pvProperty (I) | Pointer to the field property to be stored in the data dictionary. |
| usPropertyLen (I) | Length of the property pointed to by the pvProperty parameter. |
| usValidateOption (I) | If the property specified by usPropertyID is a constraint on the field, the usValidateOption parameter specifies the type of validation to perform on existing records in the table. This parameter is ignored otherwise. See Remarks for possible values. |
| pucFailTable (I) | If the property to set is a constraint on the field, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are to be deleted from the table due to the new constraint. If this parameter is NULL, the records will be saved in a table named "savefail.adt" in the same directory as the table. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid field property index, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | Either the table specified by pucTableName cannot be located in the data dictionary or the field specified by pucFieldName is not part of the table. |

Remarks

AdsDDSetFieldProperty sets one property of the specified field in the table. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the table are required to modify a data dictionary tables field properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the field description. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined field property. If pvProperty is NULL, the user defined field property is removed. User defined property is set, read, and interpreted by the application. It is not used by Advantage. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE | The function sets the fields default value that will be stored in the field when a new record is added into the table. The property passed in pvProperty is expected to be a NULL terminated expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. If this property is not set, the default field value for ADT tables is NULL and the default field value for DBF table is empty (all spaces).  Note: BLOB/Binary fields can only have a default field value of NULL. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE\_W | The function sets the fields default value that will be stored in the field when a new record is added into the table. The property passed in pvProperty is expected to be a NULL terminated UTF-16 expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. If this property is not set, the default field value for ADT tables is NULL and the default field value for DBF table is empty (all spaces).  Note: BLOB/Binary fields can only have a default field value of NULL. |
| ADS\_DD\_FIELD\_CAN\_NULL | The function sets the fields "Can NULL" flag. pvProperty is expected to contain a 2 byte (UNSIGNED16) value indicating whether a NULL value is allowed for this field in the table. By default, a NULL value is allowed. If zero is passed in as the flag, a NULL value will not be allowed for the field when updating the table. When setting the "Can NULL" flag to False, existing records in the table can be validated using the usValidateOption parameter. |
| ADS\_DD\_FIELD\_MIN\_VALUE | The function sets the minimum allowed value of the specified field in the table. The pvProperty parameter specifies the minimum value and it is expected to be a NULL terminated expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. When setting a minimum required field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_MIN\_VALUE\_W | The function sets the minimum allowed value of the specified field in the table. The pvProperty parameter specifies the minimum value and it is expected to be a NULL terminated UTF-16 expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. When setting a minimum required field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_MAX\_VALUE | The function sets the maximum allowed valued of the specified field in the table. pvProperty parameter specifies the maximum value and it is expected to be a NULL terminated expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. When setting a maximum allowed field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_MAX\_VALUE\_W | The function sets the maximum allowed valued of the specified field in the table. pvProperty parameter specifies the maximum value and it is expected to be a NULL terminated UTF-16 expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use NULL as the pvProperty. When setting a maximum allowed field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_VALIDATION\_MSG | The function sets the error message that will be returned if a new field value or a modified field value failed to meet the constraints of the field. The constraints of the field include whether the field can have a NULL value, the required minimum value of the field, and the maximum allowed value of the field. |

The usValidateOption parameter is used when usPropertyID is ADS\_DD\_FIELD\_CAN\_NULL, ADS\_DD\_FIELD\_MIN\_VALUE, or ADS\_DD\_FIELD\_MAX\_VALUE. It specifies how the existing records in the table should be validated against the new constraint. New records added to the table will always be validated against the field level constraint. Modified existing records will always be validated against the field level constraint also. The following are the allowed values for usValidateOption.

| usValidateOption | Description |
| ADS\_NO\_VALIDATE | Do not perform any validation on existing records in the table. CAUTION: Using this option can logically corrupt tables and is strongly discouraged. If an index is available on the field in question, validating constraints is a quick operation and should always be performed. |
| ADS\_VALIDATE\_APPEND\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table and appended to the table specified by pucFailTable or to the default fail table if pucFailTable is NULL. |
| ADS\_VALIDATE\_WRITE\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| ADS\_VALIDATE\_NO\_SAVE | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| ADS\_VALIDATE\_RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. The table will not be modified. If the error is returned, the new constraint will not be set. |

Example 1

After making a connection to the database, change the property of field "Zip Code" in the "Customer Information" table so that it will never have a NULL value in the field. Abort the setting if there are existing records in the table with a NULL value in the "Zip Code" field.

AdsDDOpen( "n:\\MyData\\myData.ADD", NULL, &hDD );

usFieldCanNULL = FALSE;

AdsDDSetFieldProperty( hDD, "Customer Information", "Zip Code",

ADS\_DD\_FIELD\_CAN\_NULL, &usFieldCanNULL,

(UNSIGNED16)( sizeof( usFieldCanNULL ) ),

ADS\_VALIDATE\_RETURN\_ERROR, NULL );

AdsDDClose( hDD );

Example 2

After making a connection to the database, sets the maximum allowed value of "Credit Limit" field in the "Customer Information". Do not validate existing records.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

sprintf( acMaxValue, "10000" );

AdsDDSetFieldProperty( hDD, "Customer Information", "Credit Limit",

ADS\_DD\_FIELD\_MAX\_VALUE, acMaxValue,

(UNSIGNED16)( strlen( acMaxValue ) + 1 ),

ADS\_NO\_VALIDATE, NULL );

AdsDisconnect( hDD );

See Also

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.md)

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[sp\_ModifyFieldProperty](master_sp_modifyfieldproperty.md)
