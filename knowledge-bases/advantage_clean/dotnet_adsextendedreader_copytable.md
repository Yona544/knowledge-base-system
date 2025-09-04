---
title: Dotnet Adsextendedreader Copytable
slug: dotnet_adsextendedreader_copytable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_copytable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: eb6253b5d8c90d1cc338d898df7f3ec32f29678e
---

# Dotnet Adsextendedreader Copytable

AdsExtendedReader.CopyTable

AdsExtendedReader.CopyTable

Advantage .NET Data Provider

| AdsExtendedReader.CopyTable  Advantage .NET Data Provider |  |  |  |  |

Copies a table structure and associated records to a new table.

public void CopyTable( FilterOption filtOpt, String strFile );

Remarks

The records copied to the new table depend on the FilterOption given.

Index files will not be copied, as they can be created after the copy. The resulting table must be opened by the application after the copy is performed before the application can use the table.

If performing a CopyTable on an ADT table, and that ADT table contains an AutoIncrement field, the AutoIncrement values will be preserved in the destination table. That is, the new records in the destination table will have the same values in the AutoIncrement column as those records in the source table. The next available AutoIncrement value will also be identical in the source and destination tables.

The copy will be done on the server if the following conditions are met:

- strFile is on the same server as the file referenced by hObj

- the data reader is not open on a cursor

- the table was not opened exclusively

If the server cannot perform the copy, the client will attempt the copy operation.

When the server copy fails but the client copy succeeds, CopyTable will fire an InfoMessage event (see [AdsConnection.InfoMessage](dotnet_adsconnection_infomessage.md)) with the information on why the copy could not take place on the server.

If strFile does not include a path, the current working directory will be used.

 

Note Static cursors are always in the ADT format. If you pass this function a static cursor, the resulting file will be in ADT format as well. Live cursors will maintain their file format in the new file. Specifically, when CopyTable is called with static cursors from DBF tables, the resulting table will be an ADT. When CopyTable is called with live cursors created from DBF tables, the resulting table will be a DBF. To convert to another file format use ConvertTable.

 

Note CopyTable is illegal in a transaction.

See Also

[CopyTableStructure](dotnet_adsextendedreader_copytablestructure.md)

[ConvertTable](dotnet_adsextendedreader_converttable.md)
