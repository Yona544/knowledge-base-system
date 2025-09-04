---
title: Ade Getstoredprocedurenames
slug: ade_getstoredprocedurenames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getstoredprocedurenames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0009f0b8482349f878b895b26c1e8b35ed8d1aab
---

# Ade Getstoredprocedurenames

GetStoredProcedureNames

TAdsDictionary.GetStoredProcedureNames

Advantage TDataSet Descendant

| TAdsDictionary.GetStoredProcedureNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetStoredProcedureNames( poSPNames : TStringList );

Parameters

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

[AddProcedure](ade_addprocedure.md)

[RemoveProcedure](ade_removeprocedure.md)

[GetProcedureProperty](ade_getprocedureproperty.md)
