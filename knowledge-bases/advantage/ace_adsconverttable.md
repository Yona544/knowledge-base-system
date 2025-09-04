AdsConvertTable




Advantage Database Server 12  

AdsConvertTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConvertTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsConvertTable Advantage Client Engine ace\_Adsconverttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsConvertTable  Advantage Client Engine |  |  |  |  |

Converts a table structure and associated records to a new table of a different type.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsConvertTable (ADSHANDLE hObj,  UNSIGNED16 usFilterOption,  UNSIGNED8 \*pucFile,  UNSIGNED16 usTableType); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, index handle, or cursor to convert. If hObj is a table handle, the resulting table will be in natural order. If hObj is an index handle, the resulting table will be in the current index order for that handle. If hObj is a cursor handle, the resulting table will be a copy of the result set from the cursor. |
| usFilterOption (I) | Indicates if filters or scopes are to be respected (if any are set). This allows a subset of the source table to be appended to the destination table. Options cannot be bitwise ORd together because they are mutually exclusive. The options are:  ADS\_IGNOREFILTERS: Ignores any scopes or filters that are currently set.  ADS\_RESPECTSCOPES: Obeys scopes but not filters.  ADS\_RESPECTFILTERS: Obeys scopes AND filters. |
| pucFile (I) | Name of the file to create, which must include the full path of the destination table. |
| usTableType (I) | Type of table to create. Valid options are ADS\_CDX, ADS\_NTX, ADS\_VFP, and ADS\_ADT |

Remarks

Converts a table structure and associated records to a new table of a different type. The new table will contain data types that are capable of storing the information, but the field size may change. For example, when converting from a DBF to an ADT, ADS\_NUMERIC fields, field size will be increase by one because the ADT numeric field type reserves one byte for the sign of the values stored in the field. If the new field size cannot be supported by the Advantage Database Server, an error will be returned.

Whenever conversions to DBF files are performed, the new DBF table will contain only standard DBF field types if possible. These data types include only ADS\_LOGICAL, ADS\_NUMERIC, ADS\_STRING, and ADS\_DATE.

When converting to a VFP table with this API, long field names will not be preserved. The resulting table from this API is a free table, and a data dictionary is required to store long field names for VFP tables. If the source table is in a data dictionary and has long field names, then the resulting DBF will have names shortened to 10 characters.

The records copied to the new table depend on the option set in usFilterOption. The current "show deleted records" setting, set via [AdsShowDeleted](ace_adsshowdeleted.htm), also affects what records are copied in DBF tables. If "show deleted" has been set to True, records marked for deletion will be copied in DBF tables. If "show deleted" has been set to False, records marked for deletion will not be copied. By default, the "show deleted" setting is True.

Index files will not be copied as they can be created after the conversion. The resulting table must be opened by the application after the convert table operation is performed before the application can use the table. AdsConvertTable will not attempt to convert tables on the server; the client always performs this operation.

Note This function is illegal in a transaction.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_more_examples.htm#adsconverttableexample)

See Also

[AdsCopyTable](ace_adscopytable.htm)

[AdsCopyTableContents](ace_adscopytablecontents.htm)

[AdsCopyTableStructure](ace_adscopytablestructure.htm)