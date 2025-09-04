---
title: Odbc Packet Compression
slug: odbc_packet_compression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_packet_compression.htm
source: Advantage CHM
tags:
  - odbc
checksum: a683135484df09e601602ea4cb6aee64ad076968
---

# Odbc Packet Compression

Packet Compression

Packet Compression

| Packet Compression |  |  |  |  |

This setting controls the option for communications compression (see Advantage.hlp for more information.) If INTERNET is specified, then all data communications for ADS\_AIS\_SERVER connections will be compressed unless compression is specifically turned off at the server. If ALWAYS is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. If NEVER is specified, then compression will not be used for communications between the client and server. If this entry is not specified or is left empty, then the COMPRESSION setting in the ADS.INI file will be used if available. This entry is ignored for ADS\_LOCAL\_SERVER connections.
