---
title: Ace Adsddsetprocedureproperty
slug: ace_adsddsetprocedureproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetprocedureproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0c658b31b64479056f0bcfda4c34a62a6e1d6edb
---

# Ace Adsddsetprocedureproperty

AdsDDSetProcedureProperty

AdsDDSetProcedureProperty

Advantage Client Engine

| AdsDDSetProcedureProperty  Advantage Client Engine |  |  |  |  |

Sets one property associated with a stored procedure definition in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetProcedureProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucProcedureName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection. |
| pucProcedureName (I) | Name of the stored procedure object to set the associated property. |
| usPropertyID (I) | Index of a procedure property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucProcedureName does not specify a valid stored procedure in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid procedure property ID, or the specified property cannot be set. |

Remarks

AdsDDSetProcedureProperty sets one property associated with the specified stored procedure. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the procedure are required to modify data dictionary stored procedure properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the stored procedure definition. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the description is removed. |
| ADS\_DD\_PROC\_INPUT | Changes the input parameter definition for the stored procedure. The format of this string is the same as the string passed into [AdsCreateTable](ace_adscreatetable.md) to define fields in a table. This definition will be used to create a table that will be populated with the input values. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If the stored procedure has no input, pass NULL for pvProperty. |
| ADS\_DD\_PROC\_OUTPUT | Changes the output parameter definition for the stored procedure. The format of this string is the same as the string passed into [AdsCreateTable](ace_adscreatetable.md) to define fields in a table. This definition will be used to create a table that will be populated with the output values. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If the stored procedure has no output, pass NULL for pvProperty. |
| ADS\_DD\_PROC\_DLL\_NAME | Changes the stored procedure container file name. This value must be a relative path from the Advantage Data dictionary (.ADD) file. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_PROC\_DLL\_FUNCTION\_NAME | Changes the procedure name within the stored procedure container file name. This is the name of the function that is executed when the stored procedure is called. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |

Example

After making a connection to the database, set a new container file name.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDSetProcedureProperty( hDD, "proc1", ADS\_DD\_PROC\_DLL\_NAME, "myprocs.aep", 12 );

See Also

[AdsDDAddProcedure](ace_adsddaddprocedure.md)

[AdsDDRemoveProcedure](ace_adsddremoveprocedure.md)

[AdsDDGetProcedureProperty](ace_adsddgetprocedureproperty.md)

[sp\_ModifyProcedureProperty](master_sp_modifyprocedureproperty.md)
