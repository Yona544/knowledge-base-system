Replication Overview




Advantage Database Server 12  

Replication Overview

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication Overview  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Replication Overview Advantage Concepts master\_Replication\_overview Advantage Concepts > Advantage Functionality > Replication > Replication Overview / Dear Support Staff, |  |
| Replication Overview  Advantage Concepts |  |  |  |  |

Replication provides the capability to distribute changes from tables in one database to tables in another database. Advantage Replication uses an asynchronous push implementation in order to minimize performance impact on applications and to minimize latency in the delivery of updates to target databases.

N-way replication can be accomplished by defining replication rules in each data dictionary to replicate changes to each of the other databases. Optional horizontal and vertical filters can be specified to limit replication to a subset of the data.

Transactional and referential integrity is maintained during replication. If a target database is not available, the source server will maintain updates in a queue and transmit them to the target when it becomes available. Conflict resolution can be handled by CONFLICT triggers on target tables.

Advantage Replication is not synchronization. Replication can be used to keep tables synchronized, but Advantage has no functionality that checks for differences in tables or that performs an actual synchronization operation between two tables. Replication simply acts to send updates from one table to another target table. The target table does not have to be "in sync" with the source table.

Advantage Replication currently only supports record updates in ADT and DBF tables; it does not replicate other object types. For example, if you create a new stored procedure in the source database, that stored procedure will not be replicated to the target. In addition, pack (removal of deleted records) and zap (emptying of a table) operations are not replicated.

Note: When updating linked tables in a transaction, only tables from one dictionary can be replicated in a given transaction. If you begin a transaction and update tables in two different linked dictionaries that have replication defined, only the tables from the first updated dictionary will be replicated.

Replication Terminology

The following terms are used in the documentation.

|  |  |
| --- | --- |
| Source and Target | At the definition level, replication is a one-way concept. The updates travel from a source database to a target database. You define all replication information in the source data dictionary. |
| Source database | The originating database for a replication update. This can be considered the publishing database. |
| Target database | The receiving database for a replication update. This can be considered the subscribing database. |
| Article (or publication article) | A specific table to be replicated in the source database. |
| Filter | Each article that is replicated can have optional filters to limit the replication to be a subset of the data. Both horizontal and vertical filters are supported. Horizontal filters specify which records will be replicated (similar to a WHERE clause in an SQL statement). Vertical filters specify which columns of a table will be replicated. |
| Identification Columns | When you create a publication article, you must specify the identification columns. Advantage uses this set of columns to locate the target record when a record is modified in the source database. The identification columns can be any subset of searchable columns from the table but should be chosen so that they uniquely identify the record. The columns that make up the primary key are usually a good choice. |
| Publication | A group of articles to be replicated. In addition to the article names, it includes the columns for each article that are used to identify the record at the target database and an optional filter for each article. |
| Subscription | This defines where a specific publication is to be replicated. It includes the publication name, replication target, user ID and password for the target data dictionary, and various options that control the replication actions. Note that because Advantage implements push replication, the subscription is defined at the source database; not the target/subscriber. |
| Replication Update | This refers to a single record update that is being replicated from a source to a target. |
| Replication Queue | This is the queue of updates for a given subscription that are to be sent to a target. |

Replication Requirements

|  |  |
| --- | --- |
| · | Replication is available in Advantage Database Server for Windows and Linux. |

|  |  |
| --- | --- |
| · | The copy of Advantage Database Server at the source database must be licensed for replication (contact your Advantage Sales Representative for licensing information). A separate validation code is required. Advantage Database Server at the target does not have to be licensed for replication unless it will also be replicating changes. |

|  |  |
| --- | --- |
| · | Advantage Database Server must be running at both the source and target locations. |

|  |  |
| --- | --- |
| · | A Data Dictionary is required in order to use replication. For security reasons, replication cannot be used with free connections. |

See Also

[Getting Started with Replication](master_getting_started_with_replication.htm)