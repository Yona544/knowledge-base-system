---
title: Error 7116 Unrecognized Adt Table Version
slug: error_7116_unrecognized_adt_table_version
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7116_unrecognized_adt_table_version.htm
source: Advantage CHM
tags:
  - error
checksum: ff7f4949ad816b6ead726178fec0567d7c40050c
---

# Error 7116 Unrecognized Adt Table Version

7116 Unrecognized ADT table version

7116 Unrecognized ADT table version

Advantage Error Guide

| 7116 Unrecognized ADT table version  Advantage Error Guide |  |  |  |  |

Problem: The version number of the ADT (Advantage proprietary table) is not recognized by this version of the software. The table was either created by a newer version of Advantage, or it has been corrupted.

Solution: If the table was created with a newer version of Advantage, it will be necessary to use that version of Advantage to access the table. If the table was not created by a newer version of Advantage, run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>.
