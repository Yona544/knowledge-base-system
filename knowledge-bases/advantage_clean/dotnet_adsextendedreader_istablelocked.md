---
title: Dotnet Adsextendedreader Istablelocked
slug: dotnet_adsextendedreader_istablelocked
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_istablelocked.htm
source: Advantage CHM
tags:
  - dotnet
checksum: be96b2bfce4d852ce92ef47c155acef2e97b0a70
---

# Dotnet Adsextendedreader Istablelocked

AdsExtendedReader.IsTableLocked

AdsExtendedReader.IsTableLocked

Advantage .NET Data Provider

| AdsExtendedReader.IsTableLocked  Advantage .NET Data Provider |  |  |  |  |

Tests if the table is locked by the current user.

public bool IsTableLocked();

Remarks

IsTableLocked can be used to test if the table is locked by the current user. If the table is locked by another user or by the current user with a different reader, IsTableLocked will return false.

See Also

[LockTable](dotnet_adsextendedreader_locktable.md)

[UnlockTable](dotnet_adsextendedreader_unlocktable.md)
