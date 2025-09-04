AdsExtendedReader.ConvertTable




Advantage Database Server 12  

AdsExtendedReader.ConvertTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ConvertTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ConvertTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_converttable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.ConvertTable / Dear Support Staff, |  |
| AdsExtendedReader.ConvertTable  Advantage .NET Data Provider |  |  |  |  |

Converts a table structure and associated records to a new table of a different type.

public void ConvertTable( FilterOption filtOpt, String strFile, TableType tableType );

Remarks

Converts a table structure and associated records to a new table of the given [TableType](dotnet_adsextendedreader_tabletype.htm). The new table will contain data types that are capable of storing the information, but the data types may change. For example, when converting from a DBF to an ADT, ADS\_NUMERIC fields are converted to ADS\_SHORTINT, ADS\_INTEGER, or ADS\_DOUBLE fields depending upon the size and decimals of the original numeric field.

Whenever conversions to DBF files are performed, the new DBF table will contain only standard DBF field types if possible. These data types include only ADS\_LOGICAL, ADS\_NUMERIC, ADS\_STRING, and ADS\_DATE.

The records copied to the new table depend on the option set by the given [FilterOption](dotnet_adsextendedreader_filteroption.htm).

Index files will not be copied as they can be created after the conversion. The resulting table must be opened by the application after the convert table operation is performed before the application can use the table. ConvertTable will not attempt to convert tables on the server; the client always performs this operation.

Note This function is illegal in a transaction.

See Also

[CopyTable](dotnet_adsextendedreader_copytable.htm)