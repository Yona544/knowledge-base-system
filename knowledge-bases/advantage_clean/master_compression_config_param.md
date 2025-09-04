---
title: Master Compression Config Param
slug: master_compression_config_param
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_compression_config_param.htm
source: Advantage CHM
tags:
  - master
checksum: 6c2d016b87b4c362eab3c4a73e1b9b1e74755d24
---

# Master Compression Config Param

Compression

Compression

Advantage Database Server

| Compression  Advantage Database Server |  |  |  |  |

Default = Internet

Valid values include:

InternetUse compression for ADS\_AIS\_SERVER (Internet) connections.

AlwaysUse compression unless the client specifically turns it off.

NeverDo not allow compression for any connections. This setting overrides any client compression settings.

This value controls whether or not compression is used for communications between client and server. In general, it makes sense to use compression when the network is the bottleneck (e.g., connections through a 56K modem). See [Communications Compression](master_communications_compression.md) for more information.
