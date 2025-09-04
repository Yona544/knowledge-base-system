---
title: Master Read Ahead Record Caching
slug: master_read_ahead_record_caching
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_read_ahead_record_caching.htm
source: Advantage CHM
tags:
  - master
checksum: 940bdabd912001506139d56d16dcc6e8088ce032
---

# Master Read Ahead Record Caching

Read-Ahead Record Caching

Read-Ahead Record Caching

Advantage Concepts

| Read-Ahead Record Caching  Advantage Concepts |  |  |  |  |

Whenever you perform a Skip (Next/Prior/MoveNext/MovePrevious) operation after performing any other movement operation in your application, the next N number of records (rather than just a single record) will be read and transferred to the client. This allows the next N - 1 subsequent Skip (Next/Prior/MoveNext/MovePrevious) operations to be performed locally. The record positioned to will be retrieved from client memory, rather than having to be read over the network from the server. This should improve Skip (Next/Prior/MoveNext/MovePrevious) performance, especially when performing such operations as populating a grid or a browse window.

When using Advantage Database (remote) Server, the default number of records read and cached on the client is the lesser of 10 or the number of records that can fit in one transmission burst, which defaults to 8K for IPX and 22K for IP. When using Advantage Local Server, the default is 10 records. To change the cache size for a given table, use one of the following mechanisms:

- AdsCacheRecords for the Advantage Client Engine API

- TAdsTable/TAdsQuery.AdsTableOptions.AdsRecordCache for the Advantage TDataSet Descendant

- Forward-only cursors for the Advantage OLE DB provider. Set the DBPROP\_CANSCROLLBACKWARDS and DBPROP\_CANFETCHBACKWARDS properties to FALSE. When using ADO, specify adOpenForwardOnly as the cursor type when executing a query or opening a recordset.

- Forward-only cursors for the Advantage ODBC driver. Use SQL\_CURSOR\_FORWARD\_ONLY for the SQL\_ATTR\_CURSOR\_TYPE statement attribute.

- AdsCacheRecords for the Advantage CA-Visual Objects RDDs installed from the ACE.AEF file

Note that any records cached on the client will not reflect changes made by other users to those records in the table on the server. To "dump" the cache of records currently in memory on the client and to refresh the current record, call one of the following functions which forces the client record cache to be purged:

- AdsRefreshRecord with the Advantage Client Engine API

- TAdsTable.AdsRefreshRecord with the Advantage TDataSet Descendant

- IRowsetRefresh::RefreshVisibleData with the Advantage OLE DB Provider or the Resync method if using ADO

- SKIP 0, GOTO RECNO() or AdsRefreshRecord with the Advantage CA-Visual Objects RDDs

Note that doing any movement operation other than a Skip (Next/Prior/MoveNext/MovePrevious) will cause the record cache to get dumped. Locking or updating a record will also cause the record cache to be dumped and the latest version of the record to be read to the client.

In theory, the ideal value for the number of records to read-ahead would be the number of records that normally appear in your application's grid or browse window. For example, if your applications grid or browse window contains 20 records, you may consider changing the read-ahead record value to 20 so that the entire set of records can be read with one server request. However, if your application is repeatedly doing a single Skip (Next/Prior/MoveNext/MovePrevious) operation, reading ahead 20 records and not using them may degrade your applications performance. You may want to experiment with the number of records to read-ahead in your application to find a value that provides best performance.

If your application is stepping through a recordset and updating most or all records, it will probably be best to turn off the read-ahead caching because each time a record is updated, the cache will be dumped.

The following chart shows how many seconds it took to do 10000 iterations of consecutive Skip (Next/MoveNext) operations with various read-ahead record caching values. Since an individual Skip (Next/MoveNext) operation takes just milliseconds to perform, 10000 were iterations were necessary to produce result times in readable whole numbers. For example, to do 10 consecutive Skip (Next/MoveNext) operations with a read-ahead record value of 1 took 187 seconds. To do the same 10 consecutive Skip (Next/MoveNext) operations with a read-ahead record value of 10 took just 71 seconds. Thus, if your application commonly does 10 consecutive Skip (Next/MoveNext) operations, setting the read-ahead record value to 10 would increase your applications Skip (Next/MoveNext) performance by over 250%.

Time (in seconds) to do 10000 Iterations of Consecutive Skip (Next/MoveNext) Operations

| Number of Records to Read Ahead | | | | | | | |
|  |  | 1 | 5 | 10 | 15 | 20 | 25 |
|  | 24 | 401 | 172 | 142 | 130 | 154 | 104 |
|  | 23 | 383 | 166 | 141 | 130 | 154 | 106 |
|  | 22 | 370 | 166 | 139 | 129 | 154 | 104 |
|  | 21 | 354 | 164 | 138 | 130 | 154 | 105 |
|  | 20 | 340 | 141 | 103 | 129 | 94 | 104 |
|  | 19 | 323 | 141 | 103 | 129 | 93 | 105 |
|  | 18 | 309 | 139 | 107 | 128 | 93 | 104 |
| Number of | 17 | 298 | 141 | 112 | 129 | 93 | 104 |
| Consecutive | 16 | 280 | 142 | 113 | 129 | 93 | 105 |
| Skip | 15 | 259 | 117 | 112 | 81 | 89 | 104 |
| (Next/MoveNext) | 14 | 248 | 114 | 110 | 80 | 88 | 104 |
| Operations | 13 | 230 | 112 | 110 | 81 | 88 | 103 |
|  | 12 | 216 | 114 | 111 | 81 | 88 | 103 |
|  | 11 | 200 | 112 | 111 | 80 | 88 | 103 |
|  | 10 | 187 | 86 | 71 | 80 | 87 | 103 |
|  | 9 | 169 | 88 | 71 | 79 | 87 | 103 |
|  | 8 | 151 | 85 | 71 | 80 | 87 | 103 |
|  | 7 | 127 | 87 | 73 | 80 | 91 | 102 |
|  | 6 | 113 | 86 | 70 | 80 | 91 | 103 |
|  | 5 | 99 | 57 | 73 | 81 | 90 | 102 |
|  | 4 | 85 | 59 | 71 | 78 | 90 | 103 |
|  | 3 | 75 | 59 | 70 | 78 | 90 | 102 |
|  | 2 | 60 | 59 | 69 | 76 | 89 | 102 |
|  | 1 | 43 | 59 | 71 | 76 | 88 | 102 |

With Advantage Local Server, read-ahead record caching is only used when reading tables/cursors in natural record order and when existing filters are not overly sparse. The benefit of reading multiple records with a single request is only realized with Advantage Local Server when a single read from the file can acquire multiple records that will be used. With Advantage Database Server, this is not a limitation because the reading occurs at the server and can be transmitted across the wire with a single request.
