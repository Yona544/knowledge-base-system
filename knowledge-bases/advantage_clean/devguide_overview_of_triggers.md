---
title: Devguide Overview Of Triggers
slug: devguide_overview_of_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_overview_of_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 11af748c5050b335c564ee8fc16d5cf8d8878c86
---

# Devguide Overview Of Triggers

Overview of Triggers

 

     Overview of Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Overview of Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Unlike a stored procedure, which is executed only when a client application includes a call to it, triggers are always invoked in response to an associated data event. For example, you can create a trigger that executes when a record is being inserted into your customer table. It doesn't matter whether you are inserting the record from the customer table using the Table Browser in the Data Architect or from a client applicationthe trigger will execute.

This is an important point, so let us repeat it in a slightly different way. There is no way to circumvent the execution of an enabled trigger during a record-level operation on a table (at least from ADT tables which, when bound to a data dictionary, cannot be accessed as free tables). By comparison, a given stored procedure is only executed when a client application specifically invokes it. Consequently, the operations embodied in a trigger are guaranteed to take place in response to an event, while those in a stored procedure are not.

   
NOTE: Advantage 8 introduces the ability to disable a trigger. When disabled, a trigger does not get executed in response to its associated record-level event. Disabling triggers is discussed at the end of this chapter.  
 

You write triggers to perform validation or to perform additional tasks in response to a data operation. For example, a trigger can be used to generate a unique customer ID each time a new record is being inserted into the customer table. Likewise, a trigger can be used to write to a log table each time a change is made to a customer record. This type of operation is usually called an audit trail.

As with AEPs (Advantage Extended Procedures), you can write triggers using any development environment that can create Windows DLLs (dynamic link libraries), Linux so (shared object) libraries, in-process COM (component object model) objects, or .NET class libraries (.NET managed assemblies). Because each of these libraries can have one or more triggers, they are referred to as trigger libraries or trigger containers for convenience.

You can also write triggers using SQL scripts. A trigger written in SQL is referred to as a SQL trigger. SQL triggers, like SQL stored procedures, are stored in the data dictionary in which they are defined.

The fact that Advantage can execute triggers written in languages other than SQL is significant. Many database servers only support SQL-based triggers. This SQL is necessarily quite limited compared to most higher-level programming languages. As a result, when you write your triggers using DLLs, shared object libraries, COM objects, or .NET class libraries, your Advantage triggers can be significantly more powerful than those you can create for most other database servers.

If you implement your trigger as a DLL, COM object, shared object library, or .NET class library, your triggers are passed seven parameters. The first parameter is a unique number that identifies the client connection whose actions are initiating the trigger.

The second parameter is a handle to a connection. You use this connection for two purposes. First, you use this connection to access any tables, views, or stored procedures in the data dictionary with which your trigger is associated. Second, you use this connection to work with special temporary, in-memory tables that Advantage creates with information about the trigger event.

Because this connection is associated with the connection that initiated the trigger, if the initiating connection is currently in a transaction, any operations that you perform within your trigger are processed in that same transaction. Similarly, your trigger also has access to any temporary tables created by the connection from which it is executing.

   
NOTE: These first two parameters are the same as the first two parameters passed to an Advantage Extended Procedure (AEP) function.  
 

The third parameter of a trigger is the trigger object's name, as defined in the data dictionary. The fourth parameter is the name of the table in the data dictionary with which the trigger is associated.

The fifth parameter identifies what trigger event is executing, and the sixth parameter is the type of trigger. Finally, the seventh parameter is the internal record number of the record being affected by the trigger.

Parameters are not passed to SQL triggers. Nonetheless, SQL triggers are executed on the same connection as the client whose edit initiated the trigger. As a result, SQL triggers execute within the same transaction context as the client connection, and have access to any temporary tables available to the client.

When a trigger is executing, it has access to at least one temporary in-memory table. This is the error table, and it has the name \_ \_error (this name is preceded by two underscore characters). The \_ \_error table has two fields: ERRORNO and MESSAGE. If you insert a record into the \_ \_error table, the trigger will fail and Advantage will raise an exception on your client application. For instance, if a BEFORE update trigger is executing, inserting a record into \_ \_error will prevent the record from being inserted (and any AFTER triggers will not fire either).

When you create a trigger object you have the option to create additional temporary in-memory tables that can be accessed from the trigger. One option is to include value tables. Value tables are included by default, and you will nearly always keep this setting.

For update triggers, the value tables are named \_ \_new and \_ \_old (two consecutive underscore characters precede each of these names). The \_ \_old table contains the original values of the table's fields, and the \_ \_new table contains the updated record. Insert event triggers only include the \_ \_new table, and delete event triggers can only access the \_ \_old table. Both of these tables contain exactly one record.

When you choose to include value tables for access by your triggers, you can optionally include memo and BLOB (binary large objects) data in the \_ \_old and \_ \_new tables. If your triggers do not need to work with memo or BLOB data, you can increase the performance of your trigger by omitting these types of fields.

Note that the \_ \_old, \_ \_new, and \_ \_error tables that you use in triggers are in-memory tables. Operations performed on in-memory tables are very fast.

The code that appears in a trigger is often used to write to one or more tables in a database. When a trigger writes to a table, there exists the possibility that the write operation itself will fire another trigger, which could then possibly write to another table, firing yet another trigger, and so on, and so on. To prevent an infinitely recursive trigger execution (which would ultimately stop when you run out of stack space), Advantage will only permit trigger recursion to 64 levels.

Advantage supports triggers on four types of events. These are record insertions (INSERT), record updates (UPDATE), record deletions (DELETE), and replication conflicts (ON CONFLICT).

For the first three trigger types, Advantage provides three event types. These are BEFORE triggers, INSTEAD OF triggers, and AFTER triggers. ON CONFLICT events only support UPDATE and DELETE triggers and views support only INSTEAD OF trigger types. Each of these trigger types is discussed in the following sections.
