SQL Statement Limits




Advantage Database Server 12  

SQL Statement Limits

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Statement Limits  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SQL Statement Limits Advantage SQL Engine master\_Sql\_statement\_limits Advantage SQL > Supported SQL Grammar > SQL Statement Limits / Dear Support Staff, |  |
| SQL Statement Limits  Advantage SQL Engine |  |  |  |  |

|  |  |
| --- | --- |
| Description | Value |
| Maximum character literal length | No Limit\* |
| Maximum column name length | 128 |
| Maximum table name length | 255 |
| Maximum database name length | 255 |
| Maximum index name length | 128 |
| Maximum columns in index | 15 |
| Maximum SQL statement length | No Limit\* (SQL script based stored procedure, trigger and UDF is limited to 64K maximum length) |
| Number of items in ORDER BY | 20 |

\* In versions 7.0 and earlier, the maximum character literal length was 1024 characters, and the total maximum length for an SQL statement was 65535 bytes. In versions 7.1 or greater, character literals and SQL statements can be arbitrarily long.