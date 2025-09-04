---
title: Error 6425 An Advantage Data Dictionary Connection Is Required For Internet Connections
slug: error_6425_an_advantage_data_dictionary_connection_is_required_for_internet_connections
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6425_an_advantage_data_dictionary_connection_is_required_for_internet_connections.htm
source: Advantage CHM
tags:
  - error
checksum: 5f4f78a075aaacea0b9647ff833bd16c5482f947
---

# Error 6425 An Advantage Data Dictionary Connection Is Required For Internet Connections

6425 An Advantage Data Dictionary connection is required for Internet connections

6425 An Advantage Data Dictionary connection is required for Internet connections

Advantage Error Guide

| 6425 An Advantage Data Dictionary connection is required for Internet connections  Advantage Error Guide |  |  |  |  |

Problem: When connecting to the Advantage Database Server through an Internet connection, a 6425 error occurs.

Solution: The Advantage Data Dictionary contains user names, passwords, and other needed information required for a secure connection over the Internet. All Internet connections require an Advantage Data Dictionary connection.

In the connection path, specify the full path and file name of the Advantage Data Dictionary.

If you are trying to connect using the Advantage Management Utility, it will not work because Internet connections through this utility have not been implemented. The code for the Advantage Management Utility can be modified to use an Internet-enabled Advantage Data Dictionary connection instead of a management connection. (See AdsConnect60() for details on obtaining an Internet Advantage Data Dictionary Connection.)
