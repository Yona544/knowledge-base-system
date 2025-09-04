The RI Visual Designer




Advantage Database Server 12  

     The RI Visual Designer

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The RI Visual Designer  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      The RI Visual Designer Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_The\_RI\_Visual\_Designer Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > The RI Visual Designer / Dear Support Staff, |  |
| The RI Visual Designer  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The RI Visual Designer is a special viewer that provides you with a graphical representation of the RI relationships within your data dictionary. To open the RI Visual Designer, right-click the RI OBJECTS node of your data dictionary connection and select RI Visual Designer. The RI Visual Designer for the Customer Invoices RI object is shown in Figure 5-6.

Figure 5-6 The RI Visual Designer

   
NOTE: The RI Visual Designer may overlap one or more tables within the Design pane of the RI Visual Designer. You can easily reposition tables by dragging them to new positions with the Design pane.  
 

Tables that participate in RI object definitions appear in the design pane of the RI Visual Designer. Within this pane, a line connects the foreign key index of the child table to the primary index of the parent table.

To view or change the rules for a particular RI object, double-click the RI object name in the Rules section of the RI Visual Designer.

Creating RI Objects Using the RI Visual Designer

In addition to permitting you to view and modify RI objects, you can actually create new RI objects using the RI Visual Designer. Use the following steps to create an RI relationship between the Invoice and Employee tables:

Begin by arranging the CUSTOMER and INVOICE tables in the Design pane of the RI Visual Designer so that you can see both tables easily. Resize the INVOICE table display so that you can at least see the Employee ID field in the field list of the INVOICE table.

Drag the EMPLOYEE table from the Tables list of the RI Visual Designer and drop it into the Design pane.

Click on the Employee ID field of the INVOICE table. Drag from the Employee ID field of the INVOICE table and drop on the Employee Number field of the EMPLOYEE table. By dragging from a foreign key field and dropping on a primary key field, you instruct the RI Visual Designer to create an initial RI object using the associated indexes. Once you release the foreign key field over the primary key field, the Referential Integrity dialog box is displayed, as shown in Figure 5-7.

Set Name to Employee Sales, and Fail Table to c:\AdsBook\empfail.adt.

In the Rules section, set Update to CASCADE and Delete to RESTRICT.

Click OK to complete the RI object definition and to return to the RI Visual Designer, which now looks similar to that shown in Figure 5-8.

   
NOTE: The Rules you set up are displayed in the left column of the RI Visual Designer under Rules. If you need to delete a rule, right-click on the name of the rule and select Delete. To view or change rule properties, right-click on the name of the rule and select Properties to display the Referential Integrity dialog box again.  
 

Figure 5-7: The Referential Integrity dialog box after dropping a foreign key field onto a primary key field in the RI Visual Designer

Figure 5-8: The RI Visual Designer after adding a new RI Object