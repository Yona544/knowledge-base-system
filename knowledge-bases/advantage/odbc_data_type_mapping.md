Data Type Mapping




Advantage Database Server 12  

Data Type Mapping

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Type Mapping  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Data Type Mapping Advantage ODBC Driver odbc\_Data\_type\_mapping Advantage ODBC Driver > Using the Advantage ODBC Driver with SQL > Data Type Mapping / Dear Support Staff, |  |
| Data Type Mapping  Advantage ODBC Driver |  |  |  |  |

In result sets and as parameter values, the Advantage ODBC Driver represents the Advantage data by using the following ODBC defined data types, reported in the functions SQLColAttribute, SQLColumns, SQLDescribeCol, SQLGetTypeInfo, and SQLSpecialColumns.

|  |  |
| --- | --- |
| Advantage Data Type | ODBC Data Type |
| ShortInt | SQL\_SMALLINT |
| Integer | SQL\_INTEGER |
| LongInt | SQL\_BIGINT |
| Double | SQL\_DOUBLE |
| CurDouble | SQL\_DOUBLE |
| Logical | SQL\_BIT |
| AutoIncrement | SQL\_INTEGER |
| Binary | SQL\_LONGVARBINARY |
| Image | SQL\_LONGVARBINARY |
| Raw | SQL\_BINARY |
| Character | SQL\_CHAR |
| CICharacter | SQL\_CHAR |
| Memo | SQL\_LONGVARCHAR |
| NChar | SQL\_WCHAR |
| NVarChar | SQL\_WVARCHAR |
| NMemo | SQL\_WLONGVARCHAR |
| Numeric | SQL\_NUMERIC |
| Date | SQL\_DATE |
| ShortDate | SQL\_DATE |
| Time | SQL\_TIME |
| TimeStamp | SQL\_TIMESTAMP |
| Money | SQL\_NUMERIC |
| RowVersion | SQL\_NUMERIC |
| ModTime | SQL\_TIMESTAMP |
| VarChar | SQL\_VARCHAR |
| VarBinary | SQL\_VARBINARY |
| GUID | SQL\_GUID |