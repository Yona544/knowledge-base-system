---
title: Dotnet Adsextendedreader Locktable
slug: dotnet_adsextendedreader_locktable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_locktable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0e0bfc24cd3512a5f2cd58ae029f578c0e9694c0
---

# Dotnet Adsextendedreader Locktable

AdsExtendedReader.LockTable

AdsExtendedReader.LockTable

Advantage .NET Data Provider

| AdsExtendedReader.LockTable  Advantage .NET Data Provider |  |  |  |  |

Attempts to lock the table.

public void LockTable();

Remarks

A successful call to LockTable prevents other applications from being able to update the table. It is recommended that you lock tables prior to creating indexes. Any record locks that have been obtained prior to calling LockTable will be released. If the Advantage Client Engine fails to lock the table (e.g., if another user has record locks), then the Advantage Client Engine does not attempt to relock the records that it released.

Note This API only works with tables. The use of cursors with this API is illegal and will result in an exception.

See Also

[LockTable](dotnet_adsextendedreader_locktable.md)

[UnlockTable](dotnet_adsextendedreader_unlocktable.md)

[IsTableLocked](dotnet_adsextendedreader_istablelocked.md)
