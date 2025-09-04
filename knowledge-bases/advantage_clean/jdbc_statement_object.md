---
title: Jdbc Statement Object
slug: jdbc_statement_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_statement_object.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 4b717009fa8c781f8948aafa520553aa574f245c
---

# Jdbc Statement Object

Statement Object

Statement Object

Advantage JDBC Driver

| Statement Object  Advantage JDBC Driver |  |  |  |  |

| Methods | Version Introduced | Supported | Comments |
| void addBatch (String) | 2.0 Core | Yes |  |
| void cancel () | 1.0 | Yes |  |
| void clearBatch () | 2.0 Core | Yes |  |
| void clearWarnings () | 1.0 | Yes |  |
| void close () | 1.0 | Yes |  |
| boolean execute (String) | 1.0 | Yes |  |
| int [] executeBatch () | 2.0 Core | Yes |  |
| ResultSet executeQuery (String) | 1.0 | Yes |  |
| int executeUpdate (String) | 1.0 | Yes |  |
| Connection getConnection () | 2.0 Core | Yes |  |
| int getFetchDirection () | 2.0 Core | Yes |  |
| int getFetchSize () | 2.0 Core | Yes |  |
| int getMaxFieldSize () | 1.0 | Yes |  |
| int getMaxRows () | 1.0 | Yes |  |
| boolean getMoreResults () | 1.0 | Yes |  |
| int getQueryTimeout () | 1.0 | Yes |  |
| ResultSet getResultSet () | 1.0 | Yes |  |
| int getResultSetConcurrency () | 2.0 Core | Yes |  |
| int getResultSetType () | 2.0 Core | Yes |  |
| int getUpdateCount () | 1.0 | Yes |  |
| SQLWarning getWarnings () | 1.0 | Yes |  |
| void setCursorName (String) | 1.0 | No | Throws "feature not supported" exception. |
| void setEscapeProcessing (boolean) | 1.0 | Yes | Ignored. |
| void setFetchDirection (int) | 2.0 Core | Yes |  |
| void setFetchSize (int) | 2.0 Core | Yes |  |
| void setMaxFieldSize (int) | 1.0 | Yes |  |
| void setMaxRows (int) | 1.0 | Yes |  |
| void setQueryTimeout (int) | 1.0 | Yes |  |
