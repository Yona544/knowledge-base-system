---
title: Oledb Command Syntax
slug: oledb_command_syntax
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_command_syntax.htm
source: Advantage CHM
tags:
  - oledb
checksum: 48ecfdff5fa83def83fa5711ca0893e19e4f9cc3
---

# Oledb Command Syntax

Command Syntax

Command Syntax

Advantage OLE DB Provider (for ADO)

| Command Syntax  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider recognizes command syntax specified by the DBGUID\_SQL macro. For the Advantage OLE DB Provider, the specifier indicates that an amalgam of ODBC SQL and SQL-92 is valid syntax. For example, the following SQL statement uses an ODBC SQL escape sequence to specify the LCASE string function:

 

SELECT customerid={fn LCASE( CustomerID )} FROM Customers

 

LCASE returns a character string, converting all uppercase characters to their lowercase equivalents. The SQL-92 string function LOWER performs the same operation, so the following SQL statement is an SQL-92 equivalent to the ODBC statement presented above:

 

SELECT customerid=LOWER( CustomerID ) FROM Customers

 

The Advantage OLE DB Provider processes either form of the statement successfully when specified as text for a command.
