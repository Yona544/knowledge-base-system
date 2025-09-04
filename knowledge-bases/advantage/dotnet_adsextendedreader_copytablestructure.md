AdsExtendedReader.CopyTableStructure




Advantage Database Server 12  

AdsExtendedReader.CopyTableStructure

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.CopyTableStructure  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.CopyTableStructure Advantage .NET Data Provider dotnet\_Adsextendedreader\_copytablestructure Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.CopyTableStructure / Dear Support Staff, |  |
| AdsExtendedReader.CopyTableStructure  Advantage .NET Data Provider |  |  |  |  |

Creates a new table with the given name having the same structure as the table opened with this reader.

public void CopyTableStructure( String strFile );

Remarks

The table created does not contain records, but has field structure identical to the original table. Indexes are not copied by CopyTableStructure. The resulting table must be opened by the application after the copy is performed before the application can use the table.

See Also

[CopyTable](dotnet_adsextendedreader_copytable.htm)

[ConvertTable](dotnet_adsextendedreader_converttable.htm)