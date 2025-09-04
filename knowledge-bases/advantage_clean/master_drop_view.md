---
title: Master Drop View
slug: master_drop_view
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_drop_view.htm
source: Advantage CHM
tags:
  - master
checksum: 73f8f9c87b329a2d82c9f3fa032c05eb19397d76
---

# Master Drop View

DROP VIEW

DROP VIEW

Advantage SQL Engine

| DROP VIEW  Advantage SQL Engine |  |  |  |  |

Deletes a view from the database

Syntax

DROP VIEW <view-name>

 

Remarks

CASCADE, RESTRICT not supported.

Views are supported through the use of the [Advantage Data Dictionary](master_advantage_data_dictionary.md). DROP VIEW statements must be executed on a valid dictionary connection, and from the dictionary administrator account.

Example(s)

DROP VIEW GoodCustomers

 

See Also

[sp\_ModifyViewProperty](master_sp_modifyviewproperty.md)
