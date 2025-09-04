PreparedStatement Object




Advantage Database Server 12  

PreparedStatement Object

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| PreparedStatement Object  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - PreparedStatement Object Advantage JDBC Driver jdbc\_Preparedstatement\_object Advantage JDBC Driver > Supported Functionality > PreparedStatement Object / Dear Support Staff, |  |
| PreparedStatement Object  Advantage JDBC Driver |  |  |  |  |

Note See [Statement Object](jdbc_statement_object.htm) for additional methods available in Advantage JDBC Driver.

|  |  |  |  |
| --- | --- | --- | --- |
| Methods | Version Introduced | Supported | Comments |
| void addBatch () | 2.0 Core | Yes |  |
| void addBatch (String) | 2.0 Core | No | Throws "Illegal operation." exception. |
| void cancel () | 1.0 | Yes |  |
| void clearBatch () | 2.0 Core | Yes |  |
| void clearParameters () | 1.0 | Yes |  |
| void clearWarnings () | 1.0 | Yes |  |
| void close () | 1.0 | Yes |  |
| boolean execute () | 1.0 | Yes |  |
| boolean execute (String) | 1.0 | No | Throws "Illegal operation." exception. |
| int [] executeBatch () | 2.0 Core | Yes |  |
| ResultSet executeQuery () | 1.0 | Yes |  |
| ResultSet executeQuery (String) | 1.0 | No | Throws "Illegal operation." exception. |
| int executeUpdate () | 1.0 | Yes |  |
| int executeUpdate (String) | 1.0 | No | Throws "Illegal operation." exception. |
| Connection getConnection () | 1.0 | Yes |  |
| int getFetchDirection () | 2.0 Core | Yes |  |
| int getFetchSize () | 2.0 Core | Yes |  |
| int getMaxFieldSize () | 1.0 | Yes |  |
| int getMaxRows () | 1.0 | Yes |  |
| ResultSetMetaData getMetaData () | 2.0 Core | Yes |  |
| boolean getMoreResults () | 1.0 | Yes |  |
| int getQueryTimeout () | 1.0 | Yes |  |
| ResultSet getResultSet () | 1.0 | Yes |  |
| int getResultSetConcurrency () | 2.0 Core | Yes |  |
| int getResultSetType () | 2.0 Core | Yes |  |
| int getUpdateCount () | 1.0 | Yes |  |
| SQLWarning getWarnings () | 1.0 | Yes |  |
| void setArray (int, Array) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setAsciiStream (int, InputStream, int) | 1.0 | Yes |  |
| void setBigDecimal (int, BigDecimal) | 1.0 | Yes |  |
| void setBinaryStream (int, InputStream, int) | 1.0 | Yes |  |
| void setBlob (int, Blob) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setBoolean (int, boolean) | 1.0 | Yes |  |
| void setByte (int, byte) | 1.0 | Yes |  |
| void setBytes (int, byte []) | 1.0 | Yes |  |
| void setCharacterStream (int, Reader, int) | 2.0 Core | Yes |  |
| void setClob (int, Clob) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setCursorName (String) | 1.0 | No | Throws "feature not supported" exception. |
| void setDate (int, Date) | 1.0 | Yes |  |
| void setDate (int, Date, Calendar) | 2.0 Core | Yes |  |
| void setDouble (int, double) | 1.0 | Yes |  |
| void setEscapeProcessing (boolean) | 1.0 | Yes | Ignored. |
| void setFetchDirection (int) | 2.0 Core | Yes |  |
| void setFetchSize (int) | 2.0 Core | Yes |  |
| void setFloat (int, float) | 1.0 | Yes |  |
| void setInt (int, int) | 1.0 | Yes |  |
| void setLong (int, long) | 1.0 | Yes |  |
| void setMaxFieldSize (int) | 1.0 | Yes |  |
| void setMaxRows (int) | 1.0 | Yes |  |
| void setNull (int, int) | 1.0 | Yes |  |
| void setNull (int, int, String) | 2.0 Core | Yes |  |
| void setObject (int, Object) | 1.0 | No | Throws "feature not supported" exception. |
| void setObject (int, Object, int) | 1.0 | No | Throws "feature not supported" exception. |
| void setObject (int, Object, int, int) | 1.0 | No | Throws "feature not supported" exception. |
| void setQueryTimeout (int) | 1.0 | Yes |  |
| void setRef (int, Ref) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setShort (int, short) | 1.0 | Yes |  |
| void setString (int, String) | 1.0 | Yes |  |
| void setTime (int, Time) | 1.0 | Yes |  |
| void setTime (int, Time, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setTimestamp (int, Timestamp) | 1.0 | Yes |  |
| void setTimestamp (int, Timestamp, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setUnicodeStream (int, InputStream, int) | 1.0 | No | Throws "feature not supported" exception. |