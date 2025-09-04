---
title: Oledb Record Caching
slug: oledb_record_caching
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_record_caching.htm
source: Advantage CHM
tags:
  - oledb
checksum: ee98681a071125db46bc13bf2aa980bf5ce9e1a0
---

# Oledb Record Caching

Record Caching

Record Caching

Advantage OLE DB Provider (for ADO)

| Record Caching  Advantage OLE DB Provider (for ADO) |  |  |  |  |

By default, the Advantage OLE DB provider performs some caching of records as it reads them to reduce network traffic. By default, the cache size for each rowset is 1 Megabyte. You can change the cache size through the Advantage Client Engine initialization file ADS.INI, which is expected to be located in the Windows directory. The entry is named RECORD\_CACHE\_SIZE and must be in the [SETTINGS] section. It specifies the cache size in bytes. For example, the following would set the cache size to 2 Megabytes:

 

[SETTINGS]

RECORD\_CACHE\_SIZE=2097152

 

The amount of cache required for each record is the record length plus 4. If you do not want a cache to be maintained, you can set the value to 0 to turn it off. Note that the cache is allocated as needed up to the specified limit. Thus, if you set a cache size of 4 Megabytes, for example, it will only allocate that much memory if enough records are read to fill the cache. In addition, if the cache is ever exceeded for a given rowset, the cache is eliminated for that rowset instance to avoid the cost of maintaining the cache with little chance of benefiting from future cache hits.

The record cache is primarily intended to speed up performance of applications that are oriented mainly toward user interaction. For example, data bound grids can be highly network intensive because of the number of record requests they make. If the record cache is available, it can reduce the number of network requests and improve grid response time. Note that this record caching is unrelated to the client-side caching performed by ADO when client-side cursors (adUseClient) are used. With ADO's client-side cursors, the entire rowset is read from the server as soon as the rowset as opened. After it has opened the rowset and read the data, ADO does not make further requests to read data from the provider. Once the data has been read, the client-side cursor is very fast. The drawback is the initial time to read the rowset. The record caching provided by the Advantage OLE DB provider, on the other hand, caches the records on demand, so there is no initial penalty although it can ultimately result in more network traffic in the long run depending on the type of data bound controls used and operations performed.

If an application uses client-side cursors entirely, then it may make sense to turn off the Advantage OLE DB record caching for a slight performance gain. In addition, an application that is highly geared toward batch processing may not benefit from the record caching.
