---
title: Ace Adsddremoveview
slug: ace_adsddremoveview
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremoveview.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5c0a524ee9c314aaa4eb3ea82f7ee152fac68350
---

# Ace Adsddremoveview

AdsDDRemoveView

AdsDDRemoveView

Advantage Client Engine

| AdsDDRemoveView  Advantage Client Engine |  |  |  |  |

Removes a VIEW from an Advantage Data Dictionary. See [Advantage SQL Engine](master_advantage_sql_engine.md) for more specific VIEW documentation.

Syntax

UNSIGNED32 AdsDDRemoveView( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName );

Parameters

| hAdminConn (I) | Dictionary connection handle |
| pucName (I) | Name of the VIEW to remove |

Remarks

AdsDDRemoveView will remove a view from an [Advantage Data Dictionary](master_advantage_data_dictionary.md).

DROP permissions on the view are required to remove a view from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

AdsDDRemoveView( hConn, "myview" );

See Also

[AdsDDAddView](ace_adsddaddview.md)

[AdsDDGetViewProperty](ace_adsddgetviewproperty.md)

[AdsDDSetViewProperty](ace_adsddsetviewproperty.md)
