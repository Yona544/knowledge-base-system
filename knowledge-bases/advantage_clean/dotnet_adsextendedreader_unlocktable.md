---
title: Dotnet Adsextendedreader Unlocktable
slug: dotnet_adsextendedreader_unlocktable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_unlocktable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: adaa42700118345589db69247066358655d4ef73
---

# Dotnet Adsextendedreader Unlocktable

AdsExtendedReader.UnlockTable

AdsExtendedReader.UnlockTable

Advantage .NET Data Provider

| AdsExtendedReader.UnlockTable  Advantage .NET Data Provider |  |  |  |  |

Releases all locks on the given table

public void UnlockTable();

Remarks

AdsUnlockTable releases either all record locks on the table, or a table lock if one exists. If record locks are held and the table is in a transaction, the record locks will be released at the end of the transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error.

See Also

[LockRecord](dotnet_adsextendedreader_lockrecord.md)

[LockTable](dotnet_adsextendedreader_locktable.md)

[IsTableLocked](dotnet_adsextendedreader_istablelocked.md)

[UnlockRecord](dotnet_adsextendedreader_unlockrecord.md)
