---
title: Devguide Before Triggers
slug: devguide_before_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_before_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 99e89caa3a4e8426a9320f56e52718e653aba71c
---

# Devguide Before Triggers

BEFORE Triggers

     BEFORE Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| BEFORE Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A BEFORE trigger is one that is executed before the event takes place. For example, a BEFORE trigger for a delete event will execute prior to a record's deletion. From within this trigger, your code can evaluate the record that is being deleted and take an appropriate action. The action may be to do nothing, in which case the record will be deleted.

Alternatively, you can write an error message to the \_ \_error table, in which case no further action is taken by Advantage, and the record will not be deleted. When you write to the \_ \_error table from within a trigger, no further triggers for that operation on that record will be fired. For example, if you write an error to the \_ \_error table from a BEFORE delete trigger, any AFTER triggers associated with deletions on that same record will be skipped for that data operation. (As is discussed in the next section, you cannot have a BEFORE trigger and an INSTEAD OF trigger on the same event type.)

   
NOTE: For SQL triggers, raising an exception has the same effect as writing to the error table. By comparison, you should always use the \_ \_error table to signal an error from trigger libraries.  
 

BEFORE triggers permit you to implement many of the same types of validation that can be performed using field-level and record-level constraints. In most cases, if you have the choice to perform validation using either a trigger or constraints, it's nearly always preferable to use constraints. The reason for this is that constraints are easier to configure and manage, and they execute faster.

On the other hand, there are many types of validation that can be performed by a trigger that cannot be accomplished using constraints. For example, if validation can only be accomplished by verifying that data being written to a table is consistent with data values stored in other tables, and those relationships cannot be represented using referential integrity, triggers provide you with a reliable solution for validating the data.

While a BEFORE trigger can validate an operation for a table, at least with respect to insert and update triggers, a BEFORE trigger cannot be used to change the values of the record being affected. When you need to change the data that is being written to a table from within a trigger, you can either use an INSTEAD OF trigger or an AFTER trigger.
