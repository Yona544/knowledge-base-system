---
title: Ade Removeprocedure
slug: ade_removeprocedure
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeprocedure.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 26d54d8ff161ba1f484253cc5c743cf052ae0a6f
---

# Ade Removeprocedure

RemoveProcedure

TAdsDictionary.RemoveProcedure

Advantage TDataSet Descendant

| TAdsDictionary.RemoveProcedure  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Removes a stored procedure definition from the data dictionary.

Syntax

procedure RemoveProcedure( strName : string );

Parameters

| pucName (I) | The stored procedure data dictionary name to remove from the data dictionary. |

Remarks

This function may be used to remove a stored procedure definition from the Advantage Data Dictionary. Other methods of removing stored procedures are the "DROP PROCEDURE" SQL syntax or by using Advantage Data Architect.

DROP permissions on the procedure are required to remove a procedure from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveProcedureExample;

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

 

oAdsDictionary.RemoveProcedure( 'NewProcedure' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

 

 

end;
