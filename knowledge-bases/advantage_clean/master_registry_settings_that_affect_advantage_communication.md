---
title: Master Registry Settings That Affect Advantage Communication
slug: master_registry_settings_that_affect_advantage_communication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_registry_settings_that_affect_advantage_communication.htm
source: Advantage CHM
tags:
  - master
checksum: c547283c21026729c09471f5d8da43d3c81912b1
---

# Master Registry Settings That Affect Advantage Communication

Registry Settings that affect Advantage Communication

Registry Settings that affect Advantage Communication

Advantage Concepts

| Registry Settings that affect Advantage Communication  Advantage Concepts |  |  |  |  |

The following settings will force specific communication behavior between the Advantage clients and the Advantage Database Server. The settings were specifically written for testing of the communication layer. In a few cases, these settings have been useful in solving customer issues. Care should be taken in using these settings since they limit the discovery methods and/or protocols available to the communication libraries. Only one setting may be used at a time. Setting multiple settings to non-zero values may cause unexpected communication behavior. All settings are type DWORDs located in \\HKEY\_LOCAL\_MACHINE\Software\Extended Systems\Advantage Communications. Most likely, the "Advantage Communications" key will not exist so you will need to create it. If no settings are used, mailslots, multicast and SAPs are used to "discover" the Advantage Database Server. Preference will be given to the IP or IPX protocol depending on the DEFAULT PROTOCOL setting in the [ads.ini file](master_ads_ini_file_support.md) and protocol availability.

IPX SAP ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via Service Advertising Protocol (SAP) packets only. When this setting is non-zero, mailslot and multicast packets are NOT used to locate the Advantage Database Server. A server with a bindery or a machine with bindery emulation on the current network is required. Only the IPX protocol will be used to communicate to the server. If the IPX protocol is not available, Advantage communication will fail. This registry setting will be ignored when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.

MAILSLOT ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via mailslot packets only. When this setting is non-zero, SAP and multicast packets are NOT used to locate the Advantage Database Server. Preference will be given to the IP or IPX protocol depending on the DEFAULT PROTOCOL setting and protocol availability. This registry setting will be ignored when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.

IP MULTICAST ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via multicast packets only. When this setting is non-zero, SAP and mailslot packets are NOT used to locate the Advantage Database Server. Preference will be given to the IP or IPX protocol depending on the DEFAULT PROTOCOL setting in the ADS.INI file and protocol availability. This registry setting will be ignored when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.

IP ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via mailslots and multicast packets only. SAP (Service Advertising Protocol) packets will not be used. Only the IP protocol will be used to communicate to the server. If the IP protocol is not available, Advantage communication will fail. This registry setting will be ignored when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.

IPX ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via multicast, mailslots, and SAP packets. Once discovery occurs, only the IPX protocol is used to communicate to the server. If IPX protocol is not available, Advantage communication will fail. If this setting is a non-zero value, all communication to the Advantage Database Server to fail when used when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.

IP ECHO ONLY = 1 --> Setting this value to a non-zero will cause discovery of the Advantage Database Server via mailslots and multicast packets (SAP packets are not used). The Advantage client sends an echo packet from each IP address on the client to each IP address returned in the discovery packet from the Advantage Database Server. When the Advantage Database Server responds to an echo packet, the client will use the set of IP addresses that produced the echo response from the server. This method of finding a valid IP address will normally only occur when a valid IP server address from the current network is not found. This registry setting will be ignored when the LAN\_IP/LAN\_PORT settings in the [ads.ini file](master_ads_ini_file_support.md) are being used.
