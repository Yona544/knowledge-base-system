---
title: Ace Adsgettableopenoptions
slug: ace_adsgettableopenoptions
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettableopenoptions.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 1011537b6afddd95b00195326a145bdef81ab5b0
---

# Ace Adsgettableopenoptions

AdsGetTableOpenOptions

AdsGetTableOpenOptions

Advantage Client Engine

| AdsGetTableOpenOptions  Advantage Client Engine |  |  |  |  |

Retrieves the options used to open the table

Syntax

| UNSIGNED32 | AdsGetTableOpenOptions (ADSHANDLE hTable,  UNSIGNED32 \*pulOptions); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pulOptions (O) | A bit field of options with which the table was opened. |

Remarks

AdsGetTableOpenOptions will retrieve the option setting specified during the table open. Specific options can be determined by performing a bitwise "and" operation with a possible value to determine if the appropriate bit is set. For example, if ADS\_EXCLUSIVE was specified on an [AdsOpenTable](ace_adsopentable.md) call, in the C programming language, ulOptions & ADS\_EXCLUSIVE will evaluate a non-zero value. In Visual Basic, ulOptions AND ADS\_EXCLUSIVE would be non-zero.

Example

[Click Here](ace_examples.md#adsgettableopenoptionsexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)
