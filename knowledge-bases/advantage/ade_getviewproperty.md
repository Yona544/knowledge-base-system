GetViewProperty




Advantage Database Server 12  

TAdsDictionary.GetViewProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetViewProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetViewProperty Advantage TDataSet Descendant ade\_Getviewproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetViewProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves one view property into the supplied buffer from the data dictionary.

Syntax

TAdsDictionary.GetViewProperty( strViewName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

|  |  |
| --- | --- |
| strViewName | Name of the view in the database to retrieve the property. |
| usPropertyID | Index of the view property to retrieve. See Remarks for allowed values. |
| pvProperty | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen | On input, it specifies the size of the buffer pointed by pvProperty. On output, it returns the length of property stored in the buffer. |

Remarks

TAdsDictionary.GetViewProperty retrieves one view property of the specified table property from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and usPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the view description in pvProperty. |
| ADS\_DD\_VIEW\_STMT | This will return the SQL that was used to generate the view. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_VIEW\_STMT\_LEN | Retrieves the length of the view SQL statement. Can be used to allocate a buffer before calling AdsDDGetViewProperty with the ADS\_DD\_VIEW\_STMT option. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |

Example

procedure GetViewPropertyExample;

var

oAdsDictionary : TAdsDictionary;

oViewNames : TStringList;

pucProperty : array [ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

usLength : UNSIGNED16;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

{\* now we are going to add a couple tables from our sample tables \*}

oAdsDictionary.AddTable( 'offices',

'd:\demo\offices.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddTable( 'salesreps',

'd:\demo\salesreps.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddView( 'View1',

'',

'select \* from offices' );

 

oAdsDictionary.AddView( 'View2',

'',

'select \* from salesreps' );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetViewProperty( 'View1',

ADS\_DD\_VIEW\_STMT,

@pucProperty,

usLength );

 

{\* now we are going to make the call to getviewnames \*}

oViewNames := TStringList.Create;

oAdsDictionary.Getviewnames( oViewNames );

 

oAdsDictionary.RemoveView( 'View1' );

oAdsDictionary.RemoveView( 'View2' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oViewNames.Free;

 

 

 

end;

See Also

[SetTableProperty](ade_settableproperty.htm)

[SetFieldProperty](ade_setfieldproperty.htm)

[GetFieldProperty](ade_getfieldproperty.htm)