Understanding Constraints




Advantage Database Server 12  

 

     Understanding Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Understanding Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Understanding Constraints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Understanding\_Constraints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Understanding Constraints / Dear Support Staff, |  |
| Understanding Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Constraints are declarations that you attach to a database table to ensure that your data is consistent and accurate. For example, imagine that you have a database that is used to manage the inventory of a warehouse. Using a constraint, you can prevent negative quantities from being entered into a field used to store the number of items on hand. From an inventory perspective, a negative quantity doesn't make sense. You either have some quantity of a particular object (a positive integer) or you have none. (This example assumes that back orders are handled separately from the field used to maintain the number of items on hand.)

This type of constraint applies to a single field in a table. As a result, a constraint like this one is called a field-level constraint.

Another type of constraint supported by Advantage is one that can consider the data in one or more fields of a record when determining whether data is valid or not. For example, in an invoice table you can make sure that a value has been entered into the credit card number field when payment type is credit, and that the credit card field is blank when payment type is cash. This type of constraint is called a record-level constraint.

Referential integrity constraints apply to two related tables. For example, imagine that you have a table that holds invoices for sales made to customers, and another table where each customer's information, such as their ID, name, address, and credit limit, is stored. Using a referential integrity constraint, you can ensure a new invoice added to the invoice table includes the customer ID for one of your valid customers. If a user attempts to post a new invoice record, but the customer ID that they entered is not one found in the customer table, the invoice record will be rejected.

In all three of these cases, the purpose of the constraint is to improve the accuracy and consistency of the data in your database. But constraints are not the only source of data integrity in database applications. In order to put this into perspective, it is worthwhile spending a few minutes considering the alternatives to constraints in Advantage applications.