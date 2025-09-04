---
title: Ace Adscancelupdate
slug: ace_adscancelupdate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscancelupdate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d487d4a18bbd69f9850d78dad7e25a038f58fc87
---

# Ace Adscancelupdate

AdsCancelUpdate

AdsCancelUpdate

Advantage Client Engine

| AdsCancelUpdate  Advantage Client Engine |  |  |  |  |

Cancels a pending table update.

Syntax

| UNSIGNED32 | AdsCancelUpdate (ADSHANDLE hTable) |

Parameters

| hTable (I) | Handle of table or cursor. |

Remarks

Calling AdsCancelUpdate will remove any updates to the current record that have not yet been sent to the Advantage server. If the record has been implicitly locked, the implicit lock will be released. If the record was explicitly locked, the lock is still held. If the record was appended in a DBF table, it will be written as a record with fields containing all empty values, the record will be marked for deletion, and the table will remain positioned on the appended record. With ADT tables, canceled appended records are automatically deleted and placed in the record re-use list.

Note BLOB data is written immediately; therefore changes made to fields of type ADS\_IMAGE or ADS\_BINARY through calls to [AdsSetBinary](ace_adssetbinary.md) or [AdsSetField](ace_adssetfield.md) are not cancelled by calls to AdsCancelUpdate.

Example

[Click Here](ace_examples.md#adscancelupdateexample)

See Also

[AdsLockRecord](ace_adslockrecord.md)

[AdsSetField](ace_adssetfield.md)

[AdsRefreshRecord](ace_adsrefreshrecord.md)
