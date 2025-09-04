---
title: Ace Adsddgetprocedureproperty
slug: ace_adsddgetprocedureproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetprocedureproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0f87c0eec5c09b8d7de3e1cb0098e7e066186ea8
---

# Ace Adsddgetprocedureproperty

AdsDDGetProcedureProperty

AdsDDGetProcedureProperty

Advantage Client Engine

| AdsDDGetProcedureProperty  Advantage Client Engine |  |  |  |  |

Gets a specified property from the data dictionary for a stored procedure.

Syntax

UNSIGNED32 AdsDDGetProcedureProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucProcName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucProcName (I) | The name of the stored procedure in the data dictionary. |
| usPropertyID (I) | The property to retrieve. (see below for possible values.) |
| pucProperty (O) | A buffer to hold the property value. |
| pusPropertyLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsDDGetProcedureProperty will retrieve the specified property of the stored procedure from the data dictionary.

The following are the valid values for usPropertyID:

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The comment string that is stored in the data dictionary. |
| ADS\_DD\_PROC\_INPUT | The stored procedure input parameters in same format used by AdsCreateTable when describing field definitions. |
| ADS\_DD\_PROC\_OUTPUT | The stored procedure output parameters in same format used by AdsCreateTable when describing field definitions. |
| ADS\_DD\_PROC\_SCRIPT | The SQL script that defines the stored procedure. If the stored procedure is not an SQL script, the function will return AE\_PROPERTY\_NOT\_SET.  Returned as ANSI encoded data. |
| ADS\_DD\_PROC\_DLL\_NAME | The name of the Advantage Extended Procedures file that contains the stored procedure. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. If the stored procedure is implemented using an SQL script, the function will return AE\_PROPERTY\_NOT\_SET. |
| ADS\_DD\_PROC\_SCRIPT\_W | The SQL script that defines the stored procedure. If the stored procedure is not an SQL script, the function will return AE\_PROPERTY\_NOT\_SET.  Returned as UTF-16 encoded data. |
| ADS\_DD\_PROC\_DLL\_FUNCTION\_NAME | The name of the function within the Advantage Extended Procedure file that is called when the procedure is executed. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_PROC\_INVOKE\_OPTION | This value determines the format of the stored procedure. At this time, the value is always equal to ADS\_STORED\_PROC. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid table property or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by usPropertyLen. The required buffer length is returned in usPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and usPropertylen. |

Example

usBuff = sizeof( aucBuff );

ulRetCode = AdsDDGetProcedureProperty( hConnect,

"first\_try",

ADS\_DD\_PROC\_INPUT,

aucBuff,

&usBuff );

printf( "%s\n", aucBuff );

See Also

[AdsDDAddProcedure](ace_adsddaddprocedure.md)

[AdsDDRemoveProcedure](ace_adsddremoveprocedure.md)

[AdsDDSetProcedureProperty](ace_adsddsetprocedureproperty.md)

[system.storedprocedures](master_system_storedprocedures.md)
