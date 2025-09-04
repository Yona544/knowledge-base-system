Testing Indexes




Advantage Database Server 12  

 

     Testing Indexes

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Testing Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Testing Indexes Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Testing\_Indexes Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Testing Indexes / Dear Support Staff, |  |
| Testing Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can test the indexes that you create using the Table Browser. As you learned earlier in this chapter, the primary features provided by indexes are customized views and high-speed searches (FTS indexes only provide high-speed searches). The Table Browser permits you to test both of these aspects of your indexes.

Use the following steps to test the indexes that you created in the preceding section:

With the CUST.ADT table displayed in the Table Browser, note the natural order of the records.

Using the Order By combo box that appears in the lower-left corner of the Table Browser, select the Customer ID index. Note that the records are displayed sorted by Customer ID, as shown in Figure 3-3, confirming that this index is providing the proper order view.

Figure 3-3: Setting the index to Customer ID sorts the customer records by the Customer ID field

To test the speed aspect of the index, enter Customer ID = 15198 in the field below the button labeled Set Filter. Now click Set Filter. Two things should happen. First, only the record for the customer whose ID field contains the value 15198 will be displayed, as shown in Figure 3-4. Second, a green circle should appear to the right of the Set Filter button. This green circle indicates that the filter used an Advantage Optimized Filter, or AOF. AOFs are one of the important performance-related objects that Advantage can create from indexes. Click Clear Filter to remove the filter.

Now enter Active = False in the field below the button labeled Set Filter, and then click Set Filter. Although a filter is applied, displaying only customers whose accounts are no longer active, the circle to the right of the Set Filter button is red. This red circle indicates that no indexes were used to build this filter. In other words, none of the tables indexes contributed to the location of the matching record. As a result, this operation was much slower than the filter applied in the preceding step. If there were many more records in this table, the difference would have been noticeable. (Note that if the Active Customer index had been an expression index instead of a conditional index, it would have been optimized.) Click Clear Filter to remove the filter.

Figure 3-4: An optimized filter displays a subset of records in the table

Next set Order By to Full Name. Notice that this also provides a sorting of customers, but this one is sorted by first name and then by last name.

Finally, lets test the Active Customers index. Set Order By to Active Customers. As shown in Figure 3-5, the table now appears only to contain customers where the Active field contains the value True. Also note that the records in the displayed view are sorted by Date Account Opened, in descending order.

Figure 3-5: The Active Customer conditional index shows only active customers, sorting these records by Date Account Opened, in descending order

   
TIP: If you double-click on the field below the Set Filter button, the Filter dialog box is displayed. This dialog box provides a larger field for entering filter expressions, making the testing of filter expressions more convenient. You can also save these filter expressions to a text file, which you may want to do when your filter expressions are complicated and you want to reuse them. You are prompted to save when you close the Filter dialog box.