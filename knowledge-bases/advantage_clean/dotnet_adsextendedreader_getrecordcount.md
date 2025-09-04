---
title: Dotnet Adsextendedreader Getrecordcount
slug: dotnet_adsextendedreader_getrecordcount
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_getrecordcount.htm
source: Advantage CHM
tags:
  - dotnet
checksum: f7dd1a78a3b6affd5dd75c924d7671219f991d95
---

# Dotnet Adsextendedreader Getrecordcount

AdsExtendedReader.GetRecordCount

AdsExtendedReader.GetRecordCount

Advantage .NET Data Provider

| AdsExtendedReader.GetRecordCount  Advantage .NET Data Provider |  |  |  |  |

Retrieves the total number of records in a table or number of keys in an index.

public int GetRecordCount( FilterOption eOption );

public int GetRecordCount( FilterOption eOption, bool bRefreshCount );

Remarks

If eOption is AdsExtendedReader.FilterOption.IgnoreFilters, this function will return the total number of records in the current table or cursor.

If eOption is AdsExtendedReader.FilterOption.RespectScopes, this function will return the total number of records within the current range (scope).

If eOption is AdsExtendedReader.FilterOption.RespectFilters, ranges and filters are obeyed, and this function returns the count of all records in the current range passing the current Filter.

If bRefreshCount is true, the count will be recalculated. This may be necessary when it is known that other applications are appending records to the table and a more accurate count is needed. Note that if other applications are appending records to a table, there is no guarantee that the record count will be accurate because another application may append a record immediately after the record count is retrieved. To guarantee an accurate count, an application must have opened the table exclusively or locked the table.

See Also

[FilterOption](dotnet_adsextendedreader_filteroption.md)

[LockTable](dotnet_adsextendedreader_locktable.md)

[SetRange](dotnet_adsextendedreader_setrange.md)
