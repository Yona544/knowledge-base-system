---
title: Master System Storedprocedures
slug: master_system_storedprocedures
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_storedprocedures.htm
source: Advantage CHM
tags:
  - master
checksum: 49056cd5afa29ca2a50892d19af0a428d1fec9b1
---

# Master System Storedprocedures

system.storedprocedures

system.storedprocedures

Advantage SQL Engine

| system.storedprocedures  Advantage SQL Engine |  |  |  |  |

Contains one row for each stored procedure in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Stored procedure name. |
| Proc\_Input | Memo | variable | Input parameters to the stored procedure in AdsCreateTable format. |
| Proc\_Output | Memo | variable | Output parameters for the stored procedure in AdsCreateTable format. |
| Proc\_DLL\_Name | Character | 260 | The name and path to the Advantage Extended Procedure file that contains the stored procedure, or the ProgID of the COM object for the Extended Procedure. |
| Proc\_DLL\_Function\_Name | Character | 200 | The name of the function that is called when the procedure is executed. |
| Comment | Memo | variable | The description of the stored procedure. |
| Proc\_Invoke\_Option | Integer | 4 | This property is for internal use, and specifies the type of procedure (DLL, COM object, .NET assembly, etc). The constant is based on the constants sent to the AdsDDAddProcedure ACE API in the ulInvokeOption parameter. |
| SQL\_Script | NMemo | Variable | Definition of the stored procedure if the stored procedure is an SQL script based stored procedure. |
