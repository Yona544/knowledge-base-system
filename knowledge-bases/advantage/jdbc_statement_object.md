Statement Object




Advantage Database Server 12  

Statement Object

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Statement Object  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Statement Object Advantage JDBC Driver jdbc\_Statement\_object Advantage JDBC Driver > Supported Functionality > Statement Object / Dear Support Staff, |  |
| Statement Object  Advantage JDBC Driver |  |  |  |  |

|  |  |  |  |
| --- | --- | --- | --- |
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