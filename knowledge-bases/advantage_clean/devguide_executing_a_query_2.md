---
title: Devguide Executing A Query 2
slug: devguide_executing_a_query_2
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_executing_a_query_2.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: aea2161b8f6fef6bea8ce9ee0f91b536cccdf5fb
---

# Devguide Executing A Query 2

Executing a Query

     Executing a Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You execute a query that returns a result set by calling the Open procedure of a Recordset. This procedure has five optional parameters. The first is the command you want to execute. This can be either a Command object, the name of a table or stored procedure, or (as in the case in the following code segment) the actual text of the query. The second parameter is the connection over which the query will be executed.

The third parameter identifies the type of cursor that you want returned, and the fourth specifies the type of record locking you want. The fifth and final parameter identifies what kind of command you pass in the first parameter. If you pass a table name in the first parameter, you can pass the value adCmdTable in this fifth parameter, and a SELECT \* FROM query will be generated. If you pass the name of a stored procedure that takes no input parameters in the first parameter, an EXECUTE PROCEDURE statement is generated if adCmdStoredProc is given as the fifth parameter.

The following code demonstrates the execution of a query entered by the user into the TextBox named SELECTText. This subprocedure is associated with the Execute SELECT button shown in Figure 17-1:

If AdsRecordset.State = adStateOpen Then  
    AdsRecordset.Close  
End If  
   
AdsRecordset.Open SELECTText.Text, AdsConnection, \_  
  adOpenDynamic, adLockPessimistic, adCmdText  
Set DataGrid1.DataSource = AdsRecordset

This code begins by verifying that the Recordset is not currently open, by checking its State property. Next, the query is executed and the returned records are assigned to the Recordset. Finally, the Recordset is assigned to the DataSource property of the DataGrid. The effects of executing this code are shown in Figure 17-4.

Figure 17-4: Records returned from a query are displayed in a data grid

If you need to execute a query that does not return a Recordset, use a Command object. The use of a Command object to execute a query that does not return a Recordset is demonstrated later in this chapter.
