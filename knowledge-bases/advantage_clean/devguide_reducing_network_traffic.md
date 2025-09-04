---
title: Devguide Reducing Network Traffic
slug: devguide_reducing_network_traffic
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_reducing_network_traffic.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 141044bef45bd5934065f492f9d47c8fcfa548d9
---

# Devguide Reducing Network Traffic

Reducing Network Traffic

     Reducing Network Traffic

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Reducing Network Traffic  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Local Server is not a database server. With file-serverbased systems, all data processing is performed on the individual workstations. For example, to select all records from a customer table for customers in a particular city, the entire customer table index must be transferred across the network to the workstation, which then finds the record based on the index locally. The located records are then retrieved from the file server.

The problem is worse if an appropriate index does not exist for the table. In that case, the entire table must be transmitted across the network.

While this overhead is negligible if the customer table includes several dozen records, the strain that it places on the network increases with the size of the table. For example, selecting the hundred or so records for customers from Des Moines, Iowa, from a million-record table requires that the entire index for all one million records be transmitted across the network.

The problem is particularly bad when you consider that the network load increases in direct proportion to the number of people who are using the application simultaneously. Every single client needs to read indexes and tables across the network in order to get work done.

By comparison, Advantage Database Server performs its processing on the server on which it is installed, which is typically the machine on which the shared data files are located. There is no need to copy entire indexes or tables across the network when the client application is interested in only a few records. Specifically, in a client/server environment, the client requests the records that it needs, and the server uses the indexes and tables to locate the needed data. Once the data is identified, that data, and only that data, is transmitted across the network to the client.
