AdsCopyTableStructure




Advantage Database Server 12  

AdsCopyTableStructure

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCopyTableStructure  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCopyTableStructure Advantage Client Engine ace\_Adscopytablestructure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCopyTableStructure  Advantage Client Engine |  |  |  |  |

Creates a new table with the same structure as the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCopyTableStructure (ADSHANDLE hTable,  UNSIGNED8 \*pucFile); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor to copy. |
| pucFile (I) | Name of file to create. |

Remarks

The table created does not contain records, but has field structure identical to the original table. Indexes are not copied by AdsCopyTableStructure. The empty table must be opened by a call to [AdsOpenTable](ace_adsopentable.htm) to be manipulated.

When copying a VFP table structure with this API, long field names will not be preserved. The resulting table from this API is a free table, and a data dictionary is required to store long field names for VFP tables. If the source table is in a data dictionary and has long field names, then the resulting DBF will have names shortened to 10 characters.

Examples

[Click Here](ace_examples.htm#adscopytablestructureexample)

See Also

[AdsCopyTable](ace_adscopytable.htm)

[AdsCopyTableContents](ace_adscopytablecontents.htm)

[AdsConvertTable](ace_adsconverttable.htm)