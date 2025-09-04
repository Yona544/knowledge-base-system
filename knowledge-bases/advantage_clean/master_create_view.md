---
title: Master Create View
slug: master_create_view
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_create_view.htm
source: Advantage CHM
tags:
  - master
checksum: d86b4ce3615ef5551fb1924e1fe6dc1d42814069
---

# Master Create View

CREATE VIEW

CREATE VIEW

Advantage SQL Engine

| CREATE VIEW  Advantage SQL Engine |  |  |  |  |

Creates a new view in the database

Syntax

CREATE VIEW <view-name> AS SELECT <select-spec>

Remarks

SELECT statement can not have an ORDER BY clause. Views are by definition virtual base tables, which are unordered.

Views are supported through the use of the [Advantage Data Dictionary](master_advantage_data_dictionary.md). CREATE VIEW statements must be executed on a valid dictionary connection, and from the dictionary administrator account.

Example(s)

CREATE VIEW GoodCustomers AS SELECT cust\_name from customers where credit\_limit > 50000

See Also

[sp\_ModifyViewProperty](master_sp_modifyviewproperty.md)
