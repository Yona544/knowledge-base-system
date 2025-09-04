General Improvements to Advantage SQL




Advantage Database Server 12  

     General Improvements to Advantage SQL

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| General Improvements to Advantage SQL  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      General Improvements to Advantage SQL Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_General\_Improvements\_to\_Advantage\_SQL Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > General Improvements to Advantage SQL / Dear Support Staff, |  |
| General Improvements to Advantage SQL  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The support for SQL in Advantage 7 is excellent, and in this release it gets even better. For starters, Advantage 8.1 now supports both FULL and RIGHT OUTER joins. Additional improvements include permitting the use of subqueries anywhere an expression is permitted, permitting aliased column names in HAVING clauses, the use of TOP X in subqueries, and the introduction of an escape character in LIKE conditions.

Advantage SQL scripts can now also return a cursor. Specifically, if SELECT is the last statement in a SQL script, that script will return the records fetched by that SELECT statement.