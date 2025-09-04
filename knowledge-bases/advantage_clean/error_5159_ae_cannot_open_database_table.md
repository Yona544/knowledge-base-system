---
title: Error 5159 Ae Cannot Open Database Table
slug: error_5159_ae_cannot_open_database_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5159_ae_cannot_open_database_table.htm
source: Advantage CHM
tags:
  - error
checksum: 8a05b657ff266550b84a076cbae75c55bff7755a
---

# Error 5159 Ae Cannot Open Database Table

5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE

5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE

Advantage Error Guide

| 5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE  Advantage Error Guide |  |  |  |  |

Problem: An error was encountered when trying to open a database table. This error can occur when attempting to open a database table) as a free table).

Solution for Advantage Client Engine API: When opening a database table using the Advantage Client Engine API, make sure ADS\_DEFAULT is specified as the table type. When opening a free table with the Advantage Client Engine API, the table type must be ADS\_ADT, ADS\_CDX, ADS\_VFP, or ADS\_NTX.

Solution for Advantage TDataSet Descendant: When opening a database table using the Advantage TDataSet Descendant, make sure to specify the full path to the Advantage Data Dictionary .ADD file in the TAdsConnection.ConnectPath property (for example, "x:\data\sampledd.add").

Solution for Advantage OLE DB Provider (for ADO): When opening a database table using the Advantage OLE DB Provider (for ADO), make sure to specify the full path to the Advantage Data Dictionary .ADD file for the Data Source key word in the ADO connection string (for example, "Data Source=x:\data\sampledd.add").

Solution for Advantage ODBC Driver: When opening a database table using the Advantage ODBC Driver, make sure to check the "Data Dictionary" check box and to specify the full path to the Advantage Data Dictionary .ADD file for the "Database or Data Dictionary Path" edit in the Data Source Setup Screen (for example, "x:\data\sampledd.add").
