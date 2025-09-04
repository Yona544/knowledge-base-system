---
title: Ace Adsgettablechartype
slug: ace_adsgettablechartype
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablechartype.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3c361607d6d0fb63176ea8e3a3f5a7e9c3fb8468
---

# Ace Adsgettablechartype

AdsGetTableCharType

AdsGetTableCharType

Advantage Client Engine

| AdsGetTableCharType  Advantage Client Engine |  |  |  |  |

Retrieves the setting of the character data type with which the table was opened/created

Syntax

| UNSIGNED32 | AdsGetTableCharType (ADSHANDLE hTable,  UNSIGNED16 \*pusCharType); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusCharType (O) | Type of character data in table (ADS\_OEM, ADS\_ANSI). |

Remarks

AdsGetTableCharType will retrieve the setting of the character data type specified during the table open/create. Note that ADS\_ANSI will always be returned if the usTableType parameter used in the open/create was ADS\_ADT.

If one of the [dynamic collations](master_collation_support.md) was specified when creating or opening the table, the value returned will still be ADS\_ANSI or ADS\_OEM depending on the collation selected.

Example

[Click Here](ace_examples.md#adsgettablechartypeexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableCollation](ace_adsgettablecollation.md)
