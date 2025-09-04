---
title: Master Transactions Exist Per Connection
slug: master_transactions_exist_per_connection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_transactions_exist_per_connection.htm
source: Advantage CHM
tags:
  - master
checksum: 41dcc738e01fcdad24184e9b88a60129ec432b5f
---

# Master Transactions Exist Per Connection

Transactions Exist Per Connection

Transactions Exist Per Connection

Advantage Concepts

| Transactions Exist Per Connection  Advantage Concepts |  |  |  |  |

Transactions exist on a per connection basis. A single transaction involving files opened on different connections is not supported, but an application can have separate transactions that involve tables opened on different connections since the application can have multiple connections.

Advantage Client Engine-based clients (Advantage TDataSet Descendant, Advantage OLE DB Provider, Advantage ODBC Driver, Advantage CA-Visual Objects RDD, Advantage Client Engine API, etc.) can have multiple connections on one or more file servers. The connection upon which a transaction exists is either the connection object for which the "begin transaction" method is called, or the connection handle used in the "begin transaction" API (with the Advantage Client Engine API). If you wish some tables used by your application to be part of a transaction and other tables to not be part of that transaction, open two Advantage connections, open the "transaction" table on one connection and the "non-transaction" tables on the other connection, and then begin the transaction on the one connection only.

Advantage CA-Clipper applications can have only one connection per file server. Therefore, transactions exist per file server for Advantage CA-Clipper applications. The file server on which a transaction exists is the one with the active work area when the begin transaction statement is issued. For example, if \\SERVER1\VOL1:FILE1.DBF is opened in the current work area, and a begin transaction statement is issued, then the transaction exists on SERVER1 and for any tables that are located on SERVER1.
