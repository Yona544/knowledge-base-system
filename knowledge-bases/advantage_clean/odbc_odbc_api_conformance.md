---
title: Odbc Odbc Api Conformance
slug: odbc_odbc_api_conformance
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_odbc_api_conformance.htm
source: Advantage CHM
tags:
  - odbc
checksum: 2d8ea01b503ad09a47809651d866c49d3135423e
---

# Odbc Odbc Api Conformance

ODBC API Conformance

ODBC API Conformance

Advantage ODBC Driver

| ODBC API Conformance  Advantage ODBC Driver |  |  |  |  |

This section describes the Advantage ODBC Driver API (Application Programming Interface). The ODBC API conforms to Microsofts ODBC SDK. This is not a replacement for Microsofts ODBC Programmers Reference and SDK Guide. Instead, it is a supplement to the reference guide to explain the nuances of the Advantage implementation.

This information is needed only if you are directly programming to the ODBC API. Otherwise, the information in the topic [Advantage ODBC Driver with SQL](odbc_advantage_odbc_driver_with_sql.md) should be adequate to access your data via the ODBC interface.

The Advantage ODBC Driver fully conforms to the ODBC version 2.0 specification for Core API and Level 1 API, and supports most of the Level 2 function calls. The following lists the ODBC API functions supported by the Advantage ODBC Driver.

Detail is provided for those APIs with potential differences in implementation compared to the Microsoft ODBC API definitions.

| ODBC Functions | Conformance Level |
| SQLAllocConnect | Core |
| SQLAllocHandle | Level 3 |
| SQLAllocEnv | Core |
| SQLAllocStmt | Core |
| SQLBindCol | Core |
| SQLBindParameter | Level 1 |
| SQLBulkOperations | Level 3 |
| SQLCancel | Core |
| SQLCloseCursor | Level 3 |
| SQLColAttribute | Level 3 |
| SQLColAttributes | Core |
| SQLColumns | Level 1 |
| SQLColumnPrivileges | Level 2 |
| SQLConnect | Core |
| SQLCopyDesc | Level 3 |
| SQLDataSources | Level 2 |
| SQLDescribeCol | Core |
| SQLDescribeParam | Level 2 |
| SQLDisconnect | Core |
| SQLDriverConnect | Level 1 |
| SQLDrivers | Level 2 |
| SQLEndTran | Level 3 |
| SQLError | Core |
| SQLExecDirect | Core |
| SQLExecute | Core |
| SQLFetch | Core |
| SQLFetchScroll | Level 3 |
| SQLFreeConnect | Core |
| SQLFreeEnv | Core |
| SQLFreeHandle | Level 3 |
| SQLFreeStmt | Core |
| SQLGetConnectAttr | Level 3 |
| SQLGetConnectOption | Level 1 |
| SQLGetCursorName | Core |
| SQLGetData | Level 1 |
| SQLGetDescField | Level 3 |
| SQLGetDescRec | Level 3 |
| SQLGetDiagField | Level 3 |
| SQLGetDiagRec | Level 3 |
| SQLGetEnvAttr | Level 3 |
| SQLGetFunctions | Level 1 |
| SQLGetInfo | Level 1 |
| SQLGetStmtAttr | Level 3 |
| SQLGetStmtOption | Level 1 |
| SQLGetTypeInfo | Level 1 |
| SQLMoreResults | Level 2 |
| SQLNativeSql | Level 2 |
| SQLNumResultCols | Core |
| SQLNumParams | Level 2 |
| SQLParamData | Level 1 |
| SQLPrepare | Core |
| SQLPutData | Level 1 |
| SQLRowCount | Core |
| SQLSetConnectAttr | Level 3 |
| SQLSetConnectOption | Level 1 |
| SQLSetCursorName | Core |
| SQLSetDescField | Level 3 |
| SQLSetDescRec | Level 3 |
| SQLSetEnvAttr | Level 3 |
| SQLSetStmtAttr | Level 3 |
| SQLSetStmtOption | Level 1 |
| SQLSpecialColumns | Level 1 |
| SQLStatistics | Level 1 |
| SQLTables | Level 1 |
| SQLTablePrivileges | Level 2 |
| SQLTransact | Core |
| SQLProcedures | Level 2 |
| SQLProcedureColumns | Level 2 |
