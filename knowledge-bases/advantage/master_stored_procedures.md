Stored Procedures




Advantage Database Server 12  

Stored Procedures

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Stored Procedures  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Stored Procedures Advantage Concepts master\_Stored\_procedures Advantage Concepts > Advantage Functionality > Stored Procedures / Dear Support Staff, |  |
| Stored Procedures  Advantage Concepts |  |  |  |  |

A stored procedure is a block of code, either an SQL script or a compiled library, which is executed on the server via explicit calls using EXECUTE PROCEDURE statements.

Why Use a Stored Procedure?

|  |  |
| --- | --- |
| · | Performance All processing is done on the server, no network traffic. |

|  |  |
| --- | --- |
| · | Productivity Developing new interfaces or clients for your application wont require rewriting common code if your common code is contained inside stored procedures. |

|  |  |
| --- | --- |
| · | Scalability Isolating application processing on the server means you can write client applications from any interface that supports executing SQL statements, and are not limited by the data access layers of different development environments. |

|  |  |
| --- | --- |
| · | Maintainability Application logic is isolated in one area, making modifications easier. |

Stored Procedure Containers

Stored procedures can be written as SQL scripts, WIN32 DLLs, COM Objects, Linux shared objects, or .NET Assemblies.

SQL scripts are the recommended container type. Stored procedures written as other libraries are called Advantage Extended Procedures (AEPs). See the [Advantage Extended Procedures](master_advantage_extended_procedures.htm) topic for more details on AEPs.

See the [SQL scripts](master_sql_script_overview.htm) documentation for a full discussion of the Advantage scripting language.

Creating a Stored Procedure

Stored procedures can be created via the [CREATE PROCEDURE](master_create_procedure.htm) statement or visually using the Advantage Data Architect (which is the recommended method). A data dictionary is required to use stored procedures.

When creating a new stored procedure, you define the input and output parameters the procedure will accept. These parameters can be any data type supported by the [ADT table format](master_table_adt.htm).

The input and output parameters are passed to the stored procedure via virtual table references with one column per parameter. For example, if you define a new stored procedure with two input parameters, X and Y, then inside your procedure you can access these values by referencing the X any Y columns in a virtual table called \_\_input:

DECLARE localX Integer, localY Integer, localResult Integer;

DECLARE input AS SELECT \* FROM \_\_input;

 

OPEN input;

FETCH input;

 

localX = input.X;

localY = input.Y;

localResult = localX + localY;

 

CLOSE input;

 

A more efficient way of referencing the input parameters is to use the \_ (underscore) notation. With the stored procedure described above with two input parameters, X and Y, the local variables \_X and \_Y are automatically declared and populated with values from the input parameters X and Y during execution. The script may be written as:

DECLARE localResult Integer;

localResult = \_X + \_Y;

 

Similarly, output parameters can be returned by setting their values in a virtual table called \_\_output:

INSERT INTO \_\_output VALUES ( output param one, output param two );

 

The virtual table \_\_output is not limited to one row. Your procedure can return multiple rows, effectively returning a multi-row dataset to the caller, which the caller can manipulate just like any other result set. It should be noted that this result set is returned as a static cursor.

The column structure of the \_\_input and \_\_output tables directly reflects the parameter names and data types you specify when creating the procedure in the data dictionary.

Calling a Stored Procedure

Stored procedures are called by executing EXECUTE PROCEDURE statements via any SQL interface. For example, to call a procedure with two integer parameters you would use the following statement:

EXECUTE PROCEDURE MyProcedureName( 6, 9 )

 

The same procedure could be called using named parameters:

EXECUTE PROCEDURE MyProcedureName( :param1, :param2 )

 

Stored Procedure Privileges

With a database configured to verify user permissions, the "execute" permission is required for a user to execute specific stored procedure. No other user privileges are checked when executing the code inside the stored procedure. This functionality, among other things, lets you hide tables from users, but allow access and modifications to those tables only through stored procedures which the developer can control.

Stored Procedures and Transactions

All operations performed inside of a stored procedure are included in the context of existing transactions. If you roll back a transaction after calling a stored procedure, all data operations performed by that stored procedure will also be rolled back.