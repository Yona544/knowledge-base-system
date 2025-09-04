---
title: Ace Adslocktable
slug: ace_adslocktable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adslocktable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 99c0eb4daea19f5bedaa47190d4183cfa04dff60
---

# Ace Adslocktable

AdsLockTable

AdsLockTable

Advantage Client Engine

| AdsLockTable  Advantage Client Engine |  |  |  |  |

Attempts to lock the given table

Syntax

| UNSIGNED32 | AdsLockTable (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table |

Special Return Codes

| AE\_LOCK\_FAILED | The attempted lock failed. The lock may be held by another user. |
| AE\_TABLE\_NOT\_SHARED | A lock was attempted on a table opened exclusively. |

Remarks

A successful call to AdsLockTable prevents other applications from being able to update the table. It is recommended that you lock tables prior to creating indexes. Any record locks that have been obtained prior to calling AdsLockTable will be released. If the Advantage Client Engine fails to lock the table (e.g., if another user has record locks), then the Advantage Client Engine does not attempt to relock the records that it released.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Example

[Click Here](ace_examples.md#adslocktableexample)

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsIsTableLocked](ace_adsistablelocked.md)

[AdsLockRecord](ace_adslockrecord.md)

[AdsUnlockTable](ace_adsunlocktable.md)
