Keywords




Advantage Database Server 12  

     Keywords

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Keywords  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Keywords Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Keywords Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Keywords / Dear Support Staff, |  |
| Keywords  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Keywords are special words that are used to build the primary instructions embodied in a SQL statement. For example, consider the following SQL command:

SELECT Picture FROM PRODUCTS

The keywords in this SQL statement are SELECT and FROM. These words hold special meaning to Advantage, and are used to drive the requested operations.

Keywords appear directly in your SQL statements, and are never enclosed within delimiters. Some SQL keywords are also reserved words. As you learned in the preceding section, field names and table names that begin with a letter and that consist of only alphanumeric characters also do not require delimiters. However, if you have a field name or a table name that matches one of the reserved keywords, you must enclose that field name or table name in the double-quote or square brace delimiters. Doing so prevents Advantage from confusing that field name or table name with the matching reserved keyword.

The reserved keywords, as of this writing, are listed in Table 11-1.

 

|  |  |  |  |
| --- | --- | --- | --- |
| ADD | ALL | ALTER | AND |
| ANY | AS | ASC | AVG |
| BEGIN | BETWEEN | BY | CASE |
| CAST | CLOSE | COLUMN | COMMIT |
| CONSTRAINT | COUNT | CREATE | CURSOR |
| DECLARE | DEFAULT | DELETE | DESC |
| DISTINCT | DROP | ELSE | END |
| ESCAPE | EXECUTE | EXISTS | FALSE |
| FETCH | FOR | FROM | FULL |
| FUNCTION | GRANT | GROUP | HAVING |
| IN | INDEX | INNER | INSERT |
| INTO | IS | JOIN | KEY |
| LEFT | LIKE | MAX | MIN |
| NOT | NULL | OF | ON |
| OPEN | OR | ORDER | OUTER |
| OUTPUT | PRIMARY | PROCEDURE | RETURN |
| RETURNS | REVOKE | RIGHT | ROLLBACK |
| SAVEPOINT | SELECT | SET | SQL |
| SUM | TABLE | THEN | TO |
| TRANSACTION | TRUE | UNION | UNIQUE |
| UPDATE | USER | VALUES | VIEW |
| WHEN | WHERE | WORK |  |

Table 11-1: Reserved Keywords