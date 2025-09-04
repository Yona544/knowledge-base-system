---
title: Error 5209 Ae Collations Do Not Match
slug: error_5209_ae_collations_do_not_match
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5209_ae_collations_do_not_match.htm
source: Advantage CHM
tags:
  - error
checksum: 71753d1fed0089a66bd987a054eb0b667ec3e553
---

# Error 5209 Ae Collations Do Not Match

5209 AE\_COLLATIONS\_DO\_NOT\_MATCH

5209 AE\_COLLATIONS\_DO\_NOT\_MATCH

Advantage Error Guide

| 5209 AE\_COLLATIONS\_DO\_NOT\_MATCH  Advantage Error Guide |  |  |  |  |

Problem: A table was opened that has one or more indexes built with collations that do not match the currently specified collation.

Solution: The purpose of this error is to raise visibility to the potential optimization problems that can occur when [dynamic collations](master_collation_support.md) are used. For example, if the static OEM collation is currently being used and a table has an index built using MACHINE\_VFP\_BIN\_895, then this error will be generated when the table is opened. This can be avoided by specifying the appropriate dynamic collation for the table or SQL statement.

If an application needs to use multiple collations concurrently on a single table, this error can be turned off with the [sp\_AllowMultipleCollations](master_sp_allowmultiplecollations.md) system procedure.
