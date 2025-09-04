Miscellaneous Functions




Advantage Database Server 12  

Miscellaneous Functions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Miscellaneous Functions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Miscellaneous Functions Advantage SQL Engine master\_Miscellaneous\_functions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Miscellaneous Functions  Advantage SQL Engine |  |  |  |  |

|  |  |
| --- | --- |
| [APPLICATIONID](master_applicationid.htm)( ) | Returns the Application ID of the connection application. The Application ID is initialized to the file name of the application (executable) that connected to the Advantage Database Server (only for ACE based clients). The Application ID can be set and retrieved using the [sp\_SetApplicationID](master_sp_setapplicationid.htm) and [sp\_GetApplicationID](master_sp_getapplicationid.htm) system procedures. |
| [BASE64ENCODE](master_base64encode.htm)( binary | string ) | Returns a string containing the Base64 representing of the given binary or string (ASCII or Unicode) parameter. |
| [BASE64DECODE](master_base64decode.htm)( Base64String ) | Returns the binary value represented by the Base64 encoding of the given parameter. |
| [CAST](master_cast.htm) ( expr AS data-type [( precision [, scale ] ) ] ) | Returns the value of expr casted to data-type with an optional precision and scale value. The data-type parameter can be SQL\_BINARY, SQL\_VARBINARY, SQL\_BIT (logical), SQL\_LONGVARCHAR, SQL\_VARCHAR, SQL\_CHAR, SQL\_WLONGVARCHAR, SQL\_WVARCHAR, SQL\_WCHAR, SQL\_DATE, SQL\_NUMERIC, SQL\_DOUBLE, SQL\_INTEGER, SQL\_TIMESTAMP, SQL\_TIME, or SQL\_MONEY. Only SQL\_BINARY, SQL\_VARBINARY, SQL\_VARCHAR, SQL\_CHAR, and SQL\_NUMERIC support the precision parameter and only SQL\_NUMERIC supports the scale parameter. |
| [COALESCE](master_coalesce.htm)( expr1, ... exprn ) | Returns the first non-NULL expression result. All expressions must be of the same type or be implicitly convertible to the same type. No parameters or BLOBs are allowed as an expression type. If all the expressions evaluate to NULL, COALESCE returns a NULL value. |
| [CONTAINS](master_contains.htm)( field | \*, condition ) | Performs a full text search on the given field or on all fields that have full text search (FTS) indexes if the asterisk (\*) is specified. This function returns a logical TRUE or FALSE for records that meet the search condition. For details, see [Full Text Search](master_full_text_search.htm). The search condition (second parameter) is given as a character string. It can be any valid character value (including a character field value or expression result), but it must be a character literal or a parameter value in order to be fully optimized. |
| [CONVERT](master_convert.htm)( expr, data-type ) | Returns the value of expr converted to data-type. The data-type parameter can be SQL\_BINARY, SQL\_VARBINARY, SQL\_BIT (logical), SQL\_LONGVARCHAR, SQL\_VARCHAR, SQL\_CHAR, SQL\_WLONGVARCHAR, SQL\_WVARCHAR, SQL\_WCHAR, SQL\_DATE, SQL\_DOUBLE, SQL\_INTEGER, SQL\_NUMERIC, SQL\_TIME, SQL\_TIMESTAMP, or SQL\_MONEY. |
| [DATABASE](master_database.htm)( ) | Returns name of database for the connection. |
| [DELETED](master_deleted.htm)( [tablealias] ) | Returns TRUE or FALSE indicating whether the current record is marked as deleted. |
| [DESCEND](master_descend.htm)( expr ) | Creates a descending key value. |
| [DIFFERENCE](master_difference.htm)( str1, str2 ) | Returns an integer value that indicates the difference between the values returned by the SOUNDEX() function for str1 and str2. The value returned will be in the range 0 to 4. The value 4 indicates the closest match (it actually means that the soundex encoding of str1 and str2 are identical). The value 0 indicates the lowest possible phonetic match, with the values 1, 2, and 3 indicating increasing degrees of phonetic matching. |
| [EMPTY](master_empty.htm)( columnname ) | Returns TRUE if the specified column is empty and FALSE otherwise. For ADT tables, a column is considered empty if it is NULL. For DBF tables, a column is considered empty in the traditional Xbase sense (e.g., zero length strings and 0 numeric values are considered empty). If a Visual FoxPro (VFP) table column is NULL, then it is not considered empty (see [Null Values](master_null_values.htm)). |
| [IFNULL](master_ifnull.htm)( expr, value ) | If expr is NULL, value is returned. If expr is not NULL, expr is returned. |
| [IIF](master_iif.htm)(boolean\_expr, true\_expr, false\_expr) | If boolean\_expr is True, the evaluation of true\_expr is returned. If boolean\_expr is False, the evaluation of false\_expr is returned. See [IIF](master_iif_sql.htm) for more information. |
| [INLIST](master_inlist.htm)( value, expr1, expr2, ... ) | Search for a value in a list of values. |
| [ISNULL](master_ifnull.htm)( expr, value ) | If expr is NULL, value is returned. If expr is not NULL, expr is returned. |
| [LASTAUTOINC](master_lastautoinc.htm)( CONNECTION | STATEMENT ) | Returns the last used autoinc value from an insert or append. Specifying CONNECTION will return the last used value for the entire connection. Specifying STATEMENT returns the last used value for only the current SQL statement. If no autoinc value has been updated yet, a NULL value is returned.  Note Triggers that operate on tables with autoinc fields may affect the last autoinc value.  Note SQL script triggers run on their own SQL statement. Therefore, calling LASTAUTOINC( STATEMENT ) inside an SQL script trigger would return the lastautoinc value used by the trigger's SQL statement, not the original SQL statement which caused the trigger to fire. To obtain the original SQL statement's lastautoinc value, use LASTAUTOINC( CONNECTION ) instead.  Example SELECT LASTAUTOINC( STATEMENT ) FROM system.iota |
| [LASTROWID](master_lastrowid.htm) | Returns the [ROWID](master_rowid.htm) of the last row inserted into the table. This value can be used to identify a newly inserted row without prior knowledge of that row's key value, and without requiring the table to have an autoinc column. |
| [LASTROWVERSION](master_lastrowversion.htm) | Returns the ROWVERSION from the most recent update of a table having a ROWVERSION field for the current statement handle. |
| [NEWID](master_newidstring_.htm) | Returns a GUID. A GUID is a 16-byte data structure. |
| [NEWIDSTRING](master_newidstring_.htm) | Returns a GUID formatted as a string. If the format parameter is not specified, the GUID string is formatted as a hexadecimal string with the following pattern xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. The format parameter can be the following values:  M or MIME A GUID encoded as a 24-byte string using MIME base64 encoding with the format of xxxxxxxxxxxxxxxxxxxxxxxx. Base64 encoded strings are case sensitive and should not be stored in case insensitive string fields.  F or File A GUID encoded as a 22-byte string using File and URL Safe base64 encoding with the format of xxxxxxxxxxxxxxxxxxxxxx. Base64 encoded strings are case sensitive and should not be stored in case insensitive string fields.  N or Numbers A GUID encoded as a 32-byte hexadecimal string value with a format of xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.  D or Delimited A GUID encoded as a 32-byte hexadecimal string with a format of xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.  B or Bracketed A GUID encoded as a 32-byte hexadecimal string with a format of [xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx]  P or Parenthesis A GUID encoded as a 32-byte hexadecimal string with a format of (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)  C or Curlybraces A GUID encoded as a 32-byte hexadecimal string with a format of {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx} |
| [RECNO](master_recno.htm)( [tablealias] ) | Return the physical record number of the current record in the table. |
| [ROWNUM](master_rownum_scalar.htm)() | Generates numbers starting at 1 for each row in a result set. See [ROWNUM](master_rownum.htm) for more details. |
| [SCORE](master_score.htm)( field | \*, condition ) | This returns an integer value representing the score of the search condition for a given record. The score is the total count of the words from the search condition that are in the field. This is normally expected to be used in conjunction with the CONTAINS() scalar function (e.g., in ORDER BY clauses), but it can used in statements that do not use the CONTAINS() function. |
| [SCORE](master_score.htm)( n ) | This is an alternative version of the SCORE() function. The integer parameter n refers to the nth instance of CONTAINS() in the SQL statement. |
| [SCOREDISTINCT](master_scoredistinct.htm)( field | \*, condition ) | This scoring function returns the count of the words in the search condition that appear one or more times in the field for a given record. For example, if the search condition contains three words, this function will return a value from 0 to 3. |
| [SCOREDISTINCT](master_scoredistinct.htm)( n ) | This is an alternative version of the SCOREDISTINCT() function. The integer parameter n refers to the nth instance of CONTAINS() in the SQL statement. |
| [SOUNDEX](master_soundex.htm)( str ) | The soundex function returns a four-digit phonetic encoding of the given string. The encoding is of the form <letter><digit><digit><digit>. |
| [USER](master_user.htm)( ) | Returns the user name in the DBMS. |

See Also

[Supported Scalar Functions](master_supported_scalar_functions.htm)

[String Functions](master_string_functions.htm)

[Math Functions](master_math_functions.htm)

[Date/Time Functions](master_date_time_functions.htm)