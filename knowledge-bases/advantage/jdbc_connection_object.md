Connection Object




Advantage Database Server 12  

Connection Object

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connection Object  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Connection Object Advantage JDBC Driver jdbc\_Connection\_object Advantage JDBC Driver > Supported Functionality > Connection Object / Dear Support Staff, |  |
| Connection Object  Advantage JDBC Driver |  |  |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
| Methods | Version Introduced | Supported | Comments |
| void close () | 1.0 | Yes | When a connection is closed while there is an active transaction, that transaction is rolled-back. |
| void commit () | 1.0 | Yes | See [Transaction Processing in Advantage JDBC](jdbc_transaction_processing_in_jdbc.htm) for additional information. |
| Statement createStatement () | 1.0 | Yes |  |
| Statement createStatement (int, int) | 2.0 Core | Yes |  |
| boolean getAutoCommit () | 1.0 | Yes | See [Transaction Processing in Advantage JDBC](jdbc_transaction_processing_in_jdbc.htm) for additional information. |
| String getCatalog () | 1.0 | Yes |  |
| DatabaseMetaData getMetaData () | 1.0 | Yes |  |
| int getTransactionIsolation () | 1.0 | Yes |  |
| Map getTypeMap () | 2.0 Core | No | Throws "feature not supported" exception. |
| SQLWarning getWarnings () | 1.0 | Yes |  |
| boolean isClosed () | 1.0 | Yes |  |
| boolean isReadOnly () | 1.0 | Yes |  |
| String nativeSQL (String) | 1.0 | Yes | Always returns same String as passed in. |
| CallableStatement prepareCall (String) | 1.0 | Yes |  |
| CallableStatement prepareCall (String, int, int) | 2.0 Core | Yes |  |
| PreparedStatement prepareStatement (String) | 1.0 | Yes |  |
| PreparedStatement prepareStatement (String, int, int) | 2.0 Core | Yes |  |
| void rollback () | 1.0 | Yes | See [Transaction Processing in Advantage JDBC](jdbc_transaction_processing_in_jdbc.htm) for additional information. |
| void setAutoCommit (boolean) | 1.0 | Yes | See [Transaction Processing in Advantage JDBC](jdbc_transaction_processing_in_jdbc.htm) for additional information. |
| void setCatalog (String) | 1.0 | No | Throws "Cannot change catalog" exception. |
| void setReadOnly (boolean) | 1.0 | Yes |  |
| void setTransactionIsolation (int) | 1.0 | Yes | Supports TRANSACTION\_READ\_UNCOMMITTED, TRANSACTION\_READ\_COMMITTED and TRANSACTION\_NON. The read uncommitted level is automatically upgraded to read committed. Throws "Unsupported Transaction Level" exception if other levels are requested. Default level is TRANSACTION\_NON. See [Transaction Processing in Advantage JDBC](jdbc_transaction_processing_in_jdbc.htm) for additional information. |
| void setTypeMap (Map) | 2.0 Core | Yes | Ignored. |