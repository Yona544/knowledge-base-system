---
title: Devguide Connecting To Data 2
slug: devguide_connecting_to_data_2
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_connecting_to_data_2.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: dc6ecd7d5197c041ee1dcda6dc50c11452897413
---

# Devguide Connecting To Data 2

Connecting to Data

     Connecting to Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You connect to a data dictionary or a directory in which free tables are located using a Connection object found in the ADODB namespace. At a minimum, you must provide the Connection object with sufficient information to locate your data and configure how the data should be accessed. This can be done either with the Parameters collection property or the ConnectionString property. Both of these properties accept name/value pairs using the parameters listed in Table 17-1. If you use the ConnectionString property, and use more than one name/value pair, separate them with semicolons.

 

| Parameter | Description |
| CharType | Set to the character set type for DBF files. Valid values are ADS\_ANSI and ADS\_OEM. The default value is ADS\_ANSI. |
| Compression | Set to ALWAYS, INTERNET, NEVER, or empty. If left empty (the default), the ADS.INI file will control the compression setting. This parameter is not used by ALS. |
| CommType | The communication protocol to use to connect to ADS. Under Windows and Linux, the default is UDP\_IP. To use TCP/IP, set CommType to TCP\_IP. To use IPX, set CommType to IPX. |
| Data Source | The path to your free tables or data dictionary. If you are using a data dictionary, you must include the data dictionary filename in this path. It is recommended that this path be a UNC path. Data Source is a required parameter. |
| DbfsUseNulls | Set to TRUE to return empty fields from DBF files as NULL values. If set to FALSE, empty fields are returned as empty data values. The default is FALSE. |
| EncryptionPassword | Set to an optional password to use for accessing encrypted free tables. If using less than a 20-letter password, a semicolon should be included directly after the password so the Advantage OLE DB Provider knows when the password ends. This parameter is ignored for data dictionary connections. |

Table 17-1: ADO Connection String Parameters
