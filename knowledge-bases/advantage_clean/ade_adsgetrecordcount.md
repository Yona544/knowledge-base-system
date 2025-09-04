---
title: Ade Adsgetrecordcount
slug: ade_adsgetrecordcount
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetrecordcount.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 35838492c5664546a6875a950de9c33329e977bc
---

# Ade Adsgetrecordcount

AdsGetRecordCount

TAdsTable.AdsGetRecordCount

Advantage TDataSet Descendant

| TAdsTable.AdsGetRecordCount  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the total number of records in a table or the number of keys in an index.

Syntax

function AdsGetRecordCount : Longint;

Description

If filters or ranges/scopes are to be respected in the RecordCount, be sure to set the constants appropriately for the properties AdsTableOptions.AdsFilterOptions and AdsTableOptions.AdsScopeOptions.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is IGNORE\_SCOPES\_WHEN\_COUNTING, this function will return the total number of records in the table if there is no active index, or the number of records referenced by the index order if an index is active.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is RESPECT\_SCOPES\_WHEN\_COUNTING and an index is active, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING and no index is active, all records that pass the active filter may have to be skipped through and counted. Thus, with large tables where many records pass the filter, this function can be very slow. If the only filter on the table is an Advantage Optimized Filter, no index is active, and the filter was fully optimized, the record count for that AOF will be returned and the operation will be very fast.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING and an index is active, all records referenced by keys in the index that pass any filter and/or scope/range must be skipped through and counted. Thus, with large indexes where many records pass the filter and/or keys pass the scope/range, this function can be very slow.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and no index is active, this function will be very fast; the table's current record count will be returned without reading the count from the actual table header. If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and an index is active, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If it is known that other applications are appending records to the table and a more accurate count is needed, AdsTableOptions.AdsFreshRecordCount should be set to True. Note that if other applications are appending records to a table, even if AdsTableOptions.AdsFreshRecordCount is set to True, there is no guarantee that the record count will be accurate because it is possible for another application to append a record immediately after the record count is retrieved. To guarantee an accurate count, an application must either lock the table or open it exclusively.

With ADT tables, the record count is always adjusted by the number of deleted records.

Note If an index is active, this function works identically to [AdsGetKeyCount](ade_adsgetkeycount.md) .

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.

Example

lRecordCount := AdsTable1.AdsGetRecordCount;

{ lRecordCount equals 1000 }

 

AdsTable1.SetRange( ['Adams'], ['Smith'] );

lRecordCount := AdsTable1.AdsGetRecordCount;

{ lRecordCount equals 1000 }

AdsTable1.AdsTableOptions.AdsFilterOptions := RESPECT\_WHEN\_COUNTING;

lRecordCount := AdsTable1.AdsGetRecordCount;

{ lRecordCount equals 855 }

AdsTable1.CancelRange;

 

AdsTable1.AdsTableOptions.AdsFilterOptions := RESPECT\_WHEN\_COUNTING;

AdsTable1.Filter := 'LastName = "C\*"';

AdsTable1.Filtered := TRUE;

lRecordCount := AdsTable1.AdsGetRecordCount;

{ lRecordCount equals 76 }

See Also

[AdsGetKeyCount](ade_adsgetkeycount.md)

[RecordCount](ade_recordcount.md)
