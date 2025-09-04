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
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Scanning a Result Set Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Scanning\_a\_Result\_Set\_3 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Scanning a Result Set / Dear Support Staff, |  |
| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning is the process of sequentially reading every record in a result, or every record in the filtered view of the result set if a filter is active. In ADO.NET, scanning is performed using an AdsDataReader or AdsExtendedReader, which you obtain from an AdsCommand object that contains either a SQL SELECT statement, a table name, or a stored procedure call.

   
TIP: If you are using ADS, and you must scan a large number of records, consider implementing the operation using a stored procedure as described in Chapter 7. Scanning from a stored procedure installed on the same machine on which the data resides requires no network resources.  
 

The following code demonstrates scanning using an AdsDataReader. This code is associated with the List Products button shown in Figure 18-3:

private void listProductsBtn\_Click(object sender,  
  System.EventArgs e) {  
  command.CommandText = "SELECT \* FROM PRODUCTS";  
  dataReader = command.ExecuteReader();  
  while (dataReader.Read()) {  
    productList.Items.Add(dataReader.GetString(0) + "  " +  
      dataReader.GetString(1));  
  }  
  dataReader.Close();  
}