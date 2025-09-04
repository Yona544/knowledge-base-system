Alternatives to Constraints




Advantage Database Server 12  

     Alternatives to Constraints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Alternatives to Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Alternatives to Constraints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Alternatives\_to\_Constraints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Alternatives to Constraints / Dear Support Staff, |  |
| Alternatives to Constraints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

In addition to constraints, the consistency and accuracy of your data derives from a number of other sources. These include the structures of your data files, unique indexes, client-side code, and triggers. Each of these is discussed in this section.

Table Structures

Even without constraints, there are inherent limits to the data that can be added to a table. These are derived from the table's structure. For example, you cannot post a text string to an integer field. Similarly, you cannot add a string of 100 characters to a 20-character field. Attempting to post data like this will cause an error, and the data will be rejected.

These limits, however, are very general. A 12-character field that is used to hold a product code doesn't discriminate between text strings that are 12 characters or less. Unless some other mechanism is used, such as referential integrity, an invalid product code cannot be detected based solely on the field's type.

Unique Indexes

Another source of data integrity is the use of unique indexes on ADT tables. For ADT tables, at least, a unique index prevents two records with the same unique key from being posted to the table. (DBF unique indexes do not enforce record uniqueness.) For example, if you have a unique index on the customer ID field in the customer table, an attempt to post a second customer with the same ID will fail. This type of integrity, sometimes referred to as entity integrity, guarantees that no two customers can share the same customer ID.

Client-Side Validation

Another significant source of data validation is code that you program into your client application. This type of validation, referred to as client-side validation, involves the programmatic inspection of data prior to posting it to the database. The data that is evaluated may be information entered into a graphical user interface (GUI) by an end user, or it may be data that is read from a data-collection device or a file.

Client-side validation is one of the most flexible of all of the validation mechanisms. In short, your code can perform any test and apply any criteria available in your programming language to verify that the data is acceptable before continuing with a post operation.

Although it is very flexible, client-side validation has two serious drawbacks. These are related to development and consistency.

Let's consider the development side of things first. Client-side code must be written and debugged. In some cases this is a minor matter, and in other cases it represents a significant investment of resources.

A whole new set of problems arises if you later need to change how the validation is performed. Not only do you have to modify and test your client applications, but you must also deploy your updated applications to every client machine. If only a few users use your application, the deployment may not be a big problem. However, if many people in many different locations use your application, the redeployment itself may be very expensive.

The second drawback to client-side validation is related to consistency. In short, the rules applied through client-side validation are applied consistently only to the extent that you ensure that they are. For example, imagine that you have several different client applications that work with a particular database. It is your responsibility to ensure that all client applications apply the validation rules the same way. If you make a change in the rules of validation in one client application, you need to do so in all others that work with the same database; otherwise, the data posted by one application may be inconsistent with that posted by another application.

Triggers

Like client-side validation, triggers are modules that you write. Unlike client-side validation, however, you install triggers on your server, and configure the data dictionary to call them in response to a data action. For example, a trigger can be executed prior to a record being updated in your database.

From within a trigger, your code has access to all of the data associated with the data event. For example, if the trigger is being executed because a record is being updated in your database, your trigger code has access to both the original record and the updates that the client is attempting to post.

You can use the information passed to your trigger to perform almost any action you can imagine. In most cases, though, the purpose of the trigger is to validate the data. If the data is determined to be good, the record is accepted. On the other hand, if your code finds that the record is invalid, an error can be returned and the record can be rejected.

Triggers have many advantages over client-side code. While providing the same level of flexibility in how you validate the data, triggers reside on the server. There are several advantages to this. First, triggers can be modified without requiring any changes to individual client applications. There is no need to redeploy your client applications in response to updates to triggers. (Though an updated data dictionary, and the trigger code if it is a compiled trigger, do need to be redeployed.)

Second, since triggers are executed by Advantage, and not at the discretion of the client applications, triggers are always applied consistently.

Third, triggers are also run if someone updates the database via the Advantage Data Architect or some other application that the developer has no control over.

Triggers were added to ADS in version 7.0, and represent one of the most valuable features in the product. Triggers are discussed in detail in Chapter 8.