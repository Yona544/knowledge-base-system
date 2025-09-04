Testing FTS Index Orders




Advantage Database Server 12  

     Testing FTS Index Orders

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Testing FTS Index Orders  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Testing FTS Index Orders Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Testing\_FTS\_Index\_Orders Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Testing FTS Index Orders / Dear Support Staff, |  |
| Testing FTS Index Orders  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

FTS index orders, unlike the expression-based indexes you created earlier in this chapter, are only used for filtering records, and not for sorting data. Therefore, you test an FTS index by setting filters and executing queries. The following steps demonstrate how to test an FTS-based filter:

With the CUSTOMER.ADT table open in the Table Browser, enter contains(Notes, birthday or anniversary) in the field below the Set Filter button and click Set Filter. (Note that the word Notes in the CONTAINS function is the name of the field on which to perform a full text search. It is not the index name.)

The Table Browser responds by displaying only those records whose Notes field contains the words birthday or anniversary or both. You can double-click the Notes field to examine the memo and verify that at least one of the search words is present. You will also notice that the green circle appears, indicating that this is a fully optimized filter. Click Clear Filter.

Change the filter to contains(\*, train\*) and click Set Filter.

Once again a green circle indicates that an optimized FTS index was used. In this case, the first asterisk (\*) instructed Advantage to use all FTS indexes available for this table in its search. Since there was only one FTS index, this had the same effect as when you specified the Notes field explicitly. Click Clear Filter.

Finally, try searching on a field for which there is no FTS index order. Enter contains(Last Name, zap\*) in the filter field and click Set Filter. This time the red circle indicates that a nonoptimized filter was used. In this case, Advantage searched the Last Name field record-by-record to locate the matching values.

The preceding example demonstrated how to test FTS filters. Use the following steps to demonstrate the use of FTS indexes in SQL SELECT statements:

Begin by closing the Table Browser for the CUSTOMER.ADT table.

Using the Windows Explorer, copy the three files, CUSTOMER.ADT, CUSTOMER.ADM, and CUSTOMER.ADI, from the c:\AdsBook directory to the c:\AdsBook\FreeTabs directory. Next rename each of these copies to CUST1.ADT, CUST1.ADM, and CUST1.ADI.

Right-click the Tables node of the FreeTableConnection in the Connection Repository and select Refresh List from the displayed context menu. The CUST1.ADT node should now appear under the TABLES node in the FreeTableConnection connection.

Next, Select Tools | SQL Utility from the Advantage Data Architect main menu. The SQL Utility should now be connected using the FreeTableConnection connection.

Enter the following SQL statement in the SQL Editor pane located at the top-left corner of the Native SQL Utility (make sure it is the only entry):

SELECT \* FROM CUST1 WHERE CONTAINS(Notes, 'birthday NEAR card')

Click the Execute SQL button. Two records are returned, as shown in Figure 3-8.

Now, edit the SQL statement to look like the following:

SELECT \* FROM CUST1 WHERE CONTAINS(Notes, 'birthday')   
  and SCORE(Notes, 'birthday') > 1

Click the Execute SQL button again. This time only records where the word birthday appears more than once are displayed. Close this window.

Figure 3-8: A SQL query using full text search in the Native SQL Utility