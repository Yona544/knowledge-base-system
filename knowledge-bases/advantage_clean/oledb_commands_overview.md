---
title: Oledb Commands Overview
slug: oledb_commands_overview
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_commands_overview.htm
source: Advantage CHM
tags:
  - oledb
checksum: 0af447b6dc152cb14be239762057a514a01e314c
---

# Oledb Commands Overview

Commands Overview

Commands Overview

Advantage OLE DB Provider (for ADO)

| Commands Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider exposes the necessary interfaces to provide native SQL support. The following discussion provides an overview of the Command architecture with relation to the Advantage Client Engine and the Advantage Database Server.

When an SQL statement is executed on an OLE DB Command object, the provider uses the Advantage Client Engine to perform the necessary processing and communications with the Advantage Database Server. The provider uses SQL statement handles obtained through the Advantage Client Engine to execute an SQL statement. Each Command object may contain one or more statement handles, and the OLE DB consumer never manipulates these statement handles directly. Normally, a given Command object uses a single statement handle, but the provider may create multiple statement handles if the consumer requests multiple rowsets at the same time from a single command object. If recordsets are not left open, then when successive SQL statements are issued on the same command object, each one will re-use the existing statement handle. Command objects do not share statement handles with other Command objects.

When an SQL statement is executed, the Advantage Database Server maintains the execution plan for the statement until the statement is closed or until a new statement is executed. This means that any tables referenced by the statement are kept open as well. One of the implications of this is that another Command object will not be able to open the same tables exclusively (or vice versa) until another statement is run on the first Command object or until the first Command object is closed.

When a Command object is closed, all statement handles owned by that Command object are also closed. Note, though, that the tables opened by the statement may be left open due to cursor caching performed at the Advantage Database Server. To turn off cursor caching, an application must use the Advantage Client Engine API directly and call AdsCacheOpenCursors. Alternatively, the AdsCloseCachedTables API can be used to close all cached tables without modifying the current AdsCacheOpenCursors setting.

During transactions, the Advantage Database Server holds all locks obtained during the transaction until the transaction is ended. A given lock belongs to a specific table instance on the server. This means that if an update is made to a record in one Command object in a transaction, it will not be possible to update that same record in a different Command object within the same transaction. Each Command object will be using different statement handles and, thus, different table instances on the server. As an example, consider the following sequence of operations using ADO (cn represents an ADODB.Connection object, cmd represents an ADODB.Command object and rs represents an ADODB.Recordset object):

 

cn.BeginTrans

cmd.CommandText = "update ..."

cmd.Execute

cmd.CommandText = "select ..."

Set rs = cmd.Execute

cmd.CommandText = "update ..."

cmd.Execute

cn.CommitTrans

 

The first Execute call executes the UPDATE statement. The second Execute (for the SELECT) ends up using the same OLE DB Command object as the first statement and creates a recordset. With the third Execute, ADO actually creates a new OLE DB Command object because the recordset from the second Execute is still open. This ends up causing the OLE DB provider to create a new SQL statement handle, which will not use the same table instance as the first UPDATE statement. If the UPDATE statement attempts to update the same record (or records) as the first UPDATE statement, then one or more lock failures will occur.

To avoid this, the application should close the recordset (rs.Close) prior to the third Execute statement (the second UPDATE). ADO will then use the same OLE DB command object and, thus, the same Advantage statement handle. Alternatively, an application can use separate Command objects for the SELECT and UPDATE statements.
