---
title: Error 5146 Ae Ri Rule Exists
slug: error_5146_ae_ri_rule_exists
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5146_ae_ri_rule_exists.htm
source: Advantage CHM
tags:
  - error
checksum: 28f385164e4804bebc2ece3d04c1cb80ab278d79
---

# Error 5146 Ae Ri Rule Exists

5146 AE\_RI\_RULE\_EXISTS

5146 AE\_RI\_RULE\_EXISTS

Advantage Error Guide

| 5146 AE\_RI\_RULE\_EXISTS  Advantage Error Guide |  |  |  |  |

A referential integrity rule exists, making the attempted operation illegal. Remove the referential integrity rule, perform the desired operation, and add the referential integrity rule back to the database.

Note Operations for which this is necessary are prone to integrity problems (AdsZapTable, etc.). When re-creating the referential integrity rule in question, use the "fail table" option and verify the desired rows (if any) are removed.
