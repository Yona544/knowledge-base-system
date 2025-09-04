ODBC Driver SQL Grammar




Advantage Database Server 12  

ODBC Driver SQL Grammar

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ODBC Driver SQL Grammar  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - ODBC Driver SQL Grammar Advantage ODBC Driver odbc\_Odbc\_driver\_sql\_grammar Advantage ODBC Driver > Using the Advantage ODBC Driver with SQL > ODBC Driver SQL Grammar / Dear Support Staff, |  |
| ODBC Driver SQL Grammar  Advantage ODBC Driver |  |  |  |  |

The Advantage ODBC Driver supports three levels of SQL grammars: Minimum, Core and Extended. Each higher level provides more fully implemented data definition and data manipulation language support.

The following chart outlines the SQL Grammar support with the Advantage ODBC Driver. See [Advantage SQL Engine](master_advantage_sql_engine.htm) for more information.

|  |  |
| --- | --- |
| SQL Grammar | SQL Grammar Support |
| [ALTER TABLE](master_alter_table.htm) | Extended |
| [BEGIN TRANSACTION](master_begin_transaction.htm) | Extended |
| [COMMIT WORK](master_commit_work.htm) | Extended |
| [CREATE DATABASE](master_create_database.htm) | Extended |
| [CREATE INDEX](master_create_index.htm) | Core |
| [CREATE PROCEDURE](master_create_procedure.htm) | Extended |
| [CREATE TABLE](master_create_table.htm) | Minimum |
| [CREATE TRIGGER](master_create_trigger.htm) | Extended |
| [CREATE VIEW](master_create_view.htm) | Extended |
| [DELETE](master_delete.htm) (searched) | Minimum |
| [DROP INDEX](master_drop_index.htm) | Core |
| [DROP PROCEDURE](master_drop_procedure.htm) | Extended |
| [DROP TABLE](master_drop_table.htm) | Minimum |
| [DROP TRIGGER](master_drop_trigger.htm) | Extended |
| [DROP VIEW](master_drop_view.htm) | Extended |
| [EXECUTE PROCEDURE](master_execute_procedure.htm) \* | Extended |
| [GRANT](master_grant.htm) | Core |
| [INSERT](master_insert.htm) | Minimum |
| [REVOKE](master_revoke.htm) | Core |
| [ROLLBACK WORK](master_rollback_work.htm) | Extended |
| [SELECT](master_select.htm) | Minimum |
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
| [SET TRANSACTION](master_set_transaction.htm) | Extended |
| Subqueries | Core |
| Unions | Extended |
| [UPDATE](master_update.htm) | Minimum |

\* This statement is an extension to the ODBC SQL grammar.