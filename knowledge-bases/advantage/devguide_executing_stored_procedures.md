Executing Stored Procedures




Advantage Database Server 12  

     Executing Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Executing Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Executing Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Executing\_Stored\_Procedures Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > Executing Stored Procedures / Dear Support Staff, |  |
| Executing Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You execute system stored procedures using the SQL EXECUTE PROCEDURE keywords. You follow these keywords with the name of the stored procedure, and the stored procedure's input parameters enclosed in parentheses. For example, the following query sets the password of the data dictionary's administrative account to the word password:

EXECUTE PROCEDURE sp\_ModifyDatabase('ADMIN\_PASSWORD',  
  'password')

If a stored procedure includes an input parameter, but supplying a value for that parameter is optional, you can simply pass the value NULL. This is demonstrated in the following stored procedure invocation, which creates a new group but does not set the group's description:

EXECUTE PROCEDURE sp\_CreateGroup('accounting', NULL)

Some development environments have special objects or special properties that permit you to specifically execute a stored procedure, as opposed to executing a query that invokes a stored procedure. For example, in the .NET framework you can set the CommandType property of an IDBCommand implementing object to the value System.Data.CommandType.StoredProcedure. Once you do this, you can then assign the name of the stored procedure to the CommandText String property, as well as define any required parameters.

The following C# code segment demonstrates how the invocation of sp\_ModifyDatabase might look when invoked using an AdsCommand object:

connection1.Open();  
command1 = connection1.CreateCommand();  
command1.CommandType = CommandType.StoredProcedure;  
command1.CommandText = "sp\_ModifyDatabase";  
command1.Parameters.Add(1, System.Data.DbType.String);  
command1.Parameters.Add(2, System.Data.DbType.String);  
command1.Parameters[0].Value = "ADMIN\_PASSWORD";  
command1.Parameters[1].Value = "password";  
command1.ExecuteNonQuery();

Similarly, the Advantage TDataSet Descendant for Delphi has a TStoredProc component. For this component, you set the StoredProcName property to the name of the stored procedure and set any required parameters. You then call Open (if the stored procedure returns a result set) or ExecSQL (if no result set is returned).

The following sections organize the available system stored procedures into four categories: usage information and control, data dictionary management, table maintenance, and general information.