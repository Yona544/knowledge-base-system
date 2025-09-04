---
title: Vo Axsql Parameters
slug: vo_axsql_parameters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_axsql_parameters.htm
source: Advantage CHM
tags:
  - vo
checksum: 7f102d05cadbd28e75f43df9e7a45cf2bd450916
---

# Vo Axsql Parameters

AXSQL Parameter Support

AXSQL Parameter Support

Advantage AXSQL RDDs

| AXSQL Parameter Support  Advantage AXSQL RDDs |  |  |  |  |

The AdsSQLServer class supports SQL parameters in the constructor (init) and [Refresh](vo_axsql_refresh_functionality.md) methods.  Read more about parameters in SQL statements [here](devguide_parameters_in_sql_statements.md) and [here](ace_parameters_in_sql_statements.md).  Parameters in VO are passed in using key-value arrays.  The first argument is the parameter name (key) and the second argument is the parameter value.  For example:

{{ "Lastname", "Smith" }}

Multiple parameters can be passed in like so:

{{"Lastname", "Smith"}, {"CustomerID", 100 }}

The AdsSQLServer class supports both named and unnamed parameters.  Unnamed parameters are placed in the SQL query using a question mark (?) and then set using numbers based on their position in the query.  For example:

oServer := AdsSQLServer{ "SELECT \* FROM customers WHERE Lastname = ? and Firstname = ?", , , "AXSQLADT", , {{ 1, "Coles" }, {2, "Becky" }}}

or

oServer:Refresh({{ 1, "Coles" }, {2, "Jenny" }} )
