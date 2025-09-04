---
title: Jdbc Callablestatement Object
slug: jdbc_callablestatement_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_callablestatement_object.htm
source: Advantage CHM
tags:
  - jdbc
checksum: f48eaaf8dda087a6e32153b21f1fc19d8bb2c585
---

# Jdbc Callablestatement Object

CallableStatement Object

CallableStatement Object

Advantage JDBC Driver

| CallableStatement Object  Advantage JDBC Driver |  |  |  |  |

The CallableStatement allows the application to execute the Advantage Extended Procedures (AEP) or the Advantage Database system procedures (sp\_xxx). The output parameter features of the CallableStatement are not supported since the stored procedure in Advantage Database Server always returns the output in a cursor. The "Feature not supported" exception is thrown if any of the output parameter related method is called.

Note See [Statement Object](jdbc_statement_object.md) for additional methods available in the Advantage JDBC Driver.

| Methods | Version Introduced | Supported | Comments |
| void addBatch () | 2.0 Core | Yes |  |
| void addBatch (String) | 2.0 Core | No | Throws "illegal operation" exception. |
| void cancel () | 1.0 | Yes |  |
| void clearBatch () | 2.0 Core | Yes |  |
| void clearParameters () | 1.0 | Yes |  |
| void clearWarnings () | 1.0 | Yes |  |
| void close () | 1.0 | Yes |  |
| boolean execute () | 1.0 | Yes |  |
| boolean execute (String) | 1.0 | No | Throws "illegal operation" exception. |
| int [] executeBatch () | 2.0 Core | Yes |  |
| ResultSet executeQuery () | 1.0 | Yes |  |
| ResultSet executeQuery (String) | 1.0 | No | Throws "illegal operation" exception. |
| int executeUpdate () | 1.0 | Yes |  |
| int executeUpdate (String) | 1.0 | No | Throws "illegal operation" exception. |
| Array getArray (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| BigDecimal getBigDecimal (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| BigDecimal getBigDecimal (int, int) | 1.0 | No | Throws "feature not supported" exception. |
| Blob getBlob (int) | 2.0 Core | No | Throws " feature not supported " exception. |
| boolean getBoolean (int) | 1.0 | No | Throws "feature not supported" exception. |
| byte getByte (int) | 1.0 | No | Throws "feature not supported" exception. |
| byte [] getBytes (int) | 1.0 | No | Throws "feature not supported" exception. |
| Clob getClob (int) | 2.0 Core | No | Throws "unsupported method" exception. |
| Connection getConnection () | 1.0 | Yes |  |
| Date getDate (int) | 1.0 | No | Throws "feature not supported" exception. |
| Date getDate (int, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| double getDouble (int) | 1.0 | No | Throws "feature not supported" exception. |
| int getFetchDirection () | 2.0 Core | Yes |  |
| int getFetchSize () | 2.0 Core | Yes |  |
| float getFloat (int) | 1.0 | No | Throws "feature not supported" exception. |
| int getInt (int) | 1.0 | No | Throws "feature not supported" exception. |
| long getLong (int) | 1.0 | No | Throws "feature not supported" exception. |
| int getMaxFieldSize () | 1.0 | Yes |  |
| int getMaxRows () | 1.0 | Yes |  |
| ResultSetMetaData getMetaData () | 2.0 Core | Yes |  |
| boolean getMoreResults () | 1.0 | Yes |  |
| Object getObject (int) | 1.0 | No | Throws "feature not supported" exception. |
| Object getObject (int, Map) | 2.0 Core | No | Throws "feature not supported" exception. |
| int getQueryTimeout () | 1.0 | Yes |  |
| Ref getRef (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| ResultSet getResultSet () | 1.0 | Yes |  |
| int getResultSetConcurrency () | 2.0 Core | Yes |  |
| int getResultSetType () | 2.0 Core | Yes |  |
| short getShort (int) | 1.0 | No | Throws "feature not supported" exception. |
| String getString (int) | 1.0 | No | Throws "feature not supported" exception. |
| Time getTime (int) | 1.0 | Yes | Throws "feature not supported" exception. |
| Time getTime (int, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| Timestamp getTimestamp (int) | 1.0 | Yes | Throws "feature not supported" exception. |
| Timestamp getTimestamp (int, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| int getUpdateCount () | 1.0 | Yes |  |
| SQLWarning getWarnings () | 1.0 | Yes |  |
| void registerOutParameter (int, int) | 1.0 | No | Throws "feature not supported" exception. |
| void registerOutParameter (int, int, String) | 2.0 Core | No | Throws "feature not supported" exception. |
| void registerOutParameter (int, int, int) | 1.0 | No | Throws "feature not supported" exception. |
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
| void setDate (int, Date, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
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
| void setNull (int, int, String) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setObject (int, Object) | 1.0 | No | Throws "feature not supported" exception. |
| void setObject (int, Object, int) | 1.0 | No | Throws "feature not supported" exception. |
| void setObject (int, Object, int, int) | 1.0 | No | Throws "feature not supported" exception. |
| void setQueryTimeout (int) | 1.0 | No | Throws "feature not supported" exception. |
| void setRef (int, Ref) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setShort (int, short) | 1.0 | Yes |  |
| void setString (int, String) | 1.0 | Yes |  |
| void setTime (int, Time) | 1.0 | Yes |  |
| void setTime (int, Time, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setTimestamp (int, Timestamp) | 1.0 | Yes |  |
| void setTimestamp (int, Timestamp, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| void setUnicodeStream (int, InputStream, int) | 1.0 | No | Throws "feature not supported" exception. |
| boolean wasNull () | 1.0 | Yes |  |
