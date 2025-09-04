---
title: Odbc Odbc Driver Sql Grammar
slug: odbc_odbc_driver_sql_grammar
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_odbc_driver_sql_grammar.htm
source: Advantage CHM
tags:
  - odbc
checksum: 9534355f9c67ed47b35758df96328fa36bbac797
---

# Odbc Odbc Driver Sql Grammar

ODBC Driver SQL Grammar

ODBC Driver SQL Grammar

Advantage ODBC Driver

| ODBC Driver SQL Grammar  Advantage ODBC Driver |  |  |  |  |

The Advantage ODBC Driver supports three levels of SQL grammars: Minimum, Core and Extended. Each higher level provides more fully implemented data definition and data manipulation language support.

The following chart outlines the SQL Grammar support with the Advantage ODBC Driver. See [Advantage SQL Engine](master_advantage_sql_engine.md) for more information.

| SQL Grammar | SQL Grammar Support |
| [ALTER TABLE](master_alter_table.md) | Extended |
| [BEGIN TRANSACTION](master_begin_transaction.md) | Extended |
| [COMMIT WORK](master_commit_work.md) | Extended |
| [CREATE DATABASE](master_create_database.md) | Extended |
| [CREATE INDEX](master_create_index.md) | Core |
| [CREATE PROCEDURE](master_create_procedure.md) | Extended |
| [CREATE TABLE](master_create_table.md) | Minimum |
| [CREATE TRIGGER](master_create_trigger.md) | Extended |
| [CREATE VIEW](master_create_view.md) | Extended |
| [DELETE](master_delete.md) (searched) | Minimum |
| [DROP INDEX](master_drop_index.md) | Core |
| [DROP PROCEDURE](master_drop_procedure.md) | Extended |
| [DROP TABLE](master_drop_table.md) | Minimum |
| [DROP TRIGGER](master_drop_trigger.md) | Extended |
| [DROP VIEW](master_drop_view.md) | Extended |
| [EXECUTE PROCEDURE](master_execute_procedure.md) \* | Extended |
| [GRANT](master_grant.md) | Core |
| [INSERT](master_insert.md) | Minimum |
| [REVOKE](master_revoke.md) | Core |
| [ROLLBACK WORK](master_rollback_work.md) | Extended |
| [SELECT](master_select.md) | Minimum |
| - approximate numeric literal | Core |
| - BETWEEN predicate | Core |
| - correlation name | Core |
| - date arithmetic | Extended |
| - date literal | Extended |
| - exact numeric literal | Core |
| - IN predicate | Core |
| - set function | Core |
| - time literal | Extended |
| - timestamp literal | Extended |
| [SET TRANSACTION](master_set_transaction.md) | Extended |
| Subqueries | Core |
| Unions | Extended |
| [UPDATE](master_update.md) | Minimum |

\* This statement is an extension to the ODBC SQL grammar.
