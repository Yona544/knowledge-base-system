---
title: Devguide Tcp Ip Support For All Clients
slug: devguide_tcp_ip_support_for_all_clients
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_tcp_ip_support_for_all_clients.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 4071856a6117967d3aac0048359b5ad871b7b254
---

# Devguide Tcp Ip Support For All Clients

TCP/IP Support for All Clients

     TCP/IP Support for All Clients

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| TCP/IP Support for All Clients  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Prior to Advantage 8, most communication between an Advantage client and ADS used UDP (user datagram protocol) over IP. Only the class 4 Java driver used TCP (transmission control protocol).

Advantage 8.1 now supports TCP for all client communications. The support for TCP is particularly valuable for those applications where it is not possible to open a UDP port in firewalls between the client and server.

Note, however, that Advantage's proprietary technology using UDP is exceptionally efficient compared to the more bandwidth-intensive TCP standard. As a result, performance using UDP is superior to that using TCP, making UDP the preferred protocol for Advantage communications.

 

In the next chapter you will learn about the various table types supported by Advantage.
