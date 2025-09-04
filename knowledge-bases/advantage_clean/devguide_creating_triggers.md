---
title: Devguide Creating Triggers
slug: devguide_creating_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 8c5c154f1b884f6b9cd33d8f597478d31d65bd24
---

# Devguide Creating Triggers

Creating Triggers

 

     Creating Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you are creating SQL script triggers, you can write and configure your triggers entirely in the Advantage Data Architect. In fact, if you needed to, you can create your triggers at runtime using SQL. However, creating triggers, like stored procedures, is often part of your overall database design process, which means that you are most likely to create and register your triggers at design time.

For any trigger other than SQL scripts, creating and registering the trigger requires two distinct steps. In the first step, you create the trigger library using your development environment of choice. You can then register the trigger for your data dictionary using the Advantage Data Architect, although this registration can also be performed programmatically at runtime, if necessary. If you are creating your triggers using SQL scripts, you define your SQL and configure the trigger all within the provided Triggers dialog box in the Advantage Data Architect.
