---
title: Ace Adsddremoveprocedure
slug: ace_adsddremoveprocedure
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremoveprocedure.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 534504502768951b71d2cbcb7cf9ad705b262dd1
---

# Ace Adsddremoveprocedure

AdsDDRemoveProcedure

AdsDDRemoveProcedure

Advantage Client Engine

| AdsDDRemoveProcedure  Advantage Client Engine |  |  |  |  |

Remove a stored procedure definition from the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveProcedure( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName );

Parameters

| hAdminConn (I) | Data dictionary connection handle. |
| pucName (I) | The stored procedure data dictionary name to remove from the data dictionary. |

Remarks

This function may be used to remove a stored procedure definition from the Advantage Data Dictionary. Other methods of removing stored procedures are the "DROP PROCEDURE" SQL syntax or by using Advantage Data Architect.

DROP permissions are required on the stored procedure to remove it from the data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

See Also

[AdsDDAddProcedure](ace_adsddaddprocedure.md)

[AdsDDGetProcedureProperty](ace_adsddgetprocedureproperty.md)

[AdsDDSetProcedureProperty](ace_adsddsetprocedureproperty.md)
