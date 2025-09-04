---
title: Ace Adsddremoverefintegrity
slug: ace_adsddremoverefintegrity
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremoverefintegrity.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a36b18197356e5b3723c5408a9f3dd7d27fbe10a
---

# Ace Adsddremoverefintegrity

AdsDDRemoveRefIntegrity

AdsDDRemoveRefIntegrity

Advantage Client Engine

| AdsDDRemoveRefIntegrity  Advantage Client Engine |  |  |  |  |

Removes a referential integrity (RI) constraint from the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveRefIntegrity( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucRIName );

Parameters

| hAdminConn (I) | The data dictionary connection. |
| pucRIName | Name of the RI constraint in the data dictionary to be removed. |

Description

AdsDDRemoveRefIntegrity will remove a RI constraint from the data dictionary.

The parent and child table must not be opened, so that the Advantage Client Engine can temporarily open the parent and the child tables exclusively. This function will temporarily open all tables exclusively that are in the data dictionary and that interlink with these tables through other RI constraints.

ALTER TABLE permissions are required on both related tables to remove a relation from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetCode = AdsDDRemoveRefIntegrity( hDD, "salesreps.rep\_office to offices.office" );

See Also

[AdsDDGetRefIntegrityProperty](ace_adsddgetrefintegrityproperty.md)

[AdsDDCreateRefIntegrity](ace_adsddcreaterefintegrity.md)

[sp\_DropReferentialIntegrity](master_sp_dropreferentialintegrity.md)
