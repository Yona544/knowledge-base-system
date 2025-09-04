---
title: Master Iota Table
slug: master_iota_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_iota_table.htm
source: Advantage CHM
tags:
  - master
checksum: c3bb544c974ef501aa5f910c1acdc4054fda18b2
---

# Master Iota Table

IOTA Table

IOTA Table

Advantage SQL Engine

| IOTA Table  Advantage SQL Engine |  |  |  |  |

The Advantage SQL engine has a virtual system table named IOTA. The IOTA is a table with one logical (SQL\_BIT) column named "iota" and it has a single row in the table with NULL value in the "iota" column. The main purpose of the IOTA table is to provide an efficient method for evaluating an SQL expression on the server. Some sample uses of the IOTA table (note the use of the dot notation to reference the IOTA table in the System catalog):

To get the current date and time on the server:

SELECT Now() FROM System.IOTA

To test how LCASE scalar function transforms a string:

SELECT LCase( 'Sample String' ) FROM System.IOTA

To initialize the random number generator on the server with a new seed value for current user:

SELECT Rand( 2 ) FROM System.IOTA
