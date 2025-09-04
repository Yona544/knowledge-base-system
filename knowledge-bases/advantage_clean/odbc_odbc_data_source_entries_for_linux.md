---
title: Odbc Odbc Data Source Entries For Linux
slug: odbc_odbc_data_source_entries_for_linux
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_odbc_data_source_entries_for_linux.htm
source: Advantage CHM
tags:
  - odbc
checksum: f8d90205f61f40de3bd64eb1a1138735da039d6d
---

# Odbc Odbc Data Source Entries For Linux

ODBC Data Source Entries for Linux

ODBC Data Source Entries for Linux

Advantage ODBC Driver

| ODBC Data Source Entries for Linux  Advantage ODBC Driver |  |  |  |  |

ODBC data source entries are used by the Advantage ODBC Driver to determine certain driver behaviors and Advantage settings are stored in the odbc.ini file. The odbc.ini file must be located in the directory specified by an environment variable named ODBCINI, in the users home directory, or in the /etc directory. If located in the user home directory the odbc.ini should be named .odbc.ini (note the initial "dot"). For a list of required entries, as well as the list of optional entries and their default values see [ODBC Data Source Keys](odbc_odbc_data_source_keys.md). All entries in the odbc.ini file are string values.

An example odbc.ini file is shown below:

;

; odbc.ini

;

[ODBC Data Sources]

Odie = Advantage ODBC Driver

 

[Odie]

Driver=/home/odbcuser/lib/libadsodbc.so.6

DataDirectory=\\AdvantageServer\data\w78p1\

Description=Advantage ODBC driver

Rows=False

MemoBlockSize=64

DefaultType=Advantage

MaxTableCloseCache=0

LOCKING=Record

CharSet=OEM

ADVANTAGELOCKING=OFF

ServerTypes=2

TableExtension=
