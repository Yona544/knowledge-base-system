---
title: Vo Ax Setsqltimeout
slug: vo_ax_setsqltimeout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_setsqltimeout.htm
source: Advantage CHM
tags:
  - vo
checksum: b70d5fcbf8d5bc9601d9615ecdb357b8d9efa061
---

# Vo Ax Setsqltimeout

AX\_SetSQLTimeout()

AX\_SetSQLTimeout()

Advantage SQL RDDs

| AX\_SetSQLTimeout()  Advantage SQL RDDs |  |  |  |  |

Syntax

AX\_SetSQLTimeout( AS DWORD )

Returns

The previous SQL Timeout setting.

Description

This function specifies the SQL Timeout setting to use when executing SQL Statements and working with resulting cursors. By default, no timeout is used and SQL operations will be allowed to execute indefinitely. When a timeout value is specified, any query whose execution exceeds the timeout value will be cancelled, and an error 7209 (SQL query aborted by user) is returned to the client.

NOTE: This function is only valid for use with the Advantage SQL RDDs (AXSQLNTX, AXSQLCDX, AXSQLVFP, and AXSQLADT).

See also

[AdsSetSQLTimeout](ace_adssetsqltimeout.md)
