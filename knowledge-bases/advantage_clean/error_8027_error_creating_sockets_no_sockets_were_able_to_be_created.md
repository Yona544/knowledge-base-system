---
title: Error 8027 Error Creating Sockets No Sockets Were Able To Be Created
slug: error_8027_error_creating_sockets_no_sockets_were_able_to_be_created
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8027_error_creating_sockets_no_sockets_were_able_to_be_created.htm
source: Advantage CHM
tags:
  - error
checksum: d35fe4612a25c23c30ec941fe9848c220696c684
---

# Error 8027 Error Creating Sockets No Sockets Were Able To Be Created

8027 Error creating sockets. No sockets were able to be created

8027 Error creating sockets. No sockets were able to be created

Advantage Error Guide

| 8027 Error creating sockets. No sockets were able to be created  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to create any sockets for communications. Advantage Database Server on Windows or Linux will continue to run and allow direct inter-process communications with clients running on the same physical machine as the server. It will not be able to accept connections from clients running on remote machines.

Solution: Verify that a networking protocol (TCP/IP or IPX) is installed and enabled on the server. If a LAN\_IP\_ADDRESS or INTERNET\_IP\_ADDRESS is specified in the Advantage Database Server configuration, verify that it is correct.
