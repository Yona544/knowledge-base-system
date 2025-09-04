---
title: Devguide Using Triggers
slug: devguide_using_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: d9dcf3c89377e7f58231e5e09756fc8288cddbda
---

# Devguide Using Triggers

Using Triggers

 

     Using Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Triggers, like stored procedures, can be registered with a data dictionary either using the Advantage Data Architect or programmatically by writing SQL or writing in your development language to the Advantage Client Engine API. Registering triggers programmatically is something you can do if you need to register a trigger with a data dictionary at runtime, but most developers only need to register their triggers at design time. As is the case with so many of the objects you work with in a data dictionary, the Advantage Data Architect is the preferred tool for registering triggers.

Unlike stored procedures, which are invoked by a client, triggers are associated with a specific event for a specific table. As a result, you do not find a TRIGGERS node under your data dictionary node in the Connection Repository of the Advantage Data Architect, like you do with stored procedures. Instead, you find the option to configure triggers on the context menu associated with a particular table under the TABLES node of your data dictionary connection.
