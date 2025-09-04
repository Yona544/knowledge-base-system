Modularizing Operations with Views




Advantage Database Server 12  

     Modularizing Operations with Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Modularizing Operations with Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Modularizing Operations with Views Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Modularizing\_Operations\_with\_Views Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Modularizing Operations with Views / Dear Support Staff, |  |
| Modularizing Operations with Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

One reason for creating a view that selects from a view is that it permits you to break up data operations into manageable modules. For example, you may have a view that performs a calculation for each record in a table. You can then create another view that performs an aggregation, such as a SUM operation, on the calculation performed by the first view. This view, in turn, can be used in a third query to perform additional manipulation.

One of the advantages to this approach is that some views may get used over and over by other views.

The following steps demonstrate how to create views that are used by other views:

1.        From the DemoDictionary connection, right-click the VIEWS node and select Create. The View dialog box (shown in Figure 6-1) is displayed.

|  |  |
| --- | --- |
| 2. | Set Name to Sum by Invoice. |

|  |  |
| --- | --- |
| 3. | Enter the following SQL statement in the View SQL section: |

SELECT SUM(Quantity \* Price) as [Inv Total],   
  [Invoice No] FROM ITEMS   
  GROUP BY [Invoice No]

4.        Click OK to save this new view.

|  |  |
| --- | --- |
| 5. | Right-click VIEWS again and select Create. |

|  |  |
| --- | --- |
| 6. | Set Name to Sales by Employee. |

|  |  |
| --- | --- |
| 7. | Enter the following SQL statement in the View SQL section: |

SELECT SUM(SInv.[Inv Total]) as [Total Sales],   
    Inv.[Employee ID],Emp.[First Name],   
    Emp.[Last Name]  
  FROM [Sum by Invoice] SInv, INVOICE Inv,   
    EMPLOYEE Emp  
  WHERE SInv.[Invoice No] = Inv.[Invoice No] AND  
    Inv.[Employee ID] = Emp.[Employee Number]  
  GROUP BY Inv.[Employee ID], Emp.[Last Name],  
    Emp.[First Name]

8.        Click OK to save this view.

|  |  |
| --- | --- |
| 9. | Right-click Views once more and select Create. |

|  |  |
| --- | --- |
| 10. | Set Name to Purchases by Customer. |

|  |  |
| --- | --- |
| 11. | Enter the following statement in the View SQL section: |

SELECT SUM(SInv.[Inv Total]) as [Total Purchases],  
    Inv.[Customer ID],Cust.[First Name],   
    Cust.[Last Name]   
  FROM [Sum by Invoice] SInv,INVOICE Inv,   
    CUSTOMER Cust  
  WHERE SInv.[Invoice No] = Inv.[Invoice No] AND  
    Inv.[Customer ID] = Cust.[Customer ID]  
  GROUP BY Inv.[Customer ID], Cust.[Last Name],   
    Cust.[First Name]

12.        Click OK to save the view. You should now see four views under the VIEWS node, as shown in Figure 6-8.

Figure 6-8: Your new views appear in the VIEWS node of the DemoDictionary connection

13.        Now, execute the Sales by Employee view by double-clicking its node. The results, shown in Figure 6-9, are displayed in the Table Browser. Close the Table Browser when you are done inspecting the data.

Figure 6-9: This result set involved the execution of two views

14.        Now right-click the Purchases by Customer view node. Select Open to display this data in the Table Browser. Close the Table Browser when you are done.

|  |  |
| --- | --- |
| 15. | Take a moment now to grant Select access rights to the three views that you just created to the ReadWrite group. It is not necessary to enable any further rights, since the use of aggregate operations and joins in these views renders them readonly. |

This example demonstrates the modular aspect of views. Both the Sales by Employee and the Purchases by Customer views select data from the Sum by Invoice view. If one or more future views also need to work with the summary data in the Sum by Invoice view, they can easily select from it.

   
NOTE: Views that query views may execute more slowly than a single complicated view. If performance is important for your application, you may want to compare the performance of your views with alternative data access mechanisms, such as SQL queries, stored procedures, and scopes (ranges).