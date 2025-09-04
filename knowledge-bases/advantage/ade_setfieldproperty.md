SetFieldProperty




Advantage Database Server 12  

TAdsDictionary.SetFieldProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.SetFieldProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.SetFieldProperty Advantage TDataSet Descendant ade\_Setfieldproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.SetFieldProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Sets a property of a field in a table in the data dictionary.

Syntax

TAdsDictionary.SetFieldProperty( strTableName : string;

strFieldName : string;

usPropertyID : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16;

usValidationOption : UNSIGNED16;

strFailTable : string );

Parameters

|  |  |
| --- | --- |
| strTableName | Name of the table with the specified field. |
| strFieldName | Name of the field in the table to set the property. |
| usPropertyID | Index of a field property to set. See Remarks for possible values. |
| pvProperty | Pointer to the field property to stored in the data dictionary. |
| usPropertyLen | The size of the property pointed at by pvProperty. |
| usValidateOption | If the property specified by usPropertyID is a constraint on the field, the usValidateOption parameter specifies the type of validation to perform on existing records in the table. This parameter is ignored otherwise. See Remarks for possible values. |
| strFailTable (I) | If the property to set is a constraint on the field, and validation is to be performed on existing records in the table, this parameter specifies the name of the file to save the records that are to be deleted from the table due to the new constraint. If this parameter is an empty string, the records will be saved in a table named "savefail.adt" in the same directory as the table. |

Remarks

TAdsDictionary.SetFieldProperty sets one property of the specified field in the table. The new property overwrites the existing property in the data dictionary. Because field information of DBF tables are not maintained in the data dictionary, this function will return an error if the table specified by strTableName is a DBF table. The properties can only be set when the TAdsDictionary is opened by a user with ALTER permissions on the table. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

The following are the valid values of usPropertyID and the expected value in pvProperty.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the field description. The pvProperty is expected to be NULL terminated string. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined table property. If pvProperty is NULL, the user defined table property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage Database Server. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE | The function sets the fields default value will be stored in the field when a new record is added into the table. The property passed in pvProperty is expected to be a NULL terminated expression that evaluates to a proper type for the field. If this property is not set, NULL value is the default field value. To remove a previous setting of this property, use empty string as the pvProperty. |
| ADS\_DD\_FIELD\_CAN\_NULL | The function sets the fields "Can NULL" flag. pvProperty is expected to contain a pointer to a boolean value indicating whether NULL value is allowed for this field in the table. By default, NULL value is allowed. If zero is passed in as the flag, NULL value will not be allowed for the field when updating the table. When setting the "Can NULL" flag to FALSE, existing records in the table can be validated using the usValidateOption parameter. |
| ADS\_DD\_FIELD\_MIN\_VALUE | The function sets the minimum allowed value of the specified field in the table. The pvProperty parameter specifies the minimum value and it is expected to be a NULL terminated expression that evaluates to the proper data type for the field. To remove a previous setting of this property, use empty as the pvProperty. When setting a minimum required field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_MAX\_VALUE | The function sets the maximum allowed valued of the specified field in the table. pvProperty parameter specifies the maximum value and it is expected to be a NULL terminated expression that evaluates to the proper data type for the field. usPropertyLen is the length of the expression including the NULL terminator. To remove a previous setting of this property, use empty string as the pvProperty. When setting a maximum allowed field value, existing records in the table can be validated using the usValidateOption parameter. Note that if a string value is specified, all leading and trailing spaces are removed unless the value is enclosed in quotes. |
| ADS\_DD\_FIELD\_VALIDATION\_MSG | The function sets the error message that will be returned if a new field value or a modified field value failed to meet the constraints of the field. The constraints of the field include whether the field can have NULL value, the required minimum value of the field, and the maximum allowed value of the field. |

The usValidateOption parameter is used when usPropertyID is ADS\_DD\_FIED\_CAN\_NULL, ADS\_DD\_FIELD\_MIN\_VALUE , or ADS\_DD\_FIELD\_MAX\_VALUE. It specifies how the existing records in the table should be validated against the new constraint. New records added to the table will always be validated against the field level constraint. Modified existing records will always be validated against the field level constraint also. The following are the allowed values for usValidateOption.

|  |  |
| --- | --- |
| usValidateOption | Description |
| ADS\_NO\_VALIDATE | Do not perform any validation on existing records in the table. |
| ADS\_VALIDATE\_APPEND\_FAIL | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table and appended to the table specified by strFailTable or to the default fail table if strFailTable is empty string. |
| ADS\_VALIDATE\_WRITE\_FAIL | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table. The fail table will be created to save all records that are removed from the original table. |
| ADS\_VALIDATE\_NO\_SAVE | Perform validation on existing records in the table. Records fail to meet the new constraint will be permanently deleted from the table. The deleted records are not saved and will be lost. |
| ADS\_VALIDATE\_RETURN\_ERROR | Perform validation on existing records in the table. If there are existing records in the table not meeting the new constraint, an error will be returned by the function. Table will not be modified. If the error is returned the new constraint will not be set. |

Example

procedure SetFieldPropertyExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

{\* now we are going to add a couple tables from our sample tables \*}

oAdsDictionary.AddTable( 'salesreps',

'd:\demo\salesreps.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.SetFieldProperty( 'salesreps',

'age',

ADS\_DD\_FIELD\_MIN\_VALUE,

pChar( '31' ),

3,

ADS\_VALIDATE\_WRITE\_FAIL,

'd:\demo\fail.adt' );

 

oAdsDictionary.SetFieldProperty( 'salesreps',

'age',

ADS\_VALIDATE\_APPEND\_FAIL,

pChar( '65' ),

3,

ADS\_VALIDATE\_APPEND\_FAIL,

'd:\demo\fail.adt' );

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

 

 

end;

See Also

[GetFieldProperty](ade_getfieldproperty.htm)

[SetTableProperty](ade_settableproperty.htm)

[GetTableProperty](ade_gettableproperty.htm)