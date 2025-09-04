---
title: Odbc Driver Boundaries
slug: odbc_driver_boundaries
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_driver_boundaries.htm
source: Advantage CHM
tags:
  - odbc
checksum: 6ab814306da8c4f3be0ef7537c3472fafdb725da
---

# Odbc Driver Boundaries

Driver Boundaries

Driver Boundaries

Advantage ODBC Driver

| Driver Boundaries  Advantage ODBC Driver |  |  |  |  |

The Advantage ODBC Driver has defined limits for the data size and the manner in which you reference the data. The Advantage Database Server and the ODBC driver interface determine these boundaries. The following boundaries apply to the Advantage ODBC Driver:

| Description | Amount |
| Number of Rows | 2 billion |
| Number of Database Connections | Determined by Memory |
| Number of Statements per Connection | Determined by Memory |
| Table Name Length (File Name) | 255 characters |
| Column Name Length | 10 characters for DBF, 128 characters for ADT tables and Visual FoxPro tables in data dictionaries |
| Table Qualifier (Path) | 255 characters |
| Number of Index Files per Table | 15 |
| Number of Tags per CDX/ADI Index File | 50 |
| Number of Joined Tables | Determined by Memory |
| Largest Memo Field | 4 gigabytes |
| Largest Binary Field | 4 gigabytes |
| Largest Record Size | 64K |
