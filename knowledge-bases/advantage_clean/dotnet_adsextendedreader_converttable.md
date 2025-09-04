---
title: Dotnet Adsextendedreader Converttable
slug: dotnet_adsextendedreader_converttable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_converttable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 63faa8fd261a8747d81dacb13ecb2f0240fbe0f6
---

# Dotnet Adsextendedreader Converttable

AdsExtendedReader.ConvertTable

AdsExtendedReader.ConvertTable

Advantage .NET Data Provider

| AdsExtendedReader.ConvertTable  Advantage .NET Data Provider |  |  |  |  |

Converts a table structure and associated records to a new table of a different type.

public void ConvertTable( FilterOption filtOpt, String strFile, TableType tableType );

Remarks

Converts a table structure and associated records to a new table of the given [TableType](dotnet_adsextendedreader_tabletype.md). The new table will contain data types that are capable of storing the information, but the data types may change. For example, when converting from a DBF to an ADT, ADS\_NUMERIC fields are converted to ADS\_SHORTINT, ADS\_INTEGER, or ADS\_DOUBLE fields depending upon the size and decimals of the original numeric field.

Whenever conversions to DBF files are performed, the new DBF table will contain only standard DBF field types if possible. These data types include only ADS\_LOGICAL, ADS\_NUMERIC, ADS\_STRING, and ADS\_DATE.

The records copied to the new table depend on the option set by the given [FilterOption](dotnet_adsextendedreader_filteroption.md).

Index files will not be copied as they can be created after the conversion. The resulting table must be opened by the application after the convert table operation is performed before the application can use the table. ConvertTable will not attempt to convert tables on the server; the client always performs this operation.

Note This function is illegal in a transaction.

See Also

[CopyTable](dotnet_adsextendedreader_copytable.md)
