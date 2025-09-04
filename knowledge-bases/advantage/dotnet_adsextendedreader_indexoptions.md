AdsExtendedReader.IndexOptions




Advantage Database Server 12  

AdsExtendedReader.IndexOptions

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.IndexOptions  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.IndexOptions Advantage .NET Data Provider dotnet\_Adsextendedreader\_indexoptions Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Enumerations > AdsExtendedReader.IndexOptions / Dear Support Staff, |  |
| AdsExtendedReader.IndexOptions  Advantage .NET Data Provider |  |  |  |  |

public enum IndexOptions

Remarks

IndexOptions may be used with [CreateIndex](dotnet_adsextendedreader_createindex.htm) to define the options for index creation. A bitwise combination of these values may be used.

|  |  |
| --- | --- |
| Member Name | Description |
| Default | Use if no options are needed. |
| Unique | Create a unique index order. |
| Candidate | This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as the ADS\_UNIQUE option. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships. |
| Compound | Create an index order (tag) within a compound index file. Note that this option is always set when the table type is TableType.ADT. |
| Descending | Create a descending index order. |
| Binary | Create a [binary index](master_binary_indexes.htm). The index expression must have a logical result. This option cannot be combined with other options except for Compound. |

See Also

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[TableType](dotnet_adsextendedreader_tabletype.htm)