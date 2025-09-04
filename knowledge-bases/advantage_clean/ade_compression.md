---
title: Ade Compression
slug: ade_compression
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_compression.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ff66856ae195728636e7357c64472b817fc54a79
---

# Ade Compression

Compression

TAdsConnection.Compression

Advantage TDataSet Descendant

| TAdsConnection.Compression  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the compression setting for this connection. See [Communications Compression](master_communications_compression.md).

Syntax

TAdsCompressionTypes = ( ccAdsCompressionNotSet, ccAdsCompressInternet, ccAdsCompressAlways, ccAdsCompressNever );

 

property Compression: TAdsCompressionTypes;

Description

This property is ignored for stADS\_LOCAL connections. The Compression property can be set to one of the following values:

| Value | Meaning |
| ccAdsCompressionNotSet | (Default) This value indicates that the COMPRESSION setting in the ADS.INI file will be used if available. |
| ccAdsCompressInternet | If this option is specified, then all data communications for stADS\_AIS connections will be compressed unless compression is specifically turned off at the server. |
| ccAdsCompressAlways | If this option is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. |
| ccAdsCompressNever | If this option is specified, then compression will not be used for communications between the client and server. |
