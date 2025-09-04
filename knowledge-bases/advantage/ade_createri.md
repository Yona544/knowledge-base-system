CreateRI




Advantage Database Server 12  

TAdsDictionary.CreateRI

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.CreateRI  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.CreateRI Advantage TDataSet Descendant ade\_Createri Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.CreateRI  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.CreateRI( strRIName : string; strFailTable : string;

strParentTable : string;

strParentTagName : string; strChildTable : string;

strChildTagName : string; usUpdateRule : UNSIGNED16;

usDeleteRule : UNSIGNED16; strNoPKeyError : string;

strCascadeError : string );

 

TAdsDictionary.CreateRI( strRIName : string; strFailTable : string;

strParentTable : string;

strParentTagName : string; strChildTable : string;

strChildTagName : string; usUpdateRule : UNSIGNED16;

usDeleteRule : UNSIGNED16 );

Parameters

|  |  |
| --- | --- |
| strRIName (I) | The name of the RI object. |
| strFailTable (I) | The table where failed records will be placed. If a file already exists by the same name, it is overwritten. |
| strParentTable (I) | The data dictionary name of the parent table in the RI relationship. |
| strParentTagName (I) | The name of the parent index in the RI relationship. |
| strChildTable (I) | The data dictionary name of the child table in the RI relationship. |
| strChildTagName (I) | The name of the child index in the RI relationship. |
| usUpdateRule (I) | That action that the server is to perform when any update to the parent or foreign table does not maintain the referential integrity. The actions are: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_RESTRICT, ADS\_DD\_RI\_SETNULL, or ADS\_DD\_RI\_SETDEFAULT |
| usDeleteRule (I) | That action that the server is to perform when a delete in the parent or foreign table does not maintain the referential integrity. The actions are: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_RESTRICT, ADS\_DD\_RI\_SETNULL, or ADS\_DD\_RI\_SETDEFAULT |
| strNoPKeyError | An optional custom error message to return when a primary key violation is encountered. A NULL may be used to indicate you would like the default error message to be used. |
| strCascadeError | An optional custom error message to return when an error is encountered during a cascade operation. A NULL may be used to indicate you would like the default error message to be used. |

Remarks

TAdsDictionary.CreateRI62 will open the parent and the child table exclusively. The parent table must have a primary index already defined. The primary and foreign keys must be the same size. The fields in the primary index expression will be compared with the fields in the foreign key expression. The fields must be of the identical size and type but may have different names. The parent index name must be NULL or the primary key index name. This parameter may be used in the future to allow the user to indicate a candidate key to use as the parent.

ALTER TABLE permissions are required on both related tables to add a relation to a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

 

Note If you are using Delphi3, only one instance of this overloaded method is available. If necessary, call the Advantage Client Engine (ACE) API AdsCreateRefIntegrity62 directly for full functionality.

Example

procedure CreateRIExample;

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

 

{\* now we need to set the primary index for offices \*}

usLength := 7;

oAdsDictionary.SetTableProperty( 'offices',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'office' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

{\* now we create the RI rule\*}

oAdsDictionary.CreateRI( 'RI Office Rule',

'',

'offices',

'office',

'salesreps',

'rep\_office',

ADS\_DD\_RI\_CASCADE,

ADS\_DD\_RI\_CASCADE );

 

{\* now we are going to get the parent table property \*}

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetRIProperty( 'RI Office Rule',

ADS\_DD\_RI\_PRIMARY\_TABLE,

@aucProperty,

usLength );

 

oAdsDictionary.IsConnected := FALSE;

oAdsDictionary.Free;

 

end;

See Also

[RemoveRI](ade_removeri.htm)