---
title: Dotnet Adsextendedreader Setrange
slug: dotnet_adsextendedreader_setrange
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_setrange.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c15ea97716d78f47d06104eef66c8eb3b5fcb763
---

# Dotnet Adsextendedreader Setrange

AdsExtendedReader.SetRange

AdsExtendedReader.SetRange

Advantage .NET Data Provider

| AdsExtendedReader.SetRange  Advantage .NET Data Provider |  |  |  |  |

Set the top and/or bottom range values for an index order.

public void SetRange( object[] topRange, object[] bottomRange );

Remarks

SetRange sets a range (sometimes called scope) for the active index to limit the number of records visible. For example, setting a topRange of "M" on an index on a character field will make a GotoTop call go to the first key greater than or equal to "M". The bottomRange will make the indicated value the last one visible in the index order. For example, if bottomRange is "Smith" on a lastname index, the last "Smith" on a GotoBottom call will be the current record. Set the top and bottom range to the same value to view only those records with the given range value from the index.

It is not necessary to have both top and bottom ranges set at the same time. Setting either to null will clear an existing top or bottom range. [ClearRange](dotnet_adsextendedreader_clearrange.md) will clear both top and bottom range values.

Advantage does not check whether the top and bottom range values are mutually exclusive. When setting ranges on descending indexes, the top range will be set at the logical top of the index (largest key) and the bottom range is at the logical bottom (smallest key).

Note If both a narrow range and a narrow filter (narrow meaning that very few records match the range or filter conditions) are being used on the same table, poor performance may result. Since knowledge of ranges is only on the client, and filters are handled on the server, the filtering of records on the server may unnecessarily traverse well beyond the bounds of a range, causing poor performance. If this condition is expected, it is recommended to use either a range or a filter, but not both.

After calling this method, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.

See Also

[Filter](dotnet_adsextendedreader_filter.md)

[ClearRange](dotnet_adsextendedreader_clearrange.md)
