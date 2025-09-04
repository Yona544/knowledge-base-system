---
title: Vo Ax Setcollation
slug: vo_ax_setcollation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_setcollation.htm
source: Advantage CHM
tags:
  - vo
checksum: ccb7bce769751f33572adcb809f99cfc03f7d247
---

# Vo Ax Setcollation

AX\_SetCollation()

AX\_SetCollation()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_SetCollation()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Syntax

AX\_SetCollation( strCollation AS STRING )

Parameters

| <strCollation> | Collation language for the RDD to use. |

 

Returns

The previous collation setting.

Description

This function specifies which collation language to use when opening tables, opening cursors, or creating tables. By default, no collation language is set and the client will use the language set by the Advantage Database Server.

Note Collation languages are only valid with ADT and VFP tables. For all other table types, the collation language is ignored.

See Also

[AdsSetCollation](ace_adssetcollation.md)

[AdsOpenTable90](ace_adsopentable90.md)

[AdsCreateTable90](ace_adscreatetable.md)
