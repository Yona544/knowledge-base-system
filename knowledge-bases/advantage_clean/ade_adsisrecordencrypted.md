---
title: Ade Adsisrecordencrypted
slug: ade_adsisrecordencrypted
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisrecordencrypted.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6a2c907214a973eb85a1841dff61f775e72fe96c
---

# Ade Adsisrecordencrypted

AdsIsRecordEncrypted

TAdsTable/TAdsQuery.AdsIsRecordEncrypted

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsIsRecordEncrypted  Advantage TDataSet Descendant |  |  |  |  |

Returns the encrypted status of the current record.

Syntax

function AdsIsRecordEncrypted (ulRecNum : Longint) : boolean;

Parameter

| ulRecNum | Physical record number to check if encrypted, or 0 for active record. |

Description

AdsIsRecordEncrypted will return True if the given record is encrypted. It will return False if the record is not encrypted.

Example

AdsTable1.FindKey( [Smith] );

if ( AdsTable1.AdsIsRecordEncrypted( 0 ) ) then

AdsTable1.AdsEnableEncryption( 'secret' );

 

See Also

[AdsDisableEncryption](ade_adsdisableencryption.md)

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsDecryptRecord](ade_adsdecryptrecord.md)

[AdsEncryptRecord](ade_adsencryptrecord.md)
