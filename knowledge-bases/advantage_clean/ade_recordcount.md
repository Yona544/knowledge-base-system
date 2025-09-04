---
title: Ade Recordcount
slug: ade_recordcount
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_recordcount.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 36b4b2f82ce2e836f0674f589834fb56b402fa3c
---

# Ade Recordcount

RecordCount

TAdsTable.RecordCount

Advantage TDataSet Descendant

| TAdsTable.RecordCount  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Indicates the total number of records associated with the dataset.

Syntax

property RecordCount: Longint;

Description

Examine RecordCount to determine the total number of records in the data set. Applications might use this property with RecNo to iterate through all the records in a data set, though typically record iteration is handled with calls to First, Last, MoveBy, and Prior.

If filters or ranges/scopes are to be respected in the RecordCount, make sure to set the constants appropriately for the properties AdsTableOptions.AdsFilterOptions and AdsTableOptions.AdsScopeOptions.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is IGNORE\_SCOPES\_WHEN\_COUNTING, this function will return the total number of records in the table if there is no active index, or the number of records referenced by the index order if an index is active.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is RESPECT\_SCOPES\_WHEN\_COUNTING and an index is active, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING and no index is active, all records that pass the active filter may have to be skipped through and counted. Thus, with large tables where many records pass the filter, this function can be very slow. If the only filter on the table is an Advantage Optimized Filter, and the filter was fully optimized, the record count for that AOF will be returned and the operation will be very fast.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING and an index is active, all records referenced by keys in the index that pass any filter and/or scope/range must be skipped through and counted. Thus, with large indexes where many records pass the filter and/or keys pass the scope/range, this function can be very slow.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and no index is active, this function will be very fast; the table's current record count will be returned without reading the count from the actual table header. If it is known that other applications are appending records to the table and a more accurate count is needed, AdsTableOptions.AdsFreshRecordCount should be set to True. Note that if other applications are appending records to a table, even if AdsTableOptions.AdsFreshRecordCount is set to True, there is no guarantee that the record count will be accurate because it is possible for another application to append a record immediately after the record count is retrieved. To guarantee an accurate count, an application must either lock the table or open it exclusively.

With ADT tables, the record count is always adjusted by the number of deleted records.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.
