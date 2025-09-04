Important Notes




Advantage Database Server 12  

Important Notes

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Important Notes |  |  | Feedback on: Advantage Database Server 12 - Important Notes odbc\_Important\_notes Advantage ODBC Driver > Introduction > Important Notes / Dear Support Staff, |  |
| Important Notes |  |  |  |  |

LARGE NUMERIC FIELDS

Although the Advantage ODBC Driver will let an application create large numeric fields with DBF tables (e.g., "CREATE TABLE tbl (n NUMERIC (19,5))"), some applications like Visual Basic and Access have a limit of NUMERIC(15, x). Anything larger causes the applications to treat the fields as text fields. This can generally be transparent because of automatic conversions but may be slower. One particular difference, though, is sorting. For example, a Visual Basic application that sorts on a result set may get different results if it treats the sort field as text rather than numeric. The Advantage ODBC Driver supports SQL\_DECIMAL, while other Xbase drivers may report the values as SQL\_DOUBLE and do conversions.

SQL\_PASSTHROUGH

When possible, the SQL\_PASSTHROUGH option should be used for SQL queries sent to the Advantage ODBC Driver. This allows the driver to better optimize the query. It is also necessary if the application does not recognize the SQL syntax. For example, some applications that parse SQL may not recognize the CONVERT function ("select convert(c, SQL\_DECIMAL) from tbl"). With the SQL\_PASSTHROUGH option, this statement would be passed untouched to the Advantage driver, and it would be parsed correctly. In some development environments, this option has a slightly different name, such as Microsoft Visual Basic, but use of a passthrough option is still strongly advised.

AUTO COMMIT MODE

In auto commit mode (the default transaction processing mode), the Advantage ODBC Driver does not use transactions when making updates to the data. For example, the SQL statement "UPDATE TABLE tbl SET fld = fld \* 5" will update every record in the table. In auto commit mode, each record update is performed individually rather than in a transaction for the entire update. This provides better performance than in the case where every update causes a transaction to occur. If you do want every statement to run in an individual transaction, you can use the SQL statement [SET TRANSACTION](master_set_transaction.htm) to turn on autocommit state at the server.