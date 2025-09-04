Scanning a Result Set




Advantage Database Server 12  

     Scanning a Result Set

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Scanning a Result Set Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Scanning\_a\_Result\_Set\_2 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > Scanning a Result Set / Dear Support Staff, |  |
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning is the process of sequentially reading every record in a result set, or every record in the filtered view of the result set if a filter is active. In most cases, scanning involves an initial navigation to the first record of the result set, followed by repeated calls to advance one record until all of the records have been visited.

Although scanning is a common task, it is important to note that it necessarily requires the client application to retrieve all of the records in the result set.

When using a client-side cursor, all records must be retrieved to the client before any action can be taken. However, once retrieved, the scanning process itself is very fast. By comparison, when using a server-side cursor, the records are read to the client during the scanning process. Consequently, scanning can initiate faster but may take longer when using a server-side cursor.

   
TIP: If you are using ADS, and you must scan a large number of records, implement the operation using a stored procedure as described in Chapter 7. When the server and the data reside on the same machine, scanning from a stored procedure installed on ADS requires no network resources.  
 

The following code demonstrates scanning records in a Recordset. This code, associated with the click subprocedure of the List Products button (shown in Figure 17-1), navigates the entire PRODUCTS table, assigning data from each record to the ProductList list box:

If AdsRecordset.State = adStateOpen Then  
  AdsRecordset.Close  
End If  
AdsRecordset.Open "SELECT \* FROM PRODUCTS", AdsConnection, \_  
  adOpenDynamic, adLockPessimistic, adCmdText  
ProductList.Clear  
AdsRecordset.MoveFirst  
While Not AdsRecordset.EOF  
  ProductList.AddItem (AdsRecordset.Fields(0).Value & \_  
    vbTab & AdsRecordset.Fields(1).Value)  
  AdsRecordset.MoveNext  
Wend  
AdsRecordset.Close

   
NOTE: You can improve the performance of scanning operations by using ForwardOnly cursors, which are optimized for forward navigation.