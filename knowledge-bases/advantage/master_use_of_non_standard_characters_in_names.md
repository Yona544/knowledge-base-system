Use of Non-Standard Characters in Names




Advantage Database Server 12  

Use of Non-Standard Characters in Names

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Use of Non-Standard Characters in Names  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Use of Non-Standard Characters in Names Advantage SQL Engine master\_Use\_of\_non-standard\_characters\_in\_names Advantage SQL > SQL Functionality > Use of Non-Standard Characters in Names / Dear Support Staff, |  |
| Use of Non-Standard Characters in Names  Advantage SQL Engine |  |  |  |  |

Character constants in SQL statements must be delimited by single quotes. See SQL Literals for information about character constants.

Double quotes and [] (brackets) are used to delimit identifiers that contain non-alphanumeric characters or that start with numbers. For example, if a database contains a table name or column name that starts with a number, contains spaces, or that has non-alphanumeric characters, the application must enclose the name in double quotes or [] (brackets) (e.g., "3D", "Contact Date", "l/c", [Full Name]). Also, full path names or table names that include extensions must be enclosed in double quotes or [] (brackets) (e.g., "x:\pathname\table", "\\server\volume\path\table", "table.abc", "..\otherdir\table").

In a typical application, tables are often located in a single directory, and the tables have the standard extensions (".dbf" or ".adt"). If this is the case, applications can use that location as the connection path and then refer to all tables with just the base table name (e.g., employee, customer, orders, etc.). To refer to tables that reside in locations other than the connection path, or have non-standard file extensions, applications must use full or relative paths enclosed in double quotes or [] (brackets).

Reserved SQL keywords that are used as column or table names must be enclosed in double quotes or [] (brackets). For example, USER is a reserved SQL keyword. To create a table with a column named USER, it must be enclosed in double quotes or [] (brackets):

CREATE TABLE sysman (id INTEGER, "user" CHAR(20))

SELECT \* FROM sysman WHERE "USER" = 'Tom'

UPDATE Employees SET [Last Name] = 'Johnson' WHERE [Emp ID] = 5

 

See [Reserved Keywords](master_reserved_keywords.htm) for a list of keywords that are reserved by the Advantage SQL engine.