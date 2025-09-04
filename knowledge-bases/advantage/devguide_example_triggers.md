Example Triggers




Advantage Database Server 12  

 

     Example Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Example Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Example Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Example\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Example Triggers / Dear Support Staff, |  |
| Example Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The following sections demonstrate how to create triggers for the DemoDictionary that we have been building throughout this book. Several of these triggers can be implemented using SQL scripts. In most cases, if your trigger is simple enough to implement in SQL, you probably want to use a SQL script.

One of the triggers you need is generic, and cannot be implemented in SQL (at least in its generic form). For triggers like these, you must resort to another development environment. Creating this trigger is demonstrated in Delphi, C#, and VB for .NET. As in the preceding chapter, the steps that demonstrate how to create these trigger projects assume that you are already familiar with these development environments.

Unlike in the preceding chapter, creating triggers using Visual Basic 6 is not discussed in detail. As described in the preceding chapter, you are discouraged from creating AEPs using Visual Basic 6, except in very limited situations, due to potential performance bottlenecks that they can introduce. Recall that because Visual Basic 6created COM objects use a single threaded apartment (STA), it is not possible for two threads on the Advantage Database Server to execute the same Visual Basic 6created COM object concurrently.

With triggers, the issue is the same, but the problem is far more significant. Since triggers tend to execute far more often than AEPs, the performance bottleneck that these COM triggers would introduce makes it almost inconceivable to think of using them. As a result, Advantage does not provide a template for creating triggers using Visual Basic 6.

With respect to the examples provided in this section, we wanted to keep the trigger examples relatively simple so you can concentrate more on what a trigger can do than on how to do it. Therefore, we are going to demonstrate two triggers to implement data archiving and one trigger to assign a unique, artificial key.

The triggers that demonstrate data archiving are both SQL triggers, and are assigned to the CUSTOMER and CUST\_BAK tables (CUST\_BAK will be added to your data dictionary in the following steps). When a customer record is being deleted, the first trigger will first check to see if the customer has any outstanding invoices. If that customer has one or more invoice records in which the Date Payment Received field is empty, an error will be returned, and the record will remain in the CUSTOMER table. But if there are no outstanding invoices for this customer, the customer's record will be copied to the customer archive table, named CUST\_BAK.ADT, and will be deleted from the CUSTOMER table.

The second trigger permits an archived customer record to be restored to the CUSTOMER table. This trigger, which will be attached to the CUST\_BAK table, will trigger when a record is deleted from the CUST\_BAK table. From within this trigger, the SQL script will verify that the Customer ID does not already exist in the CUSTOMER table. If the Customer ID does not already exist in CUSTOMER, the record is copied to the CUSTOMER table, after which it is removed from the CUST\_BAK table.

The effect of these two triggers (so long as they do not get disabled) is to make it impossible to ever lose a customer's record. It merely gets moved back and forth between CUSTOMER and CUST\_BAK.

The third trigger is designed to generate a unique key. In this case, the unique key will be a GUID, or globally unique identifier.

This trigger is generic, in that it can be assigned to any table whose first field is a character field of at least 38 in length. While the Advantage expression engine function NEWIDSTRING (added in 8.1) can create a GUID in a SQL script, the code would have to be customized for each table to which the trigger was assigned (since you cannot determine which table a SQL script is associated with at runtime).

Trigger libraries, however, are passed the name of the table to which they are assigned as a trigger function parameter. This generic trigger function is written in Delphi, C#, and VB for .NET.

Before you can use the SQL triggers, there is an additional table that you need to add to your data dictionary. This table is CUST\_BAK, and is currently a free table that is located in the same directory as your data dictionary. The following steps show you how to add this table to your data dictionary:

With the DemoDictionary connection open and connected in the Connection Repository, right-click the TABLES node and select Add Existing Table(s).

From the Open dialog box, select CUST\_BAK.ADT and click Open. Your expanded TABLES node in the tree view in the Advantage Data Architect should now look like that shown in Figure 8-1.

Figure 8-1: The CUST\_BAK table has been added to the data dictionary