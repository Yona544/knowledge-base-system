---
title: Odbc Character Set
slug: odbc_character_set
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_character_set.htm
source: Advantage CHM
tags:
  - odbc
checksum: 3c5d822500c621e9afad90b33293bdacf0bfcafd
---

# Odbc Character Set

Character Set

Character Set

| Character Set |  |  |  |  |

Character Sets are important when using the Advantage ODBC Driver in international environments. They are used to determine what characters are available in the chosen language. The character set setting also defines the collation sequence. Two options are available: OEM and ANSI.

As a default, OEM specifies the DOS (ASCII) character set. If your database files were created with a DOS application, then OEM must be selected. If OEM is chosen, an appropriate language must also be chosen.

Note If OEM is chosen, the Advantage ODBC Driver performs OEM to ANSI conversions. It assumes that the Windows settings are set appropriately for the conversion.

ANSI is the definition of character sets as established by Microsoft Windows. Any database files created by Windows applications most likely are defined with ANSI character sets. For these files, choose the ANSI setting.

When using Advantage-proprietary ADT tables, ANSI character sets are always used.

In addition to the ANSI and OEM character sets (collation tables) that are stamped into Advantage Database Server, it is also possible to use [dynamically loaded collation tables](master_collation_support.md) for Visual FoxPro collation compatibility.
