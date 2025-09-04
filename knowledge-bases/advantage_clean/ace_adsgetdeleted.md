---
title: Ace Adsgetdeleted
slug: ace_adsgetdeleted
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdeleted.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: cc68d9f21811d1852cfd9c44e12e3592b60b3965
---

# Ace Adsgetdeleted

AdsGetDeleted

AdsGetDeleted

Advantage Client Engine

| AdsGetDeleted  Advantage Client Engine |  |  |  |  |

Retrieves the current show deleted setting

Syntax

| UNSIGNED32 | AdsGetDeleted (UNSIGNED16 \*pbShowDeleted); |

Parameters

| pbShowDeleted (O) | Contains the retrieved deleted setting. |

Remarks

AdsGetDeleted will return the current value of the ShowDeleted setting, which can be set by [AdsShowDeleted](ace_adsshowdeleted.md). True means that deleted records in a DBF table will be visible to the user.

AdsGetDeleted is a global setting that affects the behavior of the entire application.

Note AdsShowDeleted has no effect upon Advantage proprietary ADT tables. Records that are deleted in ADT tables can never be retrieved by a client application.

Example

[Click Here](ace_examples.md#adsgetdeleteexample)

See Also

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsRecallRecord](ace_adsrecallrecord.md)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.md)

[AdsShowDeleted](ace_adsshowdeleted.md)
