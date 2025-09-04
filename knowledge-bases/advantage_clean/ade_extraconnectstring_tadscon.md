---
title: Ade Extraconnectstring Tadscon
slug: ade_extraconnectstring_tadscon
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_extraconnectstring_tadscon.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: dfd130fc7d94c338c500db263b7cc876b94d1d62
---

# Ade Extraconnectstring Tadscon

ExtraConnectString

TAdsConnection.ExtraConnectString

Advantage TDataSet Descendant

| TAdsConnection.ExtraConnectString  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

A supplemental connection string that, if specified, will be appended to the end of the automatically-generated connection string (that is built based on the other configured settings in the Connection component).  This provides a flexible way to specify additional settings that are not currently exposed as properties on the TAdsConnection component, like [DateFormat](ade_dateformat_tadsconnection.md), Decimals, ShowDeleted, and Connection Pooling options.

Syntax

property ExtraConnectString: String;

Description

Use ExtraConnectString to specify a set of additional connection string options that will be used when connecting.  See [AdsConnect101](ace_adsconnect101.md) help file topic for information on the connection string options that are available.

Remarks

The ExtraConnectString parameter allows a wide variety of options to be specified -- some of which are not directly related to making a connection.  Users wishing to avoid the use of the AdsSettings component should consider specifying connection-level options that will eliminate the need for the AdsSettings component.  (Specifically, the Decimals, ShowDeleted, and DateFormat properties of the connection string can replace the corresponding settings in the AdsSettings component.)

Example

ExtraConnectString := 'Epoch=2000;TableType=CDX;ShowDeleted=FALSE;DateFormat=DD/MM/YYYY;'

See Also

[AdsConnect101](ace_adsconnect101.md)

[TAdsSettings](ade_tadssettings_7.md)
