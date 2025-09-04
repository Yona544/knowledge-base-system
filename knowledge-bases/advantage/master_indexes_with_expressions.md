Indexes with Expressions




Advantage Database Server 12  

Indexes with Expressions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Indexes with Expressions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Indexes with Expressions Advantage SQL Engine master\_Indexes\_with\_expressions Advantage SQL > SQL Functionality > Indexes with Expressions / Dear Support Staff, |  |
| Indexes with Expressions  Advantage SQL Engine |  |  |  |  |

While the Advantage API allows expressions in indexes, SQL syntax does not. For example, the SQL statement "create index descript on bugbase (bug\_name)" is a legal statement, while "create index descript on bugbase (lcase(bug\_name))" is an illegal statement. If an expression index is necessary, use the direct Advantage Client Engine function AdsCreateIndex() or [sp\_CreateIndex()](master_sp_createindex.htm) to create an expression index.

In a subsequent SQL query, the Advantage SQL expression engine will convert certain SQL scalar functions in the SQL command onto the equivalent Advantage expression functions, so then the Advantage expression index can be used if the expressions match. By carefully choosing an Advantage index expression, SQL query performance could greatly benefit.

Given a common query such as "lcase(lastname) = 'smith'" (to find all occurances of 'Smith' regardless of case), an index might provide better performance. For example, use AdsCreateIndex() or sp\_CreateIndex() to create an index on lower(lastname). The SQL query "select \* from payroll where lcase(lastname) = 'smith'" will use that expression index.

Using the SQL statement "select \* from payroll where lcase(lastname) = 'smith' and lcase(firstname) = 'john'" may or may not be optimized. If there is no index available, a non-optimized AOF is used and traditional, but slower, filtering of each record will be done to optimize the AOF. If the expression index lower(lastname) exists, then the query is partially optimized. For partial optimization, the AOF is used to reduce the result set that must be subsequently filtered with a traditional record filter. If two expression indexes (one on lower(lastname) and one on lower(firstname)) exist, then the query will be fully optimized, and AOFs can be used for all filtering.

Also note that the ability to map the SQL expression to an index expression is a controlling factor in whether the result of a SELECT statement will be a live or static cursor. If an expression used in a WHERE clause of a SELECT statement cannot be mapped to an index expression, then the result of the query will be a static cursor.

The following table lists the SQL scalar functions mapped to Advantage scalar functions. By creating an index using any of the following Advantage scalar functions or expressions, an SQL query using the mapped scalar function will benefit.

|  |  |
| --- | --- |
| SQL Scalar | Advantage Function |
| ABS | ABS |
| ALLTRIM | ALLTRIM |
| ASCII | ASCII   (requires v12.0 client) |
| AT | AT |
| BIT\_LENGTH | LEN\*8 |
| CEILING | CEILING   (requires v12.0 client) |
| CHAR | CHR |
| CHAR2HEX | CHAR2HEX |
| CHAR\_LENGTH | LEN |
| CHARACTER\_LENGTH | LEN |
| COALESCE | COALESCE   (requires v12.0 client) |
| CONCAT | string '+' |
| CONTAINS | CONTAINS |
| CREATETIMESTAMP | CREATETIMESTAMP   (requires v12.0 client) |
| CTOD | CTOD |
| CTOT | CTOT |
| CTOTS | CTOTS |
| CURDATE | DATE |
| CURRENT\_DATE | DATE |
| CURRENT\_TIME | CTOT( TIME() ) |
| CURTIME | CTOT( TIME() ) |
| DAY | DAY   (requires v12.0 client if parameter is a timestamp) |
| DAYNAME | DAYNAME |
| DAYOFMONTH | DAY   (requires v12.0 client if parameter is a timestamp) |
| DAYOFWEEK | DAYOFWEEK |
| DAYOFYEAR | DAYOFYEAR |
| DELETED | DELETED |
| DIFFERENCE | DIFFERENCE   (requires v12.0 client) |
| DTOS | DTOS |
| DTOC | DTOC |
| EMPTY | EMPTY |
| FLOOR | FLOOR   (requires v12.0 client) |
| FRAC\_SECOND | FRAC\_SECOND   (requires v12.0 client) |
| HEX2CHAR | HEX2CHAR |
| HOUR | HOUR |
| IFNULL( expr, val ) | ADT and VFP:  IIF( ISNULL( expr ), val )    CDX and NTX:  IIF( EMPTY( expr ), val ) |
| ISNULL( expr, val ) | ADT and VFP:  IIF( ISNULL( expr ), val )    CDX and NTX:  IIF( EMPTY( expr ), val ) |
| IIF | IIF |
| ISOWEEK | ISOWEEK |
| LCASE | LOWER |
| LEFT | LEFT |
| LEN | LEN |
| LENGTH | For pre v12.0 clients: LEN(RTRIM())  For v12.0 clients:  LENGTH |
| LOCATE(x,y) | AT |
| LOCATE(x,y,z) | AT   (requires v12.0 client) |
| LOWER | LOWER |
| LTRIM | LTRIM |
| MINUTE | MINUTE |
| MONTH | MONTH   (requires v12.0 client if parameter is a timestamp) |
| MONTHNAME | MONTHNAME |
| NOW | NOW |
| OCTET\_LENGTH | LEN |
| PI | 3.1415926535897932 |
| POSITION | AT |
| POWER | \*\* |
| QUARTER | QUARTER |
| RAT | RAT |
| RECNO | RECNO |
| REVERSE | REVERSE |
| REPEAT | REPEAT   (requires v12.0 client) |
| RIGHT | RIGHT |
| RTRIM | RTRIM |
| SECOND | SECOND |
| SIGN | SIGN   (requires v12.0 client) |
| SOUNDEX | SOUNDEX   (requires v12.0 client) |
| SPACE | SPACE |
| STOD | STOD |
| STOTS | STOTS |
| STR(x,y,z) | STR(x,y,z) |
| STRZERO(x,y,z) | STRZERO(x,y,z) |
| SUBSTRING | SUBSTR |
| TIME | TIME |
| TSTOD | TSTOD |
| TTOC | TTOC |
| UCASE | UPPER |
| UPPER | UPPER |
| VAL | VAL |
| WEEK | WEEK |
| YEAR | YEAR   (requires v12.0 client if parameter is a timestamp) |

Using any of the following SQL scalar functions disqualifies the expression from using an existing index.

Math

|  |  |
| --- | --- |
| ACOS | LOG10 |
| ASIN | MOD |
| ATAN | RADIANS |
| ATAN2 | RAND |
| COS | ROUND |
| COT | SIN |
| DEGREES | SQRT |
| EXP | TAN |
| LOG | TRUNCATE |

String

|  |  |
| --- | --- |
| ENDSWITH | STARTSWITH |
| INSERT | SUBSTRINGOF |
| REPLACE |  |

Date/Time

|  |  |
| --- | --- |
| CURRENT\_TIMESTAMP | TIMESTAMPADD |
| CURRENT\_TIMESTAMP\_UTC | TIMESTAMPDIFF |
| EXTRACT |  |

Misc

|  |  |
| --- | --- |
| APPLICATIONID | LASTROWID |
| CAST | ROWNUM |
| CONVERT | SCORE |
| DATABASE | SCOREDISTINCT |
| EXTRACT | USER |
| LASTAUTOINC |  |