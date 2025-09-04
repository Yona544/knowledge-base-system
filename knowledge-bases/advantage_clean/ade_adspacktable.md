---
title: Ade Adspacktable
slug: ade_adspacktable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adspacktable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3ca4c618058eadf16fb5a14da8bc94532142b083
---

# Ade Adspacktable

AdsPackTable

TAdsTable.AdsPackTable

Advantage TDataSet Descendant

| TAdsTable.AdsPackTable  Advantage TDataSet Descendant |  |  |  |  |

Removes deleted records from the given table and re-indexes the table.

Syntax

procedure AdsPackTable;

Description

AdsPackTable removes all deleted records from this table instance. Internal fragmentation in memo files will also be eliminated. The table is then re-indexed. If a progress callback function is available, it will be called during the reindexing. The indexes must be opened during the pack or they will become logically invalid. This operation requires exclusive access to the table, which is specified during the open.

Note that if encryption was ever enabled on the table, the table cannot be packed unless the encryption is enabled with the correct password.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsPackTable;

See Also

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md)

[AdsZapTable](ade_adszaptable.md)

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsDecryptTable](ade_adsdecrypttable.md)
