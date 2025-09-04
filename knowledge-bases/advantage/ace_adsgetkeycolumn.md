AdsGetKeyColumn




Advantage Database Server 12  

AdsGetKeyColumn

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetKeyColumn  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetKeyColumn Advantage Client Engine ace\_Adsgetkeycolumn Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetKeyColumn  Advantage Client Engine |  |  |  |  |

Retrieves key column information for a given table or cursor handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetKeyColumn (ADSHANDLE hCursor,  UNSIGNED8 \*pucKeyColumn,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hCursor (I) | Handle of table or cursor. |
| pucKeyColumn (O) | Return the key column information. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetKeyColmun is used to retrieve key column information about a cursor or table. Key column information is defined as any column name in the cursor or table that has unique attributes. AdsGetKeyColumn will search for column names in the following order:

|  |  |
| --- | --- |
| · | Primary Key |

|  |  |
| --- | --- |
| · | Unique Index |

|  |  |
| --- | --- |
| · | Autoinc |

|  |  |
| --- | --- |
| · | Rowversion (tables and live cursors only) |

After calling AdsGetKeyColumn the return buffer will consist of a semicolon delimited string containing the names of the most unique columns. AdsGetKeyColumn will only return the most unique column names, (i.e., an autoinc column will not be returned if a primary key column is found.) Furthermore, partial key columns will not be returned. In other words, if a column in a cursor is part of a primary or unique index, it will not be returned unless all columns involved in that index are in the cursor as well. For primary key columns, all column names included in the primary key will be returned. For unique indexes, every column name included in each unique tag will be returned.

Note Some column names may be found multiple times in the return string if they are involved in multiple unique index tags.