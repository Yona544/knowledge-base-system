---
title: Ace Adsgetrecordcount
slug: ace_adsgetrecordcount
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetrecordcount.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 854bff4f987e8676114810b2966db40ed757e4e2
---

# Ace Adsgetrecordcount

AdsGetRecordCount

AdsGetRecordCount

Advantage Client Engine

| AdsGetRecordCount  Advantage Client Engine |  |  |  |  |

Retrieves the total number of records in a table, the number of keys in an index, or the number of rows affected by the last executed SQL statement or SQL script.

Syntax

| UNSIGNED32 | AdsGetRecordCount (ADSHANDLE hObj,  UNSIGNED16 usFilterOption,  UNSIGNED32 \*pulCount); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| usFilterOption (I) | Indicates if filters and/or scopes are to be respected (if they are set). Options are ADS\_RESPECTFILTERS, ADS\_IGNOREFILTERS, ADS\_RESPECTSCOPES, and ADS\_REFRESHCOUNT. If ADS\_IGNOREFILTERS is used and hObj is a table handle, it can be ORed with ADS\_REFRESHCOUNT to force the Advantage Client Engine to read the current number of records from the actual table header. ADS\_RESPECTSCOPES is used only if an index order handle is passed in hObj. Using ADS\_RESPECTFILTERS respects filters and scopes. Using ADS\_RESPECTSCOPES respects scopes only. Using ADS\_IGNOREFILTERS will ignore filters and scopes. |
| pulCount (O) | Return the number of records in the table or number of keys in the index. |

Remarks

If usFilterOption contains ADS\_IGNOREFILTERS, this function will return the total number of records in the table if a table is passed in hObj, or the number of records referenced by the index order if an index order handle is passed in hObj.

If usFilterOption contains ADS\_RESPECTSCOPES and an index handle is passed in hObj, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If usFilterOption contains ADS\_RESPECTFILTERS and a table handle is passed in hObj, the Advantage Client Engine may have to skip through all records in the table that pass the active filter and count them. Thus, with large tables where many records pass the filter, this function can be very slow. If the only filter on the table is an Advantage Optimized Filter (AdsSetAOF), a table handle is passed in hObj, and the filter was fully optimized or resolved immediately, the record count for that AOF will be returned and the operation will be very fast. If deleted records are being filtered for DBF tables (AdsShowDeleted( False )), then the record count will still be computed by skipping through the records regardless of the optimization level. ADT tables do not suffer this limitation.

If usFilterOption contains ADS\_RESPECTFILTERS and an index order handle is passed in hObj, the Advantage Client Engine must skip through all records referenced by keys in the index that pass any filter and/or scope and count them. Thus, with large indexes where many records pass the filter and/or keys pass the scope, this function can be very slow.

If usFilterOption contains ADS\_IGNOREFILTERS and a table handle is passed in hObj, this function will be very fast; the Advantage Client Engine simply returns the table's current record count without reading the count from the actual table header. If usFilterOption contains ADS\_IGNOREFILTERS and an index handle is passed in hObj, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If it is known that other applications are appending records to the table and a more accurate count is needed, ADS\_REFRESHCOUNT should be OR'ed with ADS\_IGNOREFILTERS (e.g., ADS\_IGNOREFILTERS | ADS\_REFRESHCOUNT in C, ADS\_IGNOREFILTERS or ADS\_REFRESHCOUNT in Visual Basic). Note that if other applications are appending records to a table, even if ADS\_REFRESHCOUNT is used, there is no guarantee that the record count will be accurate because it is possible for another application to append a record immediately after the record count is retrieved. To guarantee an accurate count, an application must either lock the table ([AdsLockTable](ace_adslocktable.md)) or open it exclusively ([AdsOpenTable](ace_adsopentable.md)).

With ADT tables, the number of deleted records adjusts the record count even if ADS\_IGNOREFILTERS is specified.

When using SQL statements and cursors the hObj parameter can be replaced with either a statement handle or a cursor handle. If passed a cursor handle, AdsGetRecordCount will return the row count of the cursor. If passed a statement handle, the returned value will be the number of rows affected by the last SQL statement or SQL script executed on this handle. If the last executed SQL statement is not a DML statement, or if the last executed SQL script does not have any DML statement, then the value returned will be -1 (0xFFFFFFFF). If there are multiple DML statements in the last executed SQL script, the value returned will be the cumulative updated record count of all DML statements in the script.

Note If an index handle is passed to this function, it works identically to AdsGetKeyCount.

 

Note If deleted records are being filtered for DBF tables (AdsShowDeleted( False )), then the record count will still be computed by skipping through the records regardless of the optimization level. ADT tables do not suffer this limitation.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.

Example

[Click Here](ace_examples.md#adsgetrecordcountexample)

See Also

[AdsGetKeyCount](ace_adsgetkeycount.md)
