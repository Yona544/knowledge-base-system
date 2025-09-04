---
title: Ade Dataencryptiontype
slug: ade_dataencryptiontype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_dataencryptiontype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 39083d9c48bbc03ba5bfb14d8d3b9cb2a15d428b
---

# Ade Dataencryptiontype

DataEncryptionType

TAdsConnection.EncryptionOptions.DataEncryptionType

Advantage TDataSet Descendant

| TAdsConnection.EncryptionOptions.DataEncryptionType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the encryption type to use on this connection.

Syntax

property EncryptionOptions.DataEncryptionType: TAdsDataEncryptionType;

 

TAdsDataEncryptionType = ( etAdsDefault, etAdsAES128, etAdsAES256, etAdsRC4 );

Description

Specifies the encryption type to use when [encrypting tables](master_encryption.md).  A newly encrypted table will be encrypted with this encryption type.  A newly created data dictionary on this connection will use the specified encryption type. When opening an existing table or data dictionary that is encrypted, this connection option is ignored and the appropriate encryption type is used. To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1.
