RemoveRI




Advantage Database Server 12  

TAdsDictionary.RemoveRI

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.RemoveRI  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.RemoveRI Advantage TDataSet Descendant ade\_Removeri Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.RemoveRI  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Removes a RI constraint from the data dictionary.

Syntax

TAdsDictionary.RemoveRI( strRIName : string );

Parameters

|  |  |
| --- | --- |
| strRIName | Name of the RI identifying the RI object in the data dictionary. |

Remarks

TAdsDictionary.RemoveRI will remove a RI constraint from the data dictionary.

ALTER permissions are required on both related tables to remove a relation from a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function requires exclusive open of the table. Error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveRIExample;

var

oAdsDictionary : TAdsDictionary;

aucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

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

 

{\* now we need to set the primary indexes for offices \*}

 

usLength := 7;

oAdsDictionary.SetTableProperty( 'offices',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'office' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

{\* now we need to set the primary indexes for offices \*}

 

usLength := 7;

oAdsDictionary.SetTableProperty( 'offices',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'office' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

 

 

{\* now we create the RI \*}

 

oAdsDictionary.CreateRI( 'NewRI',

'',

'offices',

'office',

'salesreps',

'rep\_office',

ADS\_DD\_RI\_CASCADE,

ADS\_DD\_RI\_CASCADE );

 

 

{\* now we are going to get the parent table property \*}

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetRIProperty( 'NewRI',

ADS\_DD\_RI\_PRIMARY\_TABLE,

@aucProperty,

usLength );

 

 

oAdsDictionary.RemoveRI( 'NewRI' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;

See Also

[CreateRI](ade_createri.htm)