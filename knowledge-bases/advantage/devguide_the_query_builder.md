The Query Builder




Advantage Database Server 12  

     The Query Builder

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The Query Builder  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      The Query Builder Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_The\_Query\_Builder Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > The Query Builder / Dear Support Staff, |  |
| The Query Builder  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Advantage Query Builder is a handy little utility for creating basic SQL SELECT statements. It provides a graphical user interface (GUI) that permits you to select fields and join tables visually. You can use this visual depiction to generate a SQL SELECT statement, which you can then test.

The following steps demonstrate how to use the Advantage Query Builder:

Make sure that the DemoDictionary connection is connected and is the active connection.

Select Tools | Query Builder from the Advantage Data Architect main menu. The Advantage Data Architect responds by displaying the QBuilder dialog box, shown in Figure 11-4.

Figure 11-4: The QBuilder dialog box

The Advantage Query Builder contains four sections. The table list in the right-hand pane contains all tables and views in your data dictionary (for which your connection user has rights). The bottom pane contains the work area where you will refine and display the query, the large section in the middle of the Query Builder contains the modeling area, and there is a toolbar along the top.

Begin your query by dragging one or more tables or views into the modeling area. In this case, first drag the CUSTOMER table into the modeling area, and then drag the INVOICE table. Each table appears as a window in the modeling area. Each window contains an asterisk, as well as a row for each field in the table.

To select fields, you click to the left of the \* to select all fields from that table, or you click to the left of individual field names to select specific fields. When a field is selected, a checkmark appears to the left of the field, and the field name appears in the Columns tab of the work area. Select the Customer ID, First Name, and Last Name fields from the CUSTOMER table, and the Invoice No, Employee ID, and Invoice Date fields from the INVOICE table.

If you have added two or more tables to the work area, you need to join them. To join two tables, drag from the field on which you want to link from one table, and drop it onto the corresponding field in the table to which you want to link. In this case, click the Customer ID field in the CUSTOMER table, and while keeping the mouse button depressed, drag to the Customer ID field of the INVOICE table, and then release the mouse button. A line will connect the two fields in the modeling area, as shown in Figure 11-5.

Figure 11-5: The CUSTOMER and INVOICE tables are linked in the Query Builder

You perform the rest of the configuration, if needed, using the work area. If you want the query to sort by one or more fields, right-click the Sort row for those fields and select either Ascending or Descending, depending on which direction you want to sort by. In this case, right-click the Sort row for the Customer ID column, and select Ascending.

If you want to calculate an aggregate statistic, right-click the Function row associated with the field you want to aggregate across, and select one of the available functions. If you use an aggregate function, you need to group by the fields across which you want the aggregate calculated. To group on fields, right-click on the Group row for the fields you want to group on and select Group. (You right-click and select Group again to toggle this option off.) In this example, we are not going to use aggregate functions or groups.

When you are ready to create your query, click the Generate SQL button in the Query Builder toolbar (or press Ctrl-G). The Query Builder examines your model, and then displays the generated SQL in the SQL pane of the work area, as shown in Figure 11-6.

Figure 11-6: The generated SQL appears in the SQL pane of the Query Builder

You can use the generated SQL in the SQL pane as is, or you can make changes to it, if necessary. To test the query that appears in the SQL pane of the work area, click the Execute button in the toolbar. The query result will appear in the results pane of the work area, as shown in Figure 11-7.

Figure 11-7: Use the Execute button (or press Ctrl-E) to execute the SQL in the SQL pane

   
NOTE: When you link tables, the join produced by the Advantage Query Builder is based on the left-to-right order of the tables in the modeling area.  
 

If your model is a complicated one, and you want to work with it again later, you can click the Save Model button in the toolbar. To open a previously saved model, click the Open Model button in the toolbar.

After using the Query Builder to create a SQL statement, copy the text of the SQL from the SQL pane of the Query Builder into the Windows clipboard. You can then paste it wherever you need it.

While the Advantage Query Builder is a nice utility for creating relatively simple SELECT statements, it is limited. For complicated queries, including those that include subqueries or joins (LEFT, OUTER, and so forth), you must either write those queries manually or use some other query generating tool.