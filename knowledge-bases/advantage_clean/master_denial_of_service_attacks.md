---
title: Master Denial Of Service Attacks
slug: master_denial_of_service_attacks
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_denial_of_service_attacks.htm
source: Advantage CHM
tags:
  - master
checksum: d486302182e7111e207ea412f492cf46040eab78
---

# Master Denial Of Service Attacks

Denial of Service Attacks

Denial of Service Attacks

Advantage Database Server

| Denial of Service Attacks  Advantage Database Server |  |  |  |  |

Advantage Database Server provides the capability to monitor the number of partial Internet logins. The server will allow a maximum number of attempted Internet logins, it will stop all further Internet connection requests until some of the partial Internet connections are cleared out by the watchdog thread. The purpose of this is to keep a Denial of Service attack from stopping users on the local network from connecting to the Advantage Database Server.

By default the maximum number or partial logins is 1/3 of the user license with a ceiling of 100 and a floor of 3.

Connection Errors

Internet connection errors will be logged in the ADS\_ERR.ADT or ADS\_ERR.DBF file. You can look at this file to see the incorrect logins.
