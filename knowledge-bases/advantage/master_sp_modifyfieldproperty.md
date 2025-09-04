sp\_ModifyFieldProperty




Advantage Database Server 12  

sp\_ModifyFieldProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyFieldProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyFieldProperty Advantage SQL Engine master\_Sp\_modifyfieldproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyFieldProperty / Dear Support Staff, |  |
| sp\_ModifyFieldProperty  Advantage SQL Engine |  |  |  |  |

Sets a property of a field of a database table in the data dictionary.

Syntax

sp\_ModifyFieldProperty(

TableName,CHARACTER,200,

FieldName,CHARACTER,200,

Property,CHARACTER,200,

Value,MEMO,

ValidationOption,CHARACTER,25,

FailTable,CHARACTER,515 )

 

sp\_ModifyFieldProperty(

TableName,CHARACTER,200,

FieldName,CHARACTER,200,

Property,CHARACTER,200,

Value,NMEMO,

ValidationOption,CHARACTER,25,

FailTable,CHARACTER,515 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of the table with the specified field. |
| FieldName (I) | Name of the field in the table to set the property. |
| Property (I) | Name of a field property to set. See Remarks for possible values. |
| Value (I) | Value to be stored in the data dictionary in string format. |
| ValidationOption (I) | If the property specified by is a constraint on the field, the ValidationOption parameter specifies the type of validation to perform on existing records in the table. This parameter is ignored otherwise. See Remarks for possible values. |
| FailTable (I) | If the property to set is a constraint on the field, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are to be deleted from the table due to the new constraint. If this parameter is NULL, the records will be saved in a table named "savefail.adt" in the same directory as the table. If a path is specified, it must be a fully qualified UNC path or a relative path from the data dictionary. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in Property is not a valid field property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | Either the table specified by TableName cannot be located in the data dictionary or the field specified by FieldName is not part of the table. |

Remarks

sp\_ModifyFieldProperty sets one property of the specified field in the table. The new property overwrites the existing property in the data dictionary. The following are the valid values of Property.

|  |  |
| --- | --- |
| Property | Description |
| COMMENT | Changes the field description. |
| FIELD\_DEFAULT\_VALUE | The system procedure sets the fields default value that will be stored in the field when a new record is added into the table. The value passed in is expected to evaluate to the proper data type for the field. To remove a previous setting of this property, use NULL as the value. If this property is not set, the default field value for ADT tables is NULL and the default field value for DBF table is empty (all spaces).  Note: BLOB/Binary fields can only have a default field value of NULL. |
| FIELD\_CAN\_BE\_NULL | The system procedure sets the fields "Can NULL" flag. The value is expected to be True if a NULL value is allowed for the field or False if a NULL is not allowed for the field. By default, a NULL value is allowed. When setting the "Can NULL" flag to False, existing records in the table can be validated using the ValidationOption parameter. |
| FIELD\_MIN\_VALUE | The system procedure sets the minimum allowed value of the specified field in the table. The value is expected to evaluate to the proper data type for the field. To remove a previous setting of this property, use NULL as the value. When setting a minimum required field value, existing records in the table can be validated using the ValidationOption parameter. |
| FIELD\_MAX\_VALUE | The system procedure sets the maximum allowed valued of the specified field in the table. The value is expected to evaluate to the proper data type for the field. To remove a previous setting of this property, use NULL as the value. When setting a maximum allowed field value, existing records in the table can be validated using the ValidationOption parameter. |
| FIELD\_VALIDATION\_MSG | The system procedure sets the error message that will be returned if a new field value or a modified field value failed to meet the constraints of the field. The constraints of the field include whether the field can have a NULL value, the required minimum value of the field, and the maximum allowed value of the field. |

The ValidateOption parameter is used when the property is FIELD\_CAN\_BE\_NULL, FIELD\_MIN\_VALUE, or FIELD\_MAX\_VALUE. It specifies how the existing records in the table should be validated against the new constraint. New records added to the table will always be validated against the field level constraint. Modified existing records will always be validated against the field level constraint also. The following are the allowed values for ValidationOption.

|  |  |
| --- | --- |
| ValidationOption | Description |
| NO\_VALIDATE | Do not perform any validation on existing records in the table. CAUTION: Using this option can logically corrupt tables and is strongly discouraged. If an index is available on the field in question, validating constraints is a quick operation and should always be performed. |
| APPEND\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table and appended to the table specified by FailTable or to the default fail table if FailTable is NULL. |
| WRITE\_FAIL | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| NO\_SAVE | Perform validation on existing records in the table. Records failing to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. The table will not be modified. If the error is returned, the new constraint will not be set. |

Example 1

After making a connection to the database, change the property of field "Zip Code" in the "Customer Information" table so that it will never have a NULL value in the field. Abort the setting if there are existing records in the table with a NULL value in the "Zip Code" field.

EXECUTE PROCEDURE sp\_ModifyFieldProperty(

Customer Information,

Zip Code,

FIELD\_CAN\_BE\_NULL,

FALSE,

RETURN\_ERROR,

NULL );

Example 2

After making a connection to the database, sets the maximum allowed value of "Credit Limit" field in the "Customer Information". Do not validate existing records.

EXECUTE PROCEDURE sp\_ModifyFieldProperty(

Customer Information,

Zip Code,

FIELD\_MAX\_VALUE,

10000,

NO\_VALIDATE,

NULL );

See Also

[system.columns](master_system_columns.htm)