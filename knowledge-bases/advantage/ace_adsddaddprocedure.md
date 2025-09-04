AdsDDAddProcedure




Advantage Database Server 12  

AdsDDAddProcedure

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDAddProcedure  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDAddProcedure Advantage Client Engine ace\_Adsddaddprocedure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDAddProcedure  Advantage Client Engine |  |  |  |  |

Adds a stored procedure definition to the data dictionary.

Syntax

UNSIGNED32 AdsDDAddProcedure( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucName,

UNSIGNED8 \*pucContainer,

UNSIGNED8 \*pucProcName,

UNSIGNED32 ulInvokeOption,

UNSIGNED8 \*pucInParams,

UNSIGNED8 \*pucOutParams,

UNSIGNED8 \*pucComments );

 

UNSIGNED32 AdsDDAddProcedure100( ADSHANDLE hAdminConn,

 UNSIGNED8 \*pucName,

 WCHAR     \*pwcContainer,

 UNSIGNED8 \*pucProcName,

 UNSIGNED32 ulInvokeOption,

 UNSIGNED8 \*pucInParams,

 UNSIGNED8 \*pucOutParams,

 UNSIGNED8 \*pucComments );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Data dictionary connection handle. |
| pucName (I) | The stored procedure data dictionary name. |
| pucContainer (I) | The Advantage Extended Procedure (.AEP) container file name, .NET assembly name, or SQL script depending on the ulInvokeOption Parameter. If this value is the .AEP container file name, it must be a relative path from the Advantage Data dictionary (.ADD) file. |
| pucProcName (I) | The procedure name within the Advantage Extended Procedure (AEP) container to be executed when the procedure name in pucName is called. This parameter is ignored if the ulInvokeOption is ADS\_SCRIPT\_PROC. |
| ulInvokeOption (I) | This value determines the format of the stored procedure. The values allowed for this parameter are ADS\_STORED\_PROC, ADS\_COMSTORED\_PROC, and ADS\_SCRIPT\_PROC.  ADS\_STORED\_PROC is used when creating a stored procedure using a WIN32 DLL or Linux shared object.  ADS\_COMSTORED\_PROC is used when creating a COM or .NET stored procedure.  ADS\_SCRIPT\_PROC is used when the stored procedure is completely defined using an [Advantage SQL script](master_sql_script_overview.htm) and specified in the pucContainer parameter. |
| pucInParams (I) | The definition of the input parameters for the stored procedure. The format of this string is the same as the string passed into [AdsCreateTable](ace_adscreatetable.htm) to define the new fields in the table. This definition will be used to create a table that will be populated with the input values. This new table will be passed to the stored procedure. The stored procedure reads the input parameters from this table. If the stored procedure has no input, use NULL. |
| pucOutParams (I) | The definition of the output parameters. The format of this string is the same as the pucInParams. This definition will be used to create a table that will be passed to the stored procedure. The stored procedure will populate this table without its output. If the stored procedure has no output, use NULL. |
| pucComments (I) | The description of the stored procedure. |

Remarks

AdsDDAddProcedure may be used to add stored procedure definitions to the Advantage Data Dictionary. An easier method of adding a stored procedure would be to use the "CREATE PROCEDURE" SQL syntax or by using Advantage Data Architect.

Note that the only method of executing a stored procedure is through the SQL syntax "EXECUTE PROCEDURE".

CREATE PROCEDURE permissions are required to add a stored procedure to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetCode = AdsConnect60( "x:\\addfiles\\sampledb.add",

ADS\_LOCAL\_SERVER,

"ADSSYS",

NULL,

ADS\_DEFAULT,

&hDict );

ulRetCode = AdsDDAddProcedure( hDict,

"StoredProcName1",

"x:\\Example4StoredProc",

"SP1",

ADS\_STORED\_PROC, "param1,integer;param2,char,30",

"output,char,50",

"Stored procedure #1" );

 

Example 2: Creating a stored procedure using SQL Script.

The procedure creates a table if it does not exist.

ulRetCode = AdsConnect60( "x:\\addfiles\\sampledb.add",

ADS\_LOCAL\_SERVER,

"ADSSYS",

NULL,

ADS\_DEFAULT,

&hConn );

 

ulRetCode = AdsDDAddProcedure( hDConn,

"CreateMyTable", // Name of the procedure

"DECLARE usExists logical;"

"DECLARE curs CURSOR AS SELECT TableType FROM system.Tables WHERE Name = 'MyTable'"

"usExists = FALSE;"

"OPEN curs; IF FETCH curs THEN usExists = TRUE END;"

"CLOSE curs;"

"IF usExists = FALSE THEN"

" CREATE TABLE myTable( id integer, info char(30));"

"ENDIF;"

NULL, // Ignored

ADS\_SCRIPT\_PROC, NULL, NULL,

"Create table if not exist" );

ulRetCode = AdsCreateSQLStatement( hConn, &hStmt );

ulRetCode = AdsExecuteSQLDirect( hStmt, "EXECUTE PROCEDURE CreateMyTable()", NULL );

See Also

[AdsDDRemoveProcedure](ace_adsddremoveprocedure.htm)

[AdsDDGetProcedureProperty](ace_adsddgetprocedureproperty.htm)

[AdsDDSetProcedureProperty](ace_adsddsetprocedureproperty.htm)