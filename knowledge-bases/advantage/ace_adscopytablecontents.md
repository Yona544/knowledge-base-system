AdsCopyTableContents




Advantage Database Server 12  

AdsCopyTableContents

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCopyTableContents  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCopyTableContents Advantage Client Engine ace\_Adscopytablecontents Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCopyTableContents  Advantage Client Engine |  |  |  |  |

Appends the contents of one table or cursor to another existing table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCopyTableContents (ADSHANDLE hObj,  ADSHANDLE hTableTo,  UNSIGNED16 usFilterOption); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, index handle, or cursor from which to copy. If hObj is a table handle, the resulting appended records will be in natural order. If hObj is an index handle, the resulting appended records will be in the current index order for the source handle. If hObj is a cursor handle, the resulting appended records will be a copy of the result set from the cursor. |
| hTableTo (I) | Handle of destination table or cursor to append records to. |
| usFilterOption (I) | Indicates if filters or scopes are to be respected (if any are set). This allows a subset of the source table to be appended to the destination table. Options cannot be bitwise ORed together because they are mutually exclusive. The options are:  ADS\_IGNOREFILTERS: Ignores any scopes or filters that are currently set.  ADS\_RESPECTSCOPES: Obeys scopes but not filters.  ADS\_RESPECTFILTERS: Obeys scopes AND filters. |

Remarks

AdsCopyTableContents only copies fields to the destination table that has matching names in the source table. A table cannot be copied onto itself. The current "show deleted records" setting, set via [AdsShowDeleted](ace_adsshowdeleted.htm), also affects what records are copied in DBF tables. If "show deleted" has been set to True, records marked for deletion will be copied in DBF tables. If "show deleted" has been set to False, records marked for deletion will not be copied. By default, the "show deleted" setting is True.

If performing an AdsCopyTableContents operation on an ADT table, and that ADT table contains an AutoIncrement field, the AutoIncrement values in records copied to the destination table will not necessarily be preserved. That is, the new records copied to the destination table are not guaranteed to have the same values in the AutoIncrement column as those records in the source table. Since the AdsCopyTableContents operation copies records to an existing table, it is possible that AutoIncrement values in the existing records in the destination table are identical to those in the source table. Since AutoIncrement values must be unique, the AutoIncrement values in the source table may not be preserved when they are copied to the destination table.

The copy will be done on the server if the following conditions are met:

|  |  |
| --- | --- |
| · | Both tables are on the same server and both tables are of the same type (e.g., both are opened with ADS\_CDX) |

|  |  |
| --- | --- |
| · | Neither table is opened exclusively |

|  |  |
| --- | --- |
| · | hObj is not a cursor |

|  |  |
| --- | --- |
| · | If hObj is an index, it isnt opened exclusively |

|  |  |
| --- | --- |
| · | The destination table does not have a file lock |

If the server fails to copy the data and the client succeeds, AdsCopyTableContents returns AE\_SUCCESS. The error that caused the copy to scale back from the server to the client is available by calling [AdsGetLastError](ace_adsgetlasterror.htm). The error codes that will be returned by AdsGetLastError if the copy is scaled back to the client will be one of the following:

|  |  |
| --- | --- |
| · | AE\_FILE\_NOT\_ON\_SERVER: The destination file was on another server. |

|  |  |
| --- | --- |
| · | AE\_INFO\_COPY\_MADE\_BY\_CLIENT:This error is returned in all other cases and contains specific information in the returned error buffer. |

Note This function is illegal in a transaction.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adscopytablecontentsexample)

See Also

[AdsCopyTable](ace_adscopytable.htm)

[AdsCopyTableStructure](ace_adscopytablestructure.htm)

[AdsConvertTable](ace_adsconverttable.htm)