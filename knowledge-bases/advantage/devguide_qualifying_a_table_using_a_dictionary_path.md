Qualifying a Table Using a Dictionary Path




Advantage Database Server 12  

     Qualifying a Table Using a Dictionary Path

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Qualifying a Table Using a Dictionary Path  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Qualifying a Table Using a Dictionary Path Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Qualifying\_a\_Table\_Using\_a\_Dictionary\_Path Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Qualifying a Table Using a Dictionary Path / Dear Support Staff, |  |
| Qualifying a Table Using a Dictionary Path  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You might recall that in Chapter 2 you created a free table called CUST.ADT. Imagine that instead of being a free table, CUST.ADT was in a data dictionary other than DemoDictionary. For example, suppose that CUST.ADT was stored in a data dictionary named Shared.ADD.

   
NOTE: You are free to create a data dictionary with this name and add the CUST.ADT table to it. This would permit you to try linking to another data dictionary using a view. However, when you are done, remove CUST from that data dictionary. You remove a table from a data dictionary by right-clicking the table's node in the Advantage Data Architects tree view and selecting Delete, and then selecting Yes to confirm that you want to remove the table from the data dictionary. Note that selecting Delete just removes the table from the data dictionary. It does not delete the table (or the corresponding index and memo files).  
 

If the Shared.ADD data dictionary is located in the same directory as DemoDictionary, you can use CUST.ADT by preceding the CUST table name with the name of the Shared.ADD data dictionary, enclosed in double quotation marks and separated from the table name using a period. This is demonstrated in the following SQL statement:

SELECT "Customer ID", "First Name", "Last Name"   
  FROM "Shared.ADD".CUST

Of course, this view could include links between tables in the Shared and DemoDictionary data dictionaries, as shown in this example:

SELECT CDB."Customer ID", CDB."First Name", CDB."Last Name",  
    Cust."Address", Cust."City", Cust."State"  
  FROM "Shared.ADD".CUST CDB, CUSTOMER Cust  
  WHERE CDB."Customer ID" = Cust."Customer ID"

If the data dictionaries are not in the same directory, the reference to the data dictionary table must include the path to the data dictionary (this path can be a relative path or a fully qualified path). For example, if Shared.ADD is not in the same directory as DemoDictionary, instead residing in the directory C:\MyData, the preceding view could have to be represented as follows:

SELECT CDB."Customer ID", CDB."First Name", CDB."Last Name",  
    Cust."Address", Cust."City", Cust."State"  
  FROM "C:\MyData\Shared.ADD".CUST CDB, CUSTOMER Cust  
  WHERE CDB."Customer ID" = Cust."Customer ID"

When you include a data dictionary name as the qualifier for an external database table, Advantage uses the user name and password of the connection from which the view is being accessed to connect to the external data dictionary. If you cannot ensure that the external data dictionary includes user names and passwords for all users who will access the view, you must use a data dictionary link. Using data dictionary links is discussed in the following section.

   
NOTE: A free table can also be included in a query using a relative path or a fully qualified path. In fact, if the free table is in the same directory as the data dictionary, a free table can be referred to without a path, as though it were bound to the data dictionary.