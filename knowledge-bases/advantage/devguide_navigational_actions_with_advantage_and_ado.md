Navigational Actions with Advantage and ADO




Advantage Database Server 12  

     Navigational Actions with Advantage and ADO

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Navigational Actions with Advantage and ADO  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Navigational Actions with Advantage and ADO Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Navigational\_Actions\_with\_Advantage\_and\_ADO Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > Navigational Actions with Advantage and ADO / Dear Support Staff, |  |
| Navigational Actions with Advantage and ADO  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADO supports a number of navigational operations on populated Recordsets, permitting you to leverage Advantage's support for both navigational and set-based SQL data access. This section describes the navigational options made available through server-side cursors. These operations can be performed on any SQL result set that returns a live cursor or any table opened directly.

Unlike most remote relational database servers, Advantage also supports a non-SQL technique for working with a server-side cursor. It involves opening a table directly. When you open a table directly, the Advantage OLE DB Provider obtains a table handle, which permits Advantage to use its high-performance indexes, Advantage Optimized Filters, and read-ahead record caching to supply data to your client application. Fortunately, with live cursors, Advantage also uses these high-performance features.

You open a table directly by setting the CommandText property of a Command object or the Source parameter of a Recordset's Open method to the table name. You then set the CommandType property of the Command, or the Options parameter of the Recordset's Open method, to adCmdTableDirect. This is shown in the following code segment, which is taken from the ShowInvoiceBtn click event:

If AdsRecordset.State = adStateOpen Then  
  AdsRecordset.Close  
End If  
AdsRecordset.Open "INVOICE", AdsConnection, \_  
  adOpenDynamic, adLockPessimistic, adCmdTableDirect  
Set DataGrid1.DataSource = AdsRecordset

It's worth noting that there are some similarities, but also some significant differences between using a CommandType of adCmdTable and adCmdTableDirect. Just as you do when you set CommandType (or Options) to adCmdTableDirect, when you use adCmdTable, you assign the name of the table to the CommandText property of a Command object, or pass the table name in the Source parameter of a Recordset's Open method. In response, the Command or Recordset object generates a SELECT \* FROM query. Queries like these return a live, server-side cursor (so long as you did not specifically request a client-side cursor), which enables the use of the table's indexes for searching, filtering, and the like.

By comparison, when you set CommandType (or Options) to adCmdTableDirect, the Advantage SQL engine is bypassed altogether, instead opening the table using an OLE DB Rowset object. Opening a table this way enables additional capabilities, including being able to obtain an exclusive lock on the table, which cannot be done through a SQL SELECT statement.

Performing navigational actions on server-side cursors is described in the following sections.

   
NOTE: The Advantage OLE DB Provider also supports high-performance bookmarks on server-side cursors. For information on using bookmarks, see the Advantage help.