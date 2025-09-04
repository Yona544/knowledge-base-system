---
title: Devguide Triggers And Performance
slug: devguide_triggers_and_performance
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_triggers_and_performance.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 96a3451cab349337a123b215ac43b14871917cbf
---

# Devguide Triggers And Performance

Triggers and Performance

     Triggers and Performance

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Triggers and Performance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Although triggers provide you with an important and creative way to ensure the integrity of your data, there are performance issues that you should consider. Specifically, triggers are executed once per row of data. For example, imagine that you have an INSTEAD OF DELETE trigger. If you execute a DELETE SQL query against the table that uses this trigger, and that query deletes 1,000 records, the trigger will execute 1,000 times. As a result, what might have been a fast query if no trigger was present may now be a time-consuming one.

The following are some guidelines for getting the most out of triggers:

•        If a constraint can do the same task that you can perform from a trigger, use a constraint.

| • | If a field, such as ModTime or RowVersion, can perform the same task that you want from a trigger, use the field. |

| • | When writing a trigger, ensure that the code in your trigger is as efficient as possible. |

| • | Avoid inherently slow operations from inside a trigger. For example, do not read from a file on the local file system within trigger code (unless the value of reading from a file is greater than the performance penalty it introduces). |

| • | If possible, only use the connection that is passed to your trigger to work with data. Opening (and closing) a new connection is a relatively time-consuming operation. |
