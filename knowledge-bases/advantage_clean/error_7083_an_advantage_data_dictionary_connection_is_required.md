---
title: Error 7083 An Advantage Data Dictionary Connection Is Required
slug: error_7083_an_advantage_data_dictionary_connection_is_required
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7083_an_advantage_data_dictionary_connection_is_required.htm
source: Advantage CHM
tags:
  - error
checksum: 1f56aed8625d3ede0641442f507cfbcf91e205f5
---

# Error 7083 An Advantage Data Dictionary Connection Is Required

7083 An Advantage Data Dictionary connection is required

7083 An Advantage Data Dictionary connection is required

Advantage Error Guide

| 7083 An Advantage Data Dictionary connection is required  Advantage Error Guide |  |  |  |  |

Problem 1: When connecting to the Advantage Database Server through an Internet connection, a 7083 error is returned and the connection fails.

Solution 1: The Advantage Data Dictionary contains user names, passwords, and other necessary information required for a secure connection over the Internet. All Internet connections require an Advantage Data Dictionary connection. In the connection path, specify the full path and file name of the Advantage Data Dictionary.

 

Problem 2: When connecting to the Advantage Database Server with a non-Internet connection, a 7083 error is returned and the connection fails. This error will occur if the Advantage Database Server has been configured to disallow free connections.

Solution 2: In the connection path, specify the full path and file name of the Advantage Data Dictionary, or turn off the DISABLE\_FREE\_CONNECTIONS configuration parameter.

 

Problem 3: Advantage Database Server failed to get a connection to the target database to perform a replication update. If this occurs, the error class will be 7600.

Solution 3: An Advantage Data Dictionary is required for performing replication updates. Edit the subscription and verify that the target database is a valid Advantage data dictionary.
