Data Type Mapping in Rowsets and Parameters




Advantage Database Server 12  

Data Type Mapping in Rowsets and Parameters

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Type Mapping in Rowsets and Parameters  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Data Type Mapping in Rowsets and Parameters Advantage OLE DB Provider (for ADO) oledb\_Data\_type\_mapping\_in\_rowsets\_and\_parameters Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Data Types > Data Type Mapping in Rowsets and Parameters / Dear Support Staff, |  |
| Data Type Mapping in Rowsets and Parameters  Advantage OLE DB Provider (for ADO) |  |  |  |  |

In rowsets and as parameter values, the Advantage OLE DB Provider represents the Advantage Database Server data by using the following OLE DB defined data types, reported in the functions IColumnsInfo::GetColumnInfo and ICommandWithParameters::GetParameterInfo.

|  |  |
| --- | --- |
| Advantage Database Server  Data Type | Advantage OLE DB Provider  Data Type |
| ShortInt | DBTYPE\_I2 |
| Integer | DBTYPE\_I4 |
| LongInt | DBTYPE\_I8 |
| Double | DBTYPE\_R8 |
| CurDouble | DBTYPE\_R8 |
| Logical | DBTYPE\_BOOL |
| AutoIncrement | DBTYPE\_UI4 |
| Binary | DBTYPE\_BYTES |
| Image | DBTYPE\_BYTES |
| Raw | DBTYPE\_BYTES |
| GUID | DBTYPE\_GUID |
| Character | DBTYPE\_STR |
| CICharacter | DBTYPE\_STR |
| Memo | DBTYPE\_STR |
| NChar | DBTYPE\_WSTR |
| NVarChar | DBTYPE\_WSTR |
| NMemo | DBTYPE\_WSTR |
| Numeric | DBTYPE\_NUMERIC |
| Date | DBTYPE\_DBDATE |
| ShortDate | DBTYPE\_DBDATE |
| Time | DBTYPE\_DBTIME |
| TimeStamp | DBTYPE\_DBTIMESTAMP |
| Money | DBTYPE\_CY |
| RowVersion | DBTYPE\_UI8 |
| ModTime | DBTYPE\_DBTIMESTAMP |

The Advantage OLE DB Provider supports conversion to and from most data types. For detailed information about the availability of type conversions on a command or on a rowset, call IConvertType::CanConvert.

The Advantage OLE DB Provider only supports converting to ByRef data types if the destination type is a variable-length data type such as DBTYPE\_BYTES, DBTYPE\_STR, DBTYPE\_VARNUMERIC, or DBTYPE\_WSTR.