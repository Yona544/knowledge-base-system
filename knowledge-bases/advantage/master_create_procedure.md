CREATE PROCEDURE




Advantage Database Server 12  

[ALTER | CREATE] PROCEDURE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [ALTER | CREATE] PROCEDURE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - [ALTER | CREATE] PROCEDURE Advantage SQL Engine master\_Create\_procedure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| [ALTER | CREATE] PROCEDURE  Advantage SQL Engine |  |  |  |  |

Adds or modifies an Advantage Extended Procedure (stored procedure) definition in the [Advantage Data Dictionary](master_advantage_data_dictionary.htm)

Syntax

[ALTER | CREATE] PROCEDURE <procedure-name>( [params] )

procedure\_definition

 

params ::= param | param, params

 

param ::= <parameter-identifier> <data-type> [OUTPUT] | CURSOR VARYING OUTPUT

 

procedure\_definition ::= script\_procedure\_definition | external\_procedure\_definition

 

script\_procedure\_definition ::= BEGIN script END

 

external\_procedure\_definition ::= FUNCTION <container-function-name> IN (LIBRARY | COMLIBRARY) < AEP-library >

 

Remarks

The CREATE PROCEDURE statement can be used to create a stored procedure that is written in SQL script language and stored entirely in the Advantage Data Dictionary, or it can be used to create a stored procedure (Advantage Extended Procedure) that references a function in an external library.

The ALTER PROCEDURE statement can be used to modify an existing stored procedure. The ALTER PROCEDURE command replaces the stored procedure's existing definition with the new definition.

SQL Script Stored Procedure

To create a stored procedure written in SQL script language and stored the procedure in the Advantage Data dictionary, use the syntax with the script\_procedure\_defintion. The [SQL script](master_sql_script_overview.htm) enclosed between the BEGIN and END token will be stored in the data dictionary. The SQL script will be executed when an EXECUTE PROCEDURE <procedure-name> statement is executed. In the SQL script, the input parameters may be referenced using the \_ParamX, \_ParamY notation, where ParamX and ParamY are the actual names of the input parameters. The parameters may also be referenced using the \_\_input table, however, direct reference using the \_ParamX notation is the most efficient.

The CURSOR VARYING OUTPUT parameter is a special output. It indicates that the stored procedure will return an output cursor with not predetermined structure. There should be only one CURSOR VARYING OUTPUT parameter in the parameter list. If the CURSOR VARYING OUTPUT parameter is specified, there should be no other explicit output parameter. This option is only available to SQL script stored procedure. The last SELECT or EXECUTE STORED PROCEDURE executed in the script will become the output of the stored procedure. The returned cursor may be live or static depending on the last statement executed.

Note A stored procedure with VARYING OUTPUT cannot be used directly in the FROM clause of a SELECT statement, and it cannot be used as the source of a cursor variable in SQL script.

To create a stored procedure that references a function in an external library, use the external\_procedure\_definition syntax. The reference to the external function will be stored in the data dictionary. Advantage SQL engine will load the external library and call the function when the EXECUTE PROCEDURE <procedure-name> statement is executed.

<container-function-name> is the name of the function in the Advantage Extended Procedures file that should be invoked when the procedure named <procedure-name> is executed.

COM and .NET Users

<AEP-library> is the ProgID of your AEP library. This value consists of the project name combined with the class name, and must be surrounded by quotation marks or [] (brackets). For example:

 

CREATE PROCEDURE MyComAEP

( Lastname CHAR(20) )

FUNCTION MyProcedure IN COMLIBRARY "ClassLibrary1.ComClass1"

 

Note Your COM or .NET DLL must be registered on the server that will be executing the extended procedure.

WIN32 and Linux Shared Object Users

