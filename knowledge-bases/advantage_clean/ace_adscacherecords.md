---
title: Ace Adscacherecords
slug: ace_adscacherecords
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscacherecords.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0ac6ae33cfa73b7aabcd9e27eadc7c5073dcc016
---

# Ace Adscacherecords

AdsCacheRecords

AdsCacheRecords

Advantage Client Engine

| AdsCacheRecords  Advantage Client Engine |  |  |  |  |

Sets the number of records to read ahead into client cache on skip operations.

Syntax

| UNSIGNED32 | AdsCacheRecords (ADSHANDLE hTable,  UNSIGNED16 usRecords); |

Parameters

| hTable (I) | Handle of a table or cursor. |
| usRecords (I) | The number of records to be read into the cache by movement operations that use record caching. |

Remarks

Whenever you perform a skip operation after performing any other movement operation in your application, the next N records will be read and transferred to the client rather than just a single record. This allows the next N - 1 subsequent skip operations to be performed locally. Thus, the next record will be retrieved from client memory, rather than having to be read over the network from the server. The default number of records that is read and cached on the client is the lesser of 10 or the number of records that can fit in a burst of packets from the Advantage Database Server to the Advantage client. The default burst of packets can contain 8K bytes of data when using IPX for communication and about 22K when using IP.

A usRecords value of 0 (or 1) effectively turns read-ahead record caching off. Testing has shown that, in most cases, read-ahead values greater than 100 records are not beneficial. Also, any editing of data causes the cache to be dumped. Therefore, it is probably detrimental to use a large cache size if an edit is to be made on most records. If a batch operation is being used to skip through a large number of records and update each record, it is probably best to turn off read-ahead record caching.

Any records that are cached on the client will not reflect changes made by other users to those actual records in the table on the server. To "dump" the cache of records currently in memory on the client and to refresh the current record, call [AdsRefreshRecord](ace_adsrefreshrecord.md) which forces the client record cache to be purged.

Note This API has no effect when reading data in index order with the Advantage Local Server.

Example

None.

See Also

[AdsRefreshRecord](ace_adsrefreshrecord.md)
