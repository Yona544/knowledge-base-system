---
title: Dotnet Adsextendedreader Gototop
slug: dotnet_adsextendedreader_gototop
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_gototop.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0df9dda0da08460710e326c2e32cab7c97117b83
---

# Dotnet Adsextendedreader Gototop

AdsExtendedReader.GotoTop

AdsExtendedReader.GotoTop

Advantage .NET Data Provider

| AdsExtendedReader.GotoTop  Advantage .NET Data Provider |  |  |  |  |

Sets the table position to the first record

public void GotoTop();

Remarks

If the current handle is a table or cursor, the table (or cursor) is positioned at the top of its natural order. The record on which it positions is the first record starting from record 1 (one) that satisfies current filter conditions. If the handle passed is an index order handle, the table is positioned at the top of the current logical order, obeying current filter and range.

See Also

[GotoBottom](dotnet_adsextendedreader_gotobottom.md)

[RecordNumber](dotnet_adsextendedreader_recordnumber.md)

[SetRange](dotnet_adsextendedreader_setrange.md)

[Filter](dotnet_adsextendedreader_filter.md)