<AEP-library> is the file name of the Advantage Extended Procedures file. This file is a Win32 Dynamic Link Library (DLL) or a Linux shared object (so). The default extension is .AEP. If the .AEP file has a different extension or if the file exists in a different directory than the [Advantage Data Dictionary](master_advantage_data_dictionary.htm), then two things must be done. First, the entire name and path must be surrounded with double quotes (") or [] (brackets). Secondly, the path must not contain drive letters. The SQL statement and the stored procedure are run from the Advantage Database Server. The file server where the Advantage server is running will not have the same drive mappings. Always use a relative path or a UNC path. An example relative path would be:

Assume the data dictionary file is located at \\server1\datashare\database\sample.add

Assume the stored procedure file named SP.AEP is located at \\server1\datashare\database\stored\_procs\sp.aep

The relative path is stored\_procs\sp.aep or \stored\_procs\sp.aep

The keyword OUTPUT indicates that the parameter is an output parameter. Other parameters are input parameters. Input parameters must be supplied in the EXECUTE PROCEDURE call and are passed to the stored procedure. If the stored procedure definition has output parameters, the EXECUTE PROCEDURE call will result in an opened cursor that contains the output parameter values in columns. The cursor may consist of multiple rows.

The CREATE PROCEDURE statement can only be executed by a user with CREATE PROCEDURE permissions.

The ALTER PROCEDURE statement can only be executed by a use with the ALTER permission to the stored procedure.

Examples

CREATE PROCEDURE BeginTransaction()

FUNCTION BeginTransaction IN LIBRARY "Example4StoredProc.aep"

 

CREATE PROCEDURE CommitTransaction()

FUNCTION CommitTransaction IN LIBRARY "Example4StoredProc.aep"

 

CREATE PROCEDURE RollBackTransaction()

FUNCTION RollBackTransaction IN LIBRARY "Example4StoredProc.aep"

 

CREATE PROCEDURE GetInfoForTable

( RecordCount INTEGER OUTPUT,

MaxEmployeeID INTEGER OUTPUT,

NewestEmployee CHAR(41) OUTPUT,

UniqueLastNameCount INTEGER OUTPUT )

FUNCTION GetInfoForTable IN LIBRARY "Example4StoredProc.aep"

 

CREATE PROCEDURE AddRecordToData

( LastName CHAR(20),

FirstName CHAR(20),

EmpID SHORT,

Married LOGICAL )

FUNCTION AddRecordToData IN LIBRARY "Example4StoredProc.aep"

 

CREATE PROCEDURE MyComAEP

( Lastname CHAR(20) )

FUNCTION MyProcedure IN COMLIBRARY "ClassLibrary1.ComClass1"

// A simple stored procedure implemented using SQL script and

// referencing the variables directly

CREATE PROCEDURE AddRecordToTables

 (

 LastName VARCHAR(20),

 FirstName VARCHAR(20),

 Married LOGICAL

 )

BEGIN

 IF NOT \_Married THEN

   INSERT INTO Singles( lastname, firstname ) VALUES ( \_LastName, \_FirstName );

 ELSE

   INSERT INTO Couples( lastname, firstname ) VALUES ( \_lastName, \_Firstname );

 END;

END;

// A simple stored procedure implemented using SQL script and the \_\_input table

CREATE PROCEDURE AddRecordToData2

 (

 LastName CHAR(20),

 FirstName CHAR(20),

 EmpID SHORT,

 Married LOGICAL

 )

BEGIN

 INSERT INTO Data( lastname, firstname, empid, married ) SELECT \* FROM \_\_input;

END;

 

// Change the last stored procedure to use AEP

ALTER PROCEDURE AddRecordToData

( LastName CHAR(20),

FirstName CHAR(20),

EmpID SHORT,

Married LOGICAL )

FUNCTION AddRecordToData IN LIBRARY "Example4StoredProc.aep";

 

// Create a procedure with varying output

CREATE PROCEDURE WhichTable

 (

 which integer,

 CURSOR VARYING OUTPUT

 )

BEGIN

 IF \_which = 1 THEN

   SELECT \* FROM user1Info;

 ELSE

   SELECT \* FROM userTemplate;

 END;

END;

 

See Also

[sp\_ModifyProcedureProperty](master_sp_modifyprocedureproperty.htm)