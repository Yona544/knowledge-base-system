SQL Statement Dimensions




Advantage Database Server 12  

     SQL Statement Dimensions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Statement Dimensions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      SQL Statement Dimensions Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_SQL\_Statement\_Dimensions Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > SQL Statement Dimensions / Dear Support Staff, |  |
| SQL Statement Dimensions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are a few limits to the elements of a single SQL statement. Table names and database names can be no longer than 255 characters in length, and column names and index names can be no longer than 63 characters. Furthermore, you are limited to a maximum of 20 items in an ORDER BY clause, and no more than 15 columns in an index.

There is no size limitation to SQL statements and the string literals that appear within them. (Prior to Advantage 7.1, SQL statements were limited to 65,535 characters and string literals were limited to 1,024 characters.)