GetFieldProperty




Advantage Database Server 12  

TAdsDictionary.GetFieldProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetFieldProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetFieldProperty Advantage TDataSet Descendant ade\_Getfieldproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetFieldProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves a property of a field in a table property from the data.

Syntax

TAdsDictionary.GetFieldProperty( strTableName : string;

strFieldName : string;

usPropertyID : string;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

|  |  |
| --- | --- |
| strTableName | Name of the table in the database with the specified field. |
| strFieldName | Name of the field in the table with the specified property. |
| usPropertyID | Index of the field property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen | On input, it specifies the size of the buffer pointed by pvProperty. On output, it returns the length of property copied into the buffer. |

Remarks

TAdsDictionary.GetFieldProperty retrieves one field property of the specified table from the data dictionary. Because field level information of DBF tables is not stored in the data dictionary, this function will return an error if the table specified by strTableName is a DBF table. The following are the valid values of usPropertyID and the expected return value in pvProperty and usPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the field description in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined field property in pvProperty. |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE | The function returns the default field value that will be set when a new record is added into the table. The default field value is returned as a NULL terminated string in the pvProperty. If no default field value is defined for the specified field, the function returns AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_FIELD\_CAN\_NULL | The function returns a flag that indicates whether NULL value is allowed for the specified field in the table. The flag is returned as a 2-byte (UNSIGNED16) number in pvProperty. The number is non-zero if NULL value is allowed. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_FIELD\_MIN\_VALUE | The function returns the minimum allowed value of the specified field in the table. The minimum value is returned as a NULL terminated expression in pvProperty. If there is no minimum required value for the specified field, the function returns AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_FIELD\_MAX\_VALUE | The function returns the maximum allowed valued of the specified field in the table. The maximum value is returned as a NULL terminated expression in pvProperty. If the field is not limited by a maximum value, the function returns AE\_PROPERTY\_NOT\_SET error. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_FIELD\_VALIDATION\_MSG | The function returns the error message that will be returned if a new field value or a modified field value failed to meet the constraints of the field. The constraints of the field include whether the field can have NULL value, the required minimum value of the field, and the maximum allowed value of the field. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_FIELD\_LENGTH | The function returns in pvProperty a 2-byte (UNSIGNED16) integer that is the length of the specified field. |
| ADS\_DD\_FIELD\_TYPE | The function returns in pvProperty a 2-byte (UNSIGNED16) integer that is the data type of the specified field. See AdsGetFieldType for information of Advantage field types. |
| ADS\_DD\_FIELD\_DECIMAL | The function returns in pvProperty a 2-byte (UNSIGNED16) integer that is the number of decimals of the specified field. |
| ADS\_DD\_FIELD\_OPTIONS | The function returns in pvProperty a 4 bytes (UNSIGNED32) integer that is a bitmask with various field properties. Currently, the bitmask values include: ADS\_DD\_FIELD\_OPT\_VFP\_BINARY (indicates it is a VFP field created with the NOCPTRANS option), and ADS\_DD\_FIELD\_OPT\_VFP\_NULLABLE (indicates it is a nullable VFP field). |

Example

procedure GetFieldPropertyExample;

var

oAdsDictionary : TAdsDictionary;

usLength : UNSIGNED16;

aucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

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

ADS\_DD\_FIELD\_MAX\_VALUE,

pChar( '65' ),

3,

ADS\_VALIDATE\_APPEND\_FAIL,

'd:\demo\fail.adt' );

 

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetFieldProperty( 'salesreps',

'age',

ADS\_DD\_FIELD\_MIN\_VALUE,

@aucProperty,

usLength );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetFieldProperty( 'salesreps',

'age',

ADS\_DD\_FIELD\_MAX\_VALUE,

@aucProperty,

usLength );

 

 

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[SetFieldProperty](ade_setfieldproperty.htm)

[SetTableProperty](ade_settableproperty.htm)

[GetTableProperty](ade_gettableproperty.htm)