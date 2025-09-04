---
title: Devguide Defining Referential Integrity Constraints
slug: devguide_defining_referential_integrity_constraints
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_defining_referential_integrity_constraints.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 8ac7c296509686dd618aee43ab54d006462d33bf
---

# Devguide Defining Referential Integrity Constraints

Defining Referential Integrity Constraints

     Defining Referential Integrity Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Defining Referential Integrity Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Where field-level and record-level constraints define rules concerning the data stored in a single table, referential integrity refers to rules that define relationships between tables. Before continuing with the discussion of referential integrity, it is worthwhile to pause for a moment and consider how tables in an application are related.

In almost all but the simplest application, many tables that make up your database contain related data. For example, you may have one table that contains customer records and another table that contains records of the individual invoices for your customers. These tables are related, in that a given invoice is associated with a specific customer.

This relationship is embodied in the invoice table through the invoice table's customer ID field. Assuming that the invoice table's customer ID field is limited to those customer ID values appearing in the customer ID field of the customer table, and that the customer ID field in the customer table is unique for each customer, if you know the value of the invoice table's customer ID field, you know which customer the invoice is for.

In most applications there are many of these types of relationships. The invoice table records are also likely associated with an employee who made the sale, and that employee will have a record in an employee table. The order may also include a part number or service code, and those values will be associated with records in a parts table or a services table, and on and on.

When a primary key index order of one table uses the same key expression as a nonprimary index order of a second table, the fields of the second table's index order are referred to as a foreign key. Tables that include one or more foreign keys represent associations. The invoice table, for example, represents an association between an invoice and a customer. It also represents an association between an invoice and an employee responsible for the invoice, so long as the invoice table has at least two foreign keysone for the customer table and one for the employee table.

The relationship between the customer and invoice tables in this example is often called a master-detail relationship, a one-to-many relationship, or a parent-child relationship. These terms are interchangeable, but the term "parent-child relationship" is used by Advantage.

   
NOTE: The discussion here assumes that you are familiar with the issues related to relational database design. If you are going to be responsible for designing the new tables for an application, and are not familiar with relational database design issues, you should read about the topic or engage the services of a qualified consultant before you begin. The success of a database application is greatly influenced by the soundness  
of its design.  
 

Referential integrity (RI) refers to index-based rules that define how the related data in two tables is managed. RI is useful because the associations among data in the tables of an application are valuable in that, together, they represent important information. For example, if a customer record is deleted from the customer table, and that record was associated with one or more records in the sales table, the deletion of the customer record makes the previously associated sales records less informative. Specifically, you would have a record of a sale, but no information about who made the purchase.

With referential integrity definitions, you can explicitly define what happens when data in related tables is changed. For example, you can use referential integrity to prevent the deletion of a customer record if that customer is associated with one or more sales in the sales table. To put it another way, referential integrity definitions can prevent loss of data.

Referential Constraints Example

In order to define a referential integrity relationship, you must specify which two tables participate in the relationship. In addition, you must specify which indexes embody the relationship. If the primary or foreign key indexes are single-field indexes, it is not necessary to create these indexes in advance--they will be created automatically for you when you define the RI object. If either of the indexes are multifield indexes, you need to create them in advance.

In this example the primary indexes and foreign key indexes are single-field indexes.

Use the following steps to define a referential integrity relationship between the customer (parent) and the invoice (child) tables:

1.        Right-click RI OBJECTS and select Create. The Referential Integrity dialog box, shown in Figure 5-5 is displayed.

Figure 5-5: The Referential Integrity dialog box

2.        At Name, enter Customer Invoices. At RI Fail Table, enter c:\AdsBook\rifail.adt. The RI fail table is described later in this section.

| 3. | In the Parent Table section, set Name to CUSTOMER. Set Primary Key to CUSTOMER ID. |

| 4. | In the Child Table section, set Name to INVOICE and Foreign Index to Customer ID. |

| 5. | In the Rules section, set Update to Cascade and set Delete to Cascade. (The update and delete rules are described in the next section.) |

| 6. | Click OK to complete the RI definition. |

When you complete this definition, the RI rules will be applied to the table. If the child table contains data when these rules are applied, depending on the specific rules that you applied, there is a possibility that one or more records in the child table violate the RI rules.

If one or more records of the child table violate your RI rules, what happens depends on whether or not you defined an RI fail table. If you did not specify an RI fail table, and records exist in the child table that don't have a corresponding primary key, a dialog box reports that the RI object cannot be created and the Advantage Database Architect will ask you if you want to see the first offending record.

If you defined an RI fail table, and one or more records of the child table violate the RI rule you defined, those records are deleted from the child table and placed into the RI fail table.

   
TIP: Each time you create an RI object, check to see if any records have been placed in the RI fail table. If records were added to the RI fail table, you should inspect them to see if they can be corrected and returned to the child table using the Export to Existing Table export option. In addition, since an RI fail table will be overwritten with each RI rule creation, it is a good idea to specify a different RI fail table for each RI rule you create.  
 

Update and Delete Rules

You use the update and delete rules of an RI definition to control what kinds of changes are permitted to the parent table when associated child records exist, as well as what to do if changes would otherwise disassociate the relationship.

The update rule defines what happens when you want to post a change to a parent table record that has one or more associated child records. Selecting an update rule of RESTRICT prevents a parent table's primary key fields from being changed for any record for which there are related child records. Using our current tables for example, if you use a restrict rule and there are invoices for a particular customer in the invoice table, you cannot change that customer's Customer ID field.

If you set the Update field of the Rules section to CASCADE, changes made to a parent table's primary key fields are propagated to the corresponding fields of existing child records. For example, using a cascade rule, you can change the Customer ID field for customer records, even when there are associated child records. The changed Customer ID field will be applied both to the customer table and the associated invoice table records.

Both the RESTRICT and the CASCADE update rules ensure that the parent/child relationship in your tables is maintained. The remaining two options, SET NULL and SET DEFAULT, permit you to terminate the relationship. These rules control what happens to the fields of the child table foreign key when the relationship ends.

If you set the Update rule to SET NULL, changing a parent key will cause the associated child table record's foreign key fields to be set to a null value. For example, if you were to change the Customer ID field in the customer table, any related invoice table records would have their Customer ID fields set to null values. This has the effect of orphaning the child table records.

If you set the Update rule to SET DEFAULT, changing a parent key causes the associated child table record's foreign key to be set to the default value defined using the Fields page of the Table Designer. This default value must be a legitimate primary key value in the parent table, so although an Update rule of SET DEFAULT will sever the relationship, it will create a new relationship to some other parent.

Delete rules are similar to update rules, but apply when you attempt to delete a parent table record for which there are associated child records. Set the Delete field under Rules to RESTRICT to prevent a parent record from being deleted if at least one associated child record exists. When this rule is in place, you must first delete any associated child table records before you can successfully delete the parent table record.

Set the Delete rule to CASCADE if you want Advantage to automatically delete associated child records when a parent record is deleted. Considering our example tables, if a CASCADE delete rule is enforced, deleting a customer would cause the automatic deletion of the invoices for that customer.

Set the Delete rule to SET NULL if you want the foreign key of the associated child table records to be set to a null value upon deletion of the parent record. Finally, set the Delete rule to SET DEFAULT to set the foreign key of the associated child table records to the default value defined using the Fields page of the Table Designer.

   
NOTE: When you use update and delete rules other than RESTRICT, changes or deletions made to the parent table can potentially introduce unique key violations in the child table if the child table's foreign key field is part of another unique index.
