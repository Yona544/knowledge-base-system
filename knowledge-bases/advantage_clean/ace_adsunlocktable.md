---
title: Ace Adsunlocktable
slug: ace_adsunlocktable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsunlocktable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5984913d74a492569c16c55a84260f644f350995
---

# Ace Adsunlocktable

AdsUnlockTable

AdsUnlockTable

Advantage Client Engine

| AdsUnlockTable  Advantage Client Engine |  |  |  |  |

Releases all locks on the given table

Syntax

| UNSIGNED32 | AdsUnlockTable (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of table. If a table lock is held, it is released. Otherwise, all record locks are released. |

Special Return Codes

| AE\_TABLE\_NOT\_LOCKED | The table was not locked, so it could not be unlocked. |
| AE\_TABLE\_NOT\_SHARED | An unlock was attempted on a table opened exclusively. |

Remarks

AdsUnlockTable releases either all record locks on the table, or a table lock if one exists. If record locks are held and the table is in a transaction, the record locks will be released at the end of the transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Note Releasing file locks while in a transaction is illegal.

Example

[Click Here](ace_examples.md#adsunlocktableexample)

See Also

[AdsLockTable](ace_adslocktable.md)

[AdsIsTableLocked](ace_adsistablelocked.md)

[AdsLockRecord](ace_adslockrecord.md)

[AdsGetAllLocks](ace_adsgetalllocks.md)

[AdsUnlockRecord](ace_adsunlockrecord.md)
