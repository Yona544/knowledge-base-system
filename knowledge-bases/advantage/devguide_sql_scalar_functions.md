SQL Scalar Functions




Advantage Database Server 12  

     SQL Scalar Functions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Scalar Functions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      SQL Scalar Functions Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_SQL\_Scalar\_Functions Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > SQL Scalar Functions / Dear Support Staff, |  |
| SQL Scalar Functions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

SQL scalar functions are built-in subroutines that can be used in your expressions. These functions permit you to write more flexible SQL statements by performing transformations on data or returning values that can only be determined at runtime.

   
NOTE: A scalar function is one that returns a single expression.  
 

For example, the following SQL statement uses the CURDATE() function, which returns the current date, based on your server's internal clock:

SELECT \* FROM INVOICE  
  WHERE [Invoice Due Date] > CURDATE() - 7   
  AND [Invoice Due Date] < CURDATE() AND  
  [Date Payment Received] IS NULL

This query will return all invoices that became due in the past week for which payment has not yet been received. Because of the use of the CURDATE() function, this query will always produce the past week's outstanding invoices, whether you execute it today, tomorrow, or two years from now.

The Advantage SQL scalar functions can be divided into four categories. These are date/time functions, math functions, string functions, and miscellaneous functions. Each of these is described briefly in the following sections. For a more detailed description of each function, including its syntax, refer to the Advantage help.

Date/Time Functions

You use the Advantage date/time SQL scalar functions to determine or process date/time information. Table 11-2 contains a list of the supported date/time functions.

|  |  |  |
| --- | --- | --- |
| CURDATE | CURRENT\_DATE | CURRENT\_TIME |
| CURRENT\_TIMESTAMP | CURTIME | DAYNAME |
| DAYOFMONTH | DAYOFWEEK | DAYOFYEAR |
| EXTRACT | HOUR | MINUTE |
| MONTH | MONTHNAME | NOW |
| QUARTER | SECOND | TIMESTAMPADD |
| TIMESTAMPDIFF | WEEK | YEAR |

Table 11-2: Date/Time Scalar Functions

Math Functions

The Advantage math scalar functions provide you with a rich collection of arithmetic and trigonometric functions. Also included in this category are functions that round and truncate numbers, as well as a function that generates random numbers. The Advantage math SQL scalar functions are listed in Table 11-3.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ABS | ACOS | ASIN | ATAN | ATAN2 |
| CEILING | COS | COT | DEGREES | EXP |
| FLOOR | LOG | LOG10 | MOD | PI |
| POWER | RADIANS | RAND | ROUND | SIGN |
| SIN | SQRT | TAN | TRUNCATE |  |

Table 11-3: Math Scalar Functions

String Functions

The Advantage string functions are used to process and convert string expressions. The Advantage string SQL scalar functions are listed in Table 11-4.

|  |  |  |
| --- | --- | --- |
| ASCII | BIT\_LENGTH | CHAR |
| CHAR\_LENGTH | CHARACTER\_LENGTH | COLLATE |
| CONCAT | INSERT | LCASE |
| LEFT | LENGTH | LOCATE |
| LOWER | LTRIM | OCTET\_LENGTH |
| POSITION | REPEAT | REPLACE |
| RIGHT | RTRIM | SPACE |
| SUBSTRING | TRIM | UCASE |
| UPPER |  |  |

Table 11-4: String Scalar Functions

   
NOTE: Technically, COLLATE is not a scalar function, but a clause used to coerce a string to a particular collation language.  
 

Miscellaneous Functions

The miscellaneous functions are those that do not fall into one of the other categories. Among other things, they can be used to return the name of the user whose connection the SQL query is being executed over, the name of the database being queried, a unique GUID-based value, several scalar conditional functions, IFNULL(), ISNULL(), and IIF(), as well as some functions that are used in conjunction with full text search. The Advantage miscellaneous SQL scalar functions are listed in Table 11-5.

|  |  |  |
| --- | --- | --- |
| APPLICATIONID | CAST | COALESCE |
| CONTAINS | CONVERT | DATABASE |
| DIFFERENCE | IFNULL | IIF |
| ISNULL | LASTAUTOINC | NEWIDSTRING |
| SCORE | SCOREDISTINCT | SOUNDEX |
| USER |  |  |

Table 11-5: Miscellaneous Scalar Functions