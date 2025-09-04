---
title: Master Sp Modifyprocedureproperty
slug: master_sp_modifyprocedureproperty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifyprocedureproperty.htm
source: Advantage CHM
tags:
  - master
checksum: 8a8cb713d4c9f8f44556ba56ecef177d641814c6
---

# Master Sp Modifyprocedureproperty

sp\_ModifyProcedureProperty

sp\_ModifyProcedureProperty

Advantage SQL Engine

| sp\_ModifyProcedureProperty  Advantage SQL Engine |  |  |  |  |

Modifies an existing stored procedure definition in the data dictionary.

Syntax

sp\_ModifyProcedureProperty(

ProcedureName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

sp\_ModifyProcedureProperty(

ProcedureName,CHARACTER,200,

Property,CHARACTER,200,

Value,NMemo )

Parameters

| ProcedureName (I) | Name of the existing stored procedure definition to modify. |
| Property (I) | Name of the property to set. See Remarks for allowed values. |
| Value (I) | Property value to set. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the stored procedure definition cannot be found. |

Remarks

This procedure modifies an existing stored procedure definition. The following are the valid values of Property and the expected value in Value.

| usPropertyID | Description |
| COMMENT | Stores a new description for the procedure. |
| PROC\_INPUT | Changes the input parameter definition for the stored procedure. The format of this string is the same as the string passed into the ACE API AdsCreateTable to define fields in a table. This definition will be used to create a table that will be populated with the input values. If the stored procedure has no input, pass NULL as the value. |
| PROC\_OUTPUT | Changes the output parameter definition for the stored procedure. The format of this string is the same as the string passed into the ACE API AdsCreateTable to define fields in a table. This definition will be used to create a table that will be populated with the output values. If the stored procedure has no output, pass NULL as the value. |
| PROC\_DLL\_NAME | Changes the stored procedure container file name. This value must be a relative path from the Advantage Data dictionary (.ADD) file. |
| PROC\_DLL\_FUNCTION\_NAME | Changes the procedure name within the stored procedure container file name to be executed when the procedure is called. |

Example

After making a connection to the database, set a new container file name.

EXECUTE PROCEDURE sp\_ModifyProcedureProperty(

'proc1',

'PROC\_DLL\_NAME',

'myprocs.aep' );

See Also

[CREATE PROCEDURE](master_create_procedure.md)

[DROP PROCEDURE](master_drop_procedure.md)
