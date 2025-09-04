---
title: Oledb Setting The Date Format
slug: oledb_setting_the_date_format
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_setting_the_date_format.htm
source: Advantage CHM
tags:
  - oledb
checksum: bf481016e7a0fc098f6de7ccb8f21950152a7cd5
---

# Oledb Setting The Date Format

Setting the Date Format

Setting the Date Format

Advantage OLE DB Provider (for ADO)

| Setting the Date Format  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Developers can control the date format used by date literals in Advantage record filter expressions, index expressions, and SQL expressions within an Advantage OLE DB Provider application. ADO has no "date format" property, so developers can't change the Advantage default date format via an ADO property. But, the Advantage Client Engine APIs AdsSetDateFormat and AdsSetDateFormat60 can be used to change the Advantage date format. AdsSetDateFormat sets a global date format that affects the behavior of dates throughout a program. AdsSetDateFormat60 sets a date format for a specific connection and only affects the behavior of dates for tables and cursors open on that connection. The default date format is "MM/DD/YYYY" for record filter expressions and index expression and can be either "MM/DD/YYYY" or "YYYY-MM-DD" for SQL date literals.

Dim cn As ADODB.Connection

Set cn = New ADODB.Connection

cn.Provider = "Advantage.OLEDB.1"

cn.Properties.Item("Data Source") = "\\server\volume\path"

cn.Open

 

' This works because one of the default date formats is 'YYYY-MM-DD'

rs1.Open "SELECT \* FROM customers WHERE doh > '1990-12-25'", cn, adOpenDynamic, adLockOptimistic, adCmdText

 

' This works because one of the default date formats is 'MM/DD/YYYY'

rs2.Open "SELECT \* FROM customers WHERE doh > '12/25/1990'", cn, adOpenDynamic, adLockOptimistic, adCmdText

 

' This gets the ACE connection handle

lHandle = cn.Properties.Item( "ACE Connection handle" )

 

' This sets the date format to 'YYYY.DD.MM' for all tables/cursors opened for the cn connection

lResult = AdsSetDateFormat60( lHandle, 'YYYY.DD.MM' )

rs3.Open "SELECT \* FROM customers WHERE doh > '1990.25.12'", cn, adOpenDynamic, adLockOptimistic, adCmdText
