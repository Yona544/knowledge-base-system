---
title: Arc Dynamic Collation Mismatch 5209 Error
slug: arc_dynamic_collation_mismatch_5209_error
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_dynamic_collation_mismatch_5209_error.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 616a29d85595b2b91d4617b0927164621895ef9d
---

# Arc Dynamic Collation Mismatch 5209 Error

Dynamic Collation Mismatch Error (5209)

Dynamic Collation Mismatch Error (5209)

Advantage Data Architect

| Dynamic Collation Mismatch Error (5209)  Advantage Data Architect |  |  |  |  |

When using Visual FoxPro-compatible collations (dynamic collations), it is possible to build indexes using different collations on a single table. This presents the possibility of silently hiding optimization problems. For example, if you write an SQL query in Advantage Data Architect and look at the optimization plan, you might see that it is desirable to add a new index. If your application specifies a dynamic collation that is not currently chosen in Advantage Data Architect, then the new index will be built with a collation that is not used by the application. If you then run the query in your application, it might not be optimized because the collation would not match that of the new index.

To help make developers aware of this potential issue, Advantage will, by default, produce a 5209 error when a table is opened that has indexes built with collations that do not match the currently specified collation.

If you want to be able to use multiple collations concurrently on a single table, you can use the system procedure [sp\_AllowMultipleCollations](master_sp_allowmultiplecollations.md) to turn off the 5209 error. The information that controls whether this error is generated is contained in the adscollate.adt collation table repository. This means that if you turn off the 5209 error for one or more collations, it will turn it off for all applications that are using that same collation repository. For more information, see the topic on [dynamic collation support](master_collation_support.md).
