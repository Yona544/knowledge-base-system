---
title: Master Linux Rights Checking
slug: master_linux_rights_checking
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_linux_rights_checking.htm
source: Advantage CHM
tags:
  - master
checksum: e2d2dfdee2bf354a1b58b2d9aee8d6584d89393b
---

# Master Linux Rights Checking

Linux Rights Checking

Linux Rights Checking

Advantage Concepts

| Linux Rights Checking  Advantage Concepts |  |  |  |  |

Rights checking functionality can only work if the client machine is logged in to the server in a manor that allows the client direct access to server files. If using Samba or NFS to access files on a remote machine then rights checking will behave as expected. If simply accessing files on a local machine using a native path (/mydata/tables, for example) rights checking will behave as expected.

There are a few situations, however, in which rights checking must be disabled. An example is a Windows client connecting to an ADS for Linux server that is not running Samba. In this situation the client machine is not logged in to the Linux server, and hence, can not perform any rights checking. If you attempt to open a table with the Advantage Rights Checking option turned on you will receive an AE\_FILE\_NOT\_FOUND (5004) error.
