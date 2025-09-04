---
title: Master Setting Up Your Clients Using Ads Ini
slug: master_setting_up_your_clients_using_ads_ini
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_setting_up_your_clients_using_ads_ini.htm
source: Advantage CHM
tags:
  - master
checksum: b278a017ff8aed5633d4959685d2c7eb02b02fe4
---

# Master Setting Up Your Clients Using Ads Ini

Setting Up Your Clients Using ADS.INI

Setting Up Your Clients Using ADS.INI

Advantage Database Server

| Setting Up Your Clients Using ADS.INI  Advantage Database Server |  |  |  |  |

The Advantage Internet Server configuration can be specified in the ADS.INI file by adding a couple of sections.

The [Drives] section lists the complete UNC path to which a drive letter is mapped. If your client application uses drive letters, you will need to define the drive letter mappings.

Example:

[ Drives ]

R:=\\SERVER1\SHARE

For each Advantage Database Server you want to connect to, you will need to have a separate server-name entry.

Example:

[ <server name> ]

INTERNET\_PORT=<the Internet port for the server>

INTERNET\_IP=<the IP address for the Advantage Database Server>

Example:

[Drives]

Q:=\\serverA\testsys\

r:=\\serverB\data\

[serverA]

INTERNET\_PORT=2001

INTERNET\_IP=198.169.1.69

[serverB]

INTERNET\_PORT=2002

INTERNET\_IP=198.70.169.72
