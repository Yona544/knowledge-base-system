---
title: Error 5226 Query Logging Error
slug: error_5226_query_logging_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5226_query_logging_error.htm
source: Advantage CHM
tags:
  - error
checksum: 43dfa889efc170d25e74a71ae0c3422a822e9078
---

# Error 5226 Query Logging Error

error\_5226\_query\_logging\_error

5226 Query Logging Error

Advantage Error Guide

| 5226 Query Logging Error  Advantage Error Guide |  |  |  |  |

An operation involving query logging failed.  The error text associated with this error should contain additional information on identifying the problem.

Problem:  Query Logging is already enabled on this database.

Solution:  Query logging can only be enabled once per dictionary or once for all free table connections.  Details regarding the running query log job can be found using the [sp\_ViewQueryLogging](master_sp_viewquerylogging.md) system stored procedure.

Problem:  Schema is not compatible with the current query logging table.

Solution:  If using an existing query logging table, ensure the schema of the table matches the schema required by query logging. Note, the schema may change between major versions of Advantage.

Problem:  Query Logging is not enabled on this database.

Solution:  Ensure that query logging is enabled prior to calling the [sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.md) system procedure.
