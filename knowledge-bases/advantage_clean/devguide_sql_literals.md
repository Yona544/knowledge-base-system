---
title: Devguide Sql Literals
slug: devguide_sql_literals
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_sql_literals.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: d73906e447b095c8c1649a07a58891e068866dde
---

# Devguide Sql Literals

SQL Literals

     SQL Literals

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| SQL Literals  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Literals are explicit representations of data in expressions. They are used in SQL statements to represent data that does not change. How you specify a literal depends on the type of expression. String literals, for example, are enclosed in single quotation marks. Integer literals, by comparison, are numerals without delimiters. Consider the following statement:

SELECT \* FROM INVOICE  
  WHERE [Invoice Due Date] > [Invoice Date] + 60

In this query, all invoices where customers were given more than 60 days to pay are selected. The 60 in this query is a literal integer value.

The following is an example of a query with a string literal:

SELECT "Customer ID" FROM CUSTOMER  
  WHERE State = 'CA'

This query selects the Customer ID field from the CUSTOMER table for all customers whose State field contains an exact match to the characters CA.

There are six literal types that you can use in Advantage SQL statements. These are Boolean, date, numeric, string, time, and timestamp. The rules for representing these literals are described in the following sections.

Boolean Literals

The Boolean value True is represented as 1 and a Boolean False is represented as 0. You can use the keywords TRUE instead of 1 and FALSE instead of 0.

Date Literals

Literal date values are enclosed in single quotes, and use the current date format setting (the default is mm/dd/ccyy) or the ANSI date format (ccyy-mm-dd), which will always work in Advantage regardless of the current date format setting. Unless you use the default or ANSI setting, you set this format for your client applications programmatically using the ACE API AdsSetDateFormat function, or the Advantage TDataSet Descendant's TAdsSettings DateFormat property.

You can change the date format used for viewing data in the Advantage Data Architect by selecting Tools | ARC Settings from the main menu, which displays the ARC Settings dialog box. Note that this will not change the date format used in your applications. Look at a date field in the Table Browser to determine the current date format setting used for viewing dates within the Advantage Data Architect.

Note that you must represent the month and day with two digits (use a leading zero for single digits). For example, if the current date format is ccyy-mm-dd, the correct representation of January 1, 2007, is '2007-01-01'. If your dates appear using the mm/dd/ccyy format, a valid date literal is '04/15/2007'. If dates appear using the ccyy.mm.dd format, you represent the same date using the '2007.04.15' literal.

Numeric Literals

Both integer and floating-point numbers are represented by numerals without delimiters. These numerals may be preceded by either a plus character (+) or a minus character () to denote sign. Floating-point values use a period to separate the whole number part from the decimal part. You cannot use a comma as a decimal point.

When the numbers you need to represent are very large, you can express numeric literals using exponential notation, sometimes referred to as scientific notation. Exponential notation specifies a number using two parts, the mantissa and the exponent. The mantissa is a number with one significant digit and some number of decimals. The exponent denotes the power of 10 to which the mantissa must be raised. Either the letter e or E separates the mantissa and the exponent.

If the exponent is a positive number, it indicates how many positions the decimal point of the mantissa should be shifted to the right; if the exponent is a negative number, it specifies how many decimal places the decimal point should be shifted to the left.

The following values are examples of numeric literals:

1  
1.0  
-3456.43  
3454324.93783628  
7.43e12  
-4.087e6

String Literals

A string literal is a sequence of one or more characters enclosed in single quotation marks. Any printable character can appear in a string literal. However, if your string literal includes the single quotation mark character ('), you precede it with a single quotation mark. The following are examples of string literals:

'Robert "Bob" Jefferson'  
'That''s what I was trying to say'  
'a'  
'San Francisco'

With one exception, string literals are case sensitive. Specifically, the following three string literals are not equivalent: 'advantage', 'Advantage', and 'ADVANTAGE'. The exception is string literals used with the CONTAINS scalar function on case-insensitive FTS (full text search) indexes.

In all other cases, if you want to perform a case-insensitive comparison between a string literal and another string value (either a character field reference, a string expression, or another string literal), you must use the UCASE or LCASE scalar functions to convert both parts of the comparison to a common case. SQL scalar functions are described later in this chapter. (The cicharacter field is case insensitive, so conversion is not necessary when comparing a string to a cicharacter field.)

Time Literals

Time literals are enclosed in single quotation marks, and use one of the following four formats: HH:MM, HH:MM AM (or PM), HH:MM:SS, or HH:MM:SS AM (or PM). If the AM (or PM) is missing from the literal, 24-hour time is assumed. The AM/PM part of time literals is not case sensitive. The following are valid time literals:

'19:10'  
'4:43 AM'  
'9:00:45 pm'  
'22:19:59'

Timestamp Literals

A timestamp literal denotes a specific date and time, and can be accurate to the millisecond. Timestamp literals, like time literals, are enclosed in single quotation marks. The date part of a timestamp uses the date format as defined earlier in the "Date Literals" section. The time part of the timestamp literal uses the 24-hour HH:MM:SS time format, where seconds are required, but may optionally include milliseconds (HH:MM:SS.mmm). The date part and the time part are separated from each other using a single space. If your date format is mm/dd/ccyy, the following are valid stamp literals:

'07/06/2007 04:52:34'  
'12/31/2007 23:59:59.999'

If your date format is ccyy/mm/dd, the following are valid timestamp literals:

'2007/07/06 04:52:34'  
'2007/12/31 23:59:59.999'

The ANSI date format (ccyy-mm-dd) is always supported by Advantage, regardless of the current date format setting. The following are valid timestamp literals regardless of current date format:

'2007-07-06 04:52:34'  
'2007-12-31 23:59:59.999'

Other Literal Types

Not all data types can be represented literally in your SQL statements. For example, there is no raw literal. If you want to include a literal in your SQL statements, but there is no literal for the data you want to represent, you can either convert one of the available literal types to the data type you need or you can use a query parameter. Parameterized queries are discussed later in this chapter.

You perform data type conversions using either the CONVERT or CAST SQL scalar functions. When you invoke CONVERT, you pass two parameters. The first is a literal representation of your data using one of the available literal types, and the second is a SQL data type that you want that literal converted to. For example, the following is how you represent a literal raw value:

CONVERT ('{B54F3741-5B07-11cf-A4B0-00AA004A55E8}',  
  SQL\_BINARY)

The CAST SQL scalar function has a slightly different syntax. When you invoke CAST, you pass the value followed by the AS keyword and then the SQL data type. Importantly, CAST permits you to optionally follow the SQL data type by a value for precision and scale (where applicable). For example, the following statement casts a string literal as a CHAR(20):

CAST( 'Advantage' AS SQL\_CHAR (20))

   
NOTE: CONVERT and CAST are not just for converting literals. They can be used for to convert any type of expression.
