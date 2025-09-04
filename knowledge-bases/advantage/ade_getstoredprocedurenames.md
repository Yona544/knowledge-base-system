GetStoredProcedureNames




Advantage Database Server 12  

TAdsDictionary.GetStoredProcedureNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetStoredProcedureNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetStoredProcedureNames Advantage TDataSet Descendant ade\_Getstoredprocedurenames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetStoredProcedureNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.GetStoredProcedureNames( poSPNames : TStringList );

Parameters

|  |  |
| --- | --- |
| poSPNames (O) | A TStringList that will contain all of the stored procedure names that are in the database. |

Remarks

GetStoredProcedureNames will get all of the names of the stored procedures in the database.

Example

procedure GetStoredProcedureNamesExample

var

oAdsDictionary : TAdsDictionary;

usPropertyLen : UNSIGNED16;

pucProperty : array[0..ADS\_DD\_MAX\_PROPERTY\_LEN] of char;

oSPNames : TStringList;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

oAdsDictionary.AddProcedure( 'NewProcedure',

'.\sp.aep',

'Echo',

ADS\_STORED\_PROC,

'InParam,Char,10',

'OutParam,Char,10',

'This is a stored procedure' );

 

usPropertyLen := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetProcedureProperty( 'NewProcedure',

ADS\_DD\_PROC\_DLL\_NAME,

@pucProperty,

usPropertyLen );

 

oSPNames := TStringList.Create;

oAdsDictionary.GetStoredProcedureNames( oSPNames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;

See Also

[AddProcedure](ade_addprocedure.htm)

[RemoveProcedure](ade_removeprocedure.htm)

[GetProcedureProperty](ade_getprocedureproperty.htm)