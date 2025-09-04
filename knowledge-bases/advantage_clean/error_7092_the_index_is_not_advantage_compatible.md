---
title: Error 7092 The Index Is Not Advantage Compatible
slug: error_7092_the_index_is_not_advantage_compatible
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7092_the_index_is_not_advantage_compatible.htm
source: Advantage CHM
tags:
  - error
checksum: 83cd8ec59884bf2ee75a7e503138ee1bc7b4173d
---

# Error 7092 The Index Is Not Advantage Compatible

7092 The index is not Advantage compatible

7092 The index is not Advantage compatible

Advantage Error Guide

| 7092 The index is not Advantage compatible  Advantage Error Guide |  |  |  |  |

Problem: Advantage has detected that the index was not built with an Advantage-compatible format. This problem can occur if the original index was built with the CA-Clipper 5.3 DBFCDX RDD, which does not create FoxPro-compatible indexes.

Solution: Rebuild the index with Advantage. For example, open the table with Advantage Data Architect and click the re-index button, or choose Re-Index from the Table menu.

If you get this error when using the Advantage proprietary table format (.ADT/.ADI), report the error to Advnatage [Technical Support](master_technical_support_u_s__and_canada.md).
