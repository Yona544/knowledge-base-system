---
title: Ace Adsddaddview
slug: ace_adsddaddview
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddaddview.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d5dd06a7405ddd6f0f001f6b7201f860da35e1c4
---

# Ace Adsddaddview

AdsDDAddView

AdsDDAddView

Advantage Client Engine

| AdsDDAddView  Advantage Client Engine |  |  |  |  |

Adds a VIEW to an Advantage Data Dictionary. See [Views](master_views.md) for more specific VIEW information.

Syntax

UNSIGNED32 AdsDDAddView( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName,

UNSIGNED8 \*pucComments,

UNSIGNED8 \*pucSQL );

 

UNSIGNED32 AdsDDAddView100( ADSHANDLE hAdminConn,

                           UNSIGNED8 \*pucName,

                           UNSIGNED8 \*pucComments,

                           WCHAR     \*pwcSQL );

Parameters

| hAdminConn (I) | Dictionary connection handle. |
| pucName (I) | Name of the new VIEW object to create. |
| pucComments (I) | Optional comments. |
| pucSQL (I) | SQL SELECT statement definition of the VIEW. |

Remarks

AdsDDAddView will add a new view to an Advantage Data Dictionary. Once created the view can be referenced in SQL statements or opened directly with a call to [AdsOpenTable](ace_adsopentable.md).

CREATE VIEW permissions are required to add a view to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note AdsDDAddView can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

AdsDDAddView( hConn, "myview", "test comment", "select \* from customers where

credit\_limit > 50000" );

See Also

[AdsDDRemoveView](ace_adsddremoveview.md)

[AdsDDGetViewProperty](ace_adsddgetviewproperty.md)

[AdsDDSetViewProperty](ace_adsddsetviewproperty.md)
