---
title: Jdbc Resultset Object
slug: jdbc_resultset_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_resultset_object.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 13708abca2426fd7d342c6323be201fd0f30c525
---

# Jdbc Resultset Object

ResultSet Object

ResultSet Object

Advantage JDBC Driver

| ResultSet Object  Advantage JDBC Driver |  |  |  |  |

| Methods | Version Introduced | Supported | Comments |
| boolean absolute (int) | 2.0 Core | Yes |  |
| void afterLast () | 2.0 Core | Yes |  |
| void beforeFirst () | 2.0 Core | Yes |  |
| void cancelRowUpdates () | 2.0 Core | Yes |  |
| void clearWarnings () | 1.0 | Yes |  |
| void close () | 1.0 | Yes |  |
| void deleteRow () | 2.0 Core | Yes |  |
| int findColumn (String) | 1.0 | Yes |  |
| boolean first () | 2.0 Core | Yes |  |
| Array getArray (String) | 2.0 Core | No | Throws "feature not supported" exception. |
| Array getArray (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| InputStream getAsciiStream (String) | 1.0 | Yes |  |
| InputStream getAsciiStream (int) | 1.0 | Yes |  |
| BigDecimal getBigDecimal (String) | 2.0 Core | Yes |  |
| BigDecimal getBigDecimal (int) | 2.0 Core | Yes |  |
| BigDecimal getBigDecimal (String, int) | 1.0 | No | Throws "feature not supported" exception. |
| BigDecimal getBigDecimal (int, int) | 1.0 | No | Throws "feature not supported" exception. |
| InputStream getBinaryStream (int) | 1.0 | Yes |  |
| InputStream getBinaryStream (String) | 1.0 | Yes |  |
| Blob getBlob (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| Blob getBlob (String) | 2.0 Core | No | Throws "feature not supported" exception. |
| boolean getBoolean (String) | 1.0 | Yes |  |
| boolean getBoolean (int) | 1.0 | Yes |  |
| byte getByte (int) | 1.0 | Yes |  |
| byte getByte (String) | 1.0 | Yes |  |
| byte [] getBytes (String) | 1.0 | Yes |  |
| byte [] getBytes (int) | 1.0 | Yes |  |
| Reader getCharacterStream (int) | 2.0 Core | Yes |  |
| Reader getCharacterStream (String) | 2.0 Core | Yes |  |
| Clob getClob (String) | 2.0 Core | No | Throws "feature not supported" exception. |
| Clob getClob (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| int getConcurrency () | 2.0 Core | Yes |  |
| String getCursorName () | 1.0 | No | Throws "feature not supported" exception. |
| Date getDate (int) | 1.0 | Yes |  |
| Date getDate (String) | 1.0 | Yes |  |
| Date getDate (String, Calendar) | 2.0 Core | Yes |  |
| Date getDate (int, Calendar) | 2.0 Core | Yes |  |
| double getDouble (String) | 1.0 | Yes |  |
| double getDouble (int) | 1.0 | Yes |  |
| int getFetchDirection () | 2.0 Core | Yes |  |
| int getFetchSize () | 2.0 Core | Yes |  |
| float getFloat (int) | 1.0 | Yes |  |
| float getFloat (String) | 1.0 | Yes |  |
| int getInt (int) | 1.0 | Yes |  |
| int getInt (String) | 1.0 | Yes |  |
| long getLong (int) | 1.0 | Yes |  |
| long getLong (String) | 1.0 | Yes |  |
| ResultSetMetaData getMetaData () | 1.0 | Yes |  |
| Object getObject (int) | 1.0 | Yes |  |
| Object getObject (String) | 1.0 | Yes |  |
| Object getObject (int, Map) | 2.0 Core | No | Throws "feature not supported" exception. |
| Object getObject (String, Map) | 2.0 Core | No | Throws "feature not supported" exception. |
| Ref getRef (int) | 2.0 Core | No | Throws "feature not supported" exception. |
| Ref getRef (String) | 2.0 Core | No | Throws "feature not supported" exception. |
| int getRow () | 2.0 Core | Yes |  |
| short getShort (String) | 1.0 | Yes |  |
| short getShort (int) | 1.0 | Yes |  |
| Statement getStatement () | 2.0 Core | Yes |  |
| String getString (int) | 1.0 | Yes |  |
| String getString (String) | 1.0 | Yes |  |
| Time getTime (int) | 1.0 | Yes |  |
| Time getTime (String) | 1.0 | Yes |  |
| Time getTime (String, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| Time getTime (int, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| Timestamp getTimestamp (int) | 1.0 | Yes |  |
| Timestamp getTimestamp (String) | 1.0 | Yes |  |
| Timestamp getTimestamp (String, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| Timestamp getTimestamp (int, Calendar) | 2.0 Core | No | Throws "feature not supported" exception. |
| int getType () | 2.0 Core | Yes |  |
| InputStream getUnicodeStream (int) | 1.0 | No | Throws "feature not supported" exception. |
| InputStream getUnicodeStream (String) | 1.0 | No | Throws "feature not supported" exception. |
| SQLWarning getWarnings () | 1.0 | Yes |  |
| void insertRow () | 2.0 Core | Yes |  |
| boolean isAfterLast () | 2.0 Core | Yes |  |
| boolean isBeforeFirst () | 2.0 Core | Yes |  |
| boolean isFirst () | 2.0 Core | Yes |  |
| boolean isLast () | 2.0 Core | Yes |  |
| boolean last () | 2.0 Core | Yes |  |
| void moveToCurrentRow () | 2.0 Core | Yes |  |
| void moveToInsertRow () | 2.0 Core | Yes |  |
| boolean next () | 1.0 | Yes |  |
| boolean previous () | 2.0 Core | Yes |  |
| void refreshRow () | 2.0 Core | Yes |  |
| boolean relative (int) | 2.0 Core | Yes |  |
| boolean rowDeleted () | 2.0 Core | Yes | If ShowDeleted=True is specified in the connection URL and the result set is a live cursor based on a DBF table, the data may still be read from the columns of a deleted row.  If ShowDelete=False is specified, or the result set is not a live cursor, or the cursor is based on ADT table, then no data may be read from a deleted row and attempting to read data will cause an SQLException being thrown. |
| boolean rowInserted () | 2.0 Core | Yes |  |
| boolean rowUpdated () | 2.0 Core | Yes |  |
| void setFetchDirection (int) | 2.0 Core | Yes |  |
| void setFetchSize (int) | 2.0 Core | Yes |  |
| void updateAsciiStream (String, InputStream, int) | 2.0 Core | Yes |  |
| void updateAsciiStream (int, InputStream, int) | 2.0 Core | Yes |  |
| void updateBigDecimal (int, BigDecimal) | 2.0 Core | Yes |  |
| void updateBigDecimal (String, BigDecimal) | 2.0 Core | Yes |  |
| void updateBinaryStream (String, InputStream, int) | 2.0 Core | Yes |  |
| void updateBinaryStream (int, InputStream, int) | 2.0 Core | Yes |  |
| void updateBoolean (int, boolean) | 2.0 Core | Yes |  |
| void updateBoolean (String, boolean) | 2.0 Core | Yes |  |
| void updateByte (String, byte) | 2.0 Core | Yes |  |
| void updateByte (int, byte) | 2.0 Core | Yes |  |
| void updateBytes (String, byte []) | 2.0 Core | Yes |  |
| void updateBytes (int, byte []) | 2.0 Core | Yes |  |
| void updateCharacterStream (String, Reader, int) | 2.0 Core | Yes |  |
| void updateCharacterStream (int, Reader, int) | 2.0 Core | Yes |  |
| void updateDate (int, Date) | 2.0 Core | Yes |  |
| void updateDate (String, Date) | 2.0 Core | Yes |  |
| void updateDouble (String, double) | 2.0 Core | Yes |  |
| void updateDouble (int, double) | 2.0 Core | Yes |  |
| void updateFloat (int, float) | 2.0 Core | Yes |  |
| void updateFloat (String, float) | 2.0 Core | Yes |  |
| void updateInt (int, int) | 2.0 Core | Yes |  |
| void updateInt (String, int) | 2.0 Core | Yes |  |
| void updateLong (String, long) | 2.0 Core | Yes |  |
| void updateLong (int, long) | 2.0 Core | Yes |  |
| void updateNull (String) | 2.0 Core | Yes |  |
| void updateNull (int) | 2.0 Core | Yes |  |
| void updateObject (String, Object) | 2.0 Core | Yes |  |
| void updateObject (int, Object) | 2.0 Core | Yes |  |
| void updateObject (String, Object, int) | 2.0 Core | No | Throws "feature not supported" exception. |
| void updateObject (int, Object, int) | 2.0 Core | No | Throws "feature not supported" exception. |
| void updateRow () | 2.0 Core | Yes |  |
| void updateShort (int, short) | 2.0 Core | Yes |  |
| void updateShort (String, short) | 2.0 Core | Yes |  |
| void updateString (String, String) | 2.0 Core | Yes |  |
| void updateString (int, String) | 2.0 Core | Yes |  |
| void updateTime (int, Time) | 2.0 Core | Yes |  |
| void updateTime (String, Time) | 2.0 Core | Yes |  |
| void updateTimestamp (String, Timestamp) | 2.0 Core | Yes |  |
| void updateTimestamp (int, Timestamp) | 2.0 Core | Yes |  |
| boolean wasNull () | 1.0 | Yes |  |
