Using the LIKE Operator




Advantage Database Server 12  

Using the LIKE Operator

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using the LIKE Operator  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using the LIKE Operator Advantage SQL Engine master\_Using\_the\_like\_operator Advantage SQL > SQL Functionality > Using the LIKE Operator / Dear Support Staff, |  |
| Using the LIKE Operator  Advantage SQL Engine |  |  |  |  |

The SQL LIKE operator provides pattern matching capability in a WHERE clause. It allows, for example, a character field to be compared against a pattern matching string that can contain wild card characters. The wild card characters are '%' (percent) and '\_' (underscore). The '%' character matches 0 or more characters, and the '\_' matches exactly one character. For example, the statement

SELECT \* FROM emp WHERE lastname LIKE 'S%'

will select all rows from the table where the lastname field starts with the character 'S'. The pattern 'S\_o%' would match all rows from the table where the lastname field starts with the character 'S' and has 'o' as the third character. The pattern '%x%' would match all rows where the lastname contains the character 'x'.

The use of the LIKE operator in a statement results in static cursor. If the field that is used in the expression is indexed, then the query can be optimized as long as the pattern does not begin with either wild card character (% or\_). For example, the pattern 'Sm%' would make use of an existing index to restrict the range of records to those where the field begins with 'Sm'. The pattern '%row%' would not make use of any indexes because it requires a generic search of the field for the characters 'row'.

An escape character can be defined with the ESCAPE clause. If an escape character is specified before either of the wild card characters ( '%' or '\_' ) in the LIKE pattern, the Advantage SQL Engine will perform an exact match on that character. In other words, an escaped wild card character is no longer a wild card, but instead just a normal character. Also, the escape character itself may be escaped by itself in order to perform an exact match on the escape character. Specifying an escape character before any other character has no effect. Specifying more than one character in the escape clause results in a parsing error.

Here's an example which finds records containing '80% Discount':

SELECT promotion FROM sales WHERE promotion LIKE '%80@% Discount%' ESCAPE '@'

This example will find records containing '80% @ 10,000'

SELECT flow FROM watertable WHERE flow LIKE '80@% @@ 10,000' ESCAPE '@'