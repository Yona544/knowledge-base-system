USER DEFINED FUNCTION




Advantage Database Server 12  

USER DEFINED FUNCTION

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| USER DEFINED FUNCTION  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - USER DEFINED FUNCTION Advantage SQL Engine master\_User\_defined\_function Advantage SQL > SQL Functionality > USER DEFINED FUNCTION / Dear Support Staff, |  |
| USER DEFINED FUNCTION  Advantage SQL Engine |  |  |  |  |

User Defined Functions (UDFs) allow a developer to create reusable functions that can be used in an SQL statement or SQL script just like existing system scalar functions. By encapsulating frequently performed or complex operations into user defined functions, SQL statements or scripts become easier to write, understand, and debug. In a sense, UDFs make it possible to extend the functionality of the SQL engine.

UDFs also make it simpler for developers to alter the behavior of their application without recompiling. For example, different countries in the world have different formats for displaying monetary data. Instead of creating separate versions of SQL statements for each country, the developer can have one version of the SQL statement that utilizes a UDF to perform the transformation of the monetary data into character format. By either making the UDF return different character strings based on an environment variable or deploying different implementations of the same UDF to different countries, the application can present the monetary data in the correct format.

Advantage Database Server supports the concept of Function Packages to provide independent name spaces for the functions. This allows developers to deploy UDFs into an existing database without worrying about name conflicts.

See Also

[ALTER FUNCTION](master_alter_function.htm)

[CREATE FUNCTION](master_create_function.htm)

[CREATE PACKAGE](master_create_package.htm)

[DROP FUNCTION](master_drop_function.htm)

[DROP PACKAGE](master_drop_package.htm)