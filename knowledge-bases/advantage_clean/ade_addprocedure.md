---
title: Ade Addprocedure
slug: ade_addprocedure
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addprocedure.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 980e3b46d908babe491812eb91190d7eb0b414f0
---

# Ade Addprocedure

AddProcedure

TAdsDictionary.AddProcedure

Advantage TDataSet Descendant

| TAdsDictionary.AddProcedure  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure TAdsDictionary.AddProcedure( strName : string;

strDll : string;

strProcName : string;

ulInvokeOption : UNSIGNED32;

strInParams : string;

strOutParams : string;

strComments : string );

Parameters

| strName (I) | The stored procedure data dictionary name. |
| strDLL (I) | The Advantage Extended Procedure (.AEP) container file name. This value must be a relative path from the Advantage Data dictionary (.ADD) file. |
| strProcName (I) | The procedure name within the AEP container to be executed when the procedure name in strName is called. |
| ulInvokeOption (I) | This value determines the format of the stored procedure. At this time, this value must be equal to ADS\_STORED\_PROC if creating a stored procedure using a WIN32 DLL or Linux shared object. The value must be equal to ADS\_COMSTORED\_PROC if creating a COM or .NET stored procedure. |
| strInParams (I) | The definition of the input parameters for the stored procedure. The format of this string is the same as the string passed into AdsCreateTable to define the new fields in the table. This definition will be used to create a table that will be populated with the input values. This new table will be passed to the stored procedure. The stored procedure reads the input parameters from this table. If the stored procedure has no input, use NULL. |
| strOutParams (I) | The definition of the output parameters. The format of this string is the same as the strInParams. This definition will be used to create a table that will be passed to the stored procedure. The stored procedure will populate this table without its output. If the stored procedure has no output, use NULL. |
| strComments (I) | The description of the stored procedure. |

Remarks

AddStoredProc may be used to add stored procedure definitions to the Advantage Data Dictionary. An easier method of adding a stored procedure would be to use the "CREATE PROCEDURE" SQL syntax or by using the Advantage Data Architect.

CREATE PROCEDURE permissions are required to add a stored procedure to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

The only method of executing a stored procedure is through the SQL syntax "EXECUTE PROCEDURE".

This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddProcedureExample;  
var  
  oAdsDictionary : TAdsDictionary;   
begin  
  {\* call the constructor \*}   
  oAdsDictionary := TAdsDictionary.Create( self );   
   
  oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];   
   
  {\* call the method to create the data dictionary files \*}   
  oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );   
   
  {\* The CreateDictionary call leaves an ADSSYS connection open.\*}   
   
  oAdsDictionary.AddProcedure( 'NewProcedure', '.\sp.aep', 'Echo', ADS\_STORED\_PROC, 'InParam,Char,10',   
                               'OutParam,Char,10', 'This is a stored procedure' );   
   
  oAdsDictionary.IsConnected := FALSE;   
   
  oAdsDictionary.Free;

 

end;

 

 

See Also

[RemoveProcedure](ade_removeprocedure.md)

[GetProcedureProperty](ade_getprocedureproperty.md)
