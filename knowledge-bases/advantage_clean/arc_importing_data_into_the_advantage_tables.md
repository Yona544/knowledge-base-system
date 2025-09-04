---
title: Arc Importing Data Into The Advantage Tables
slug: arc_importing_data_into_the_advantage_tables
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_importing_data_into_the_advantage_tables.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 9934e32a509a2067769c57208a24af586ef6aa3e
---

# Arc Importing Data Into The Advantage Tables

Importing Data into the Advantage Tables

Importing Data into Advantage Tables

Advantage Data Architect

| Importing Data into Advantage Tables  Advantage Data Architect |  |  |  |  |

Use the ARC Import Utility to move data (both schema and content) into Advantage Database Table (ADT) format. To start the ARC Import Utility, select Tools | Import Data from the main menu.

The following types of tables can be directly imported using ARC:

- Paradox\dBase Tables

- Advantage FoxPro Tables

- Advantage CA-Clipper Tables

- Text Files

Data may also be imported from the following data sources:

- Any BDE alias

- Any ADO data source

To import data:

| 1. | Select the type of data to import. |

| 2. | Input the location of the data by directory or data source. |

| 3. | Input the location for the new Advantage data. |

| 4. | Import the data. |

Considerations when Importing Data Into the ADT File Format

To use a Borland Database Engine (BDE) alias, the BDE must be installed on the machine.

To use an ADO data source, the following items must be installed on the machine: Microsoft ADO 2.1 or greater, and an OLEDB or an ODBC driver for access to the data to be imported. The latest Microsoft ADO driver can be downloaded from the Microsoft Web site (search for MDAC in the downloads area).
