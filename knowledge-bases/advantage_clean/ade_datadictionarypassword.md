---
title: Ade Datadictionarypassword
slug: ade_datadictionarypassword
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_datadictionarypassword.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3d25e3b518c189f8583e26b50e8e32e0966735a9
---

# Ade Datadictionarypassword

DataDictionaryPassword

TAdsConnection.EncryptionOptions.DataDictionaryPassword

Advantage TDataSet Descendant

| TAdsConnection.EncryptionOptions.DataDictionaryPassword  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the data dictionary password for a dictionary encrypted with AES.

Syntax

property EncryptionOptions.DataDictionaryPassword: String;

Description

Specifies the AES password for the dictionary if using [strong encryption](master_encryption.md). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.md) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed.
