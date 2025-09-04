---
title: Ace Adsgettablerights
slug: ace_adsgettablerights
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablerights.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 95420dac65db60c0df03beb30adb810285b78713
---

# Ace Adsgettablerights

AdsGetTableRights

AdsGetTableRights

Advantage Client Engine

| AdsGetTableRights  Advantage Client Engine |  |  |  |  |

Retrieves the type of rights checking used with a table

Syntax

| UNSIGNED32 | AdsGetTableRights (ADSHANDLE hTable,  UNSIGNED16 \*pusRights); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pusRights (O) | Type of rights checking used to open the table (ADS\_CHECKRIGHTS, ADS\_IGNORERIGHTS). |

Remarks

AdsGetTableRights will retrieve the type of rights checking specified during the table open.

Example

[Click Here](ace_examples.md#adsgettablerightsexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)
