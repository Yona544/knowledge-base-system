---
title: Ace Adswriteallrecords
slug: ace_adswriteallrecords
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adswriteallrecords.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 89c0eb2ca5529d25e5468fd2c1ddbeb18f7432b8
---

# Ace Adswriteallrecords

AdsWriteAllRecords

AdsWriteAllRecords

Advantage Client Engine

| AdsWriteAllRecords  Advantage Client Engine |  |  |  |  |

Writes changes for all open tables in the current application.

Syntax

| UNSIGNED32 | AdsWriteAllRecords(); |

Parameters

None.

Remarks

AdsWriteAllRecords will flush all pending updates on all open tables to disk. It will also release all implicit locks held in all tables.

Example

[Click Here](ace_examples.md#adswriteallrecordsexample)

See Also

[AdsWriteRecord](ace_adswriterecord.md)
