AdsCopyTable




Advantage Database Server 12  

AdsCopyTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCopyTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCopyTable Advantage Client Engine ace\_Adscopytable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCopyTable  Advantage Client Engine |  |  |  |  |

Copies a table structure and associated records to a new table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCopyTable (ADSHANDLE hObj,  UNSIGNED16 usFilterOption,  UNSIGNED8 \*pucFile); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, index handle, or cursor to copy. If hObj is a table handle, the resulting table will be in natural order. If hObj is an index handle, the resulting table will be in the current index order for that handle. If hObj is a cursor handle, the resulting table will be a copy of the result set from the cursor. |
| usFilterOption (I) | Indicates if filters or scopes are to be respected (if any are set). This allows a subset of the source table to be copied to the destination table. Options cannot be bitwise ORed together because they are mutually exclusive. The options are:  ADS\_IGNOREFILTERS: Ignores any scopes or filters that are currently set.  ADS\_RESPECTSCOPES: Obeys scopes but not filters.  ADS\_RESPECTFILTERS: Obeys scopes AND filters. |
| pucFile (I) | Name of the file to create, which must include the full path of the destination table. |

Remarks

The records copied to the new table depend on the option set in usFilterOption. The current "show deleted records" setting, set via [AdsShowDeleted](ace_adsshowdeleted.htm), also affects what records are copied in DBF tables. If "show deleted" has been set to True, records marked for deletion will be copied in DBF tables. If "show deleted" has been set to False, records marked for deletion will not be copied. By default, the "show deleted" setting is True.

Index files will not be copied, as they can be created after the copy. The resulting table must be opened by the application after the copy command is performed before the application can use the table.

If performing an AdsCopyTable operation on an ADT table, and that ADT table contains an AutoIncrement field, the AutoIncrement values will be preserved in the destination table. That is, the new records in the destination table will have the same values in the AutoIncrement column as those records in the source table. The next available AutoIncrement value will also be identical in the source and destination tables.

When copying a VFP table with this API, long field names will not be preserved. The resulting table from this API is a free table, and a data dictionary is required to store long field names for VFP tables. If the source table is in a data dictionary and has long field names, then the resulting DBF will have names shortened to 10 characters.

The copy will be done on the server if the following conditions are met:

|  |  |
| --- | --- |
| · | pucFile is on the same server as the file referenced by hObj |

|  |  |
| --- | --- |
| · | hObj is not a cursor |

|  |  |
| --- | --- |
| · | hObj is not a table or index handle that is opened exclusively |

If the server cannot perform the copy, the client will attempt the copy operation.

When the server copy fails but the client copy succeeds, AdsCopyTable returns AE\_SUCCESS. The error that caused the copy to scale back from the server to the client is available by calling [AdsGetLastError](ace_adsgetlasterror.htm). The error codes that will be returned by AdsGetLastError if the copy is scaled back to the client will be one of the following:

|  |  |
| --- | --- |
| · | AE\_FILE\_NOT\_ON\_SERVERThe destination file was on another server. |

|  |  |
| --- | --- |
| · | AE\_INFO\_COPY\_MADE\_BY\_CLIENTThis error is returned in all other cases and contains specific information in the returned error buffer. |

If the table name provided does not include a path, the current working directory will be used. A "default" search path can be specified using the [AdsSetDefault](ace_adssetdefault.htm) API. It is recommend you always pass a path, however.

Note Static cursors are always in the ADT format. If you pass this function a static cursor, the resulting file will be in ADT format as well. Live cursors will maintain their file format in the new file. Specifically, when AdsCopyTable is called with static cursors from DBF tables, the resulting table will be an ADT. When AdsCopyTable is called with live cursors created from DBF tables, the resulting table will be a DBF. To convert to another file format use [AdsConvertTable](ace_adsconverttable.htm).

 

Note AdsCopyTable is illegal in a transaction.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adscopytableexample)

See Also

[AdsCopyTableContents](ace_adscopytablecontents.htm)

[AdsCopyTableStructure](ace_adscopytablestructure.htm)

[AdsConvertTable](ace_adsconverttable.htm)