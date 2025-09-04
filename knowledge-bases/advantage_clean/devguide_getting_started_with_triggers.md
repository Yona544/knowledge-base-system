---
title: Devguide Getting Started With Triggers
slug: devguide_getting_started_with_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_getting_started_with_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6ccf93d56b3aec024e5ab74a1378e13981ac5f9e
---

# Devguide Getting Started With Triggers

Getting Started with Triggers

     Getting Started with Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Getting Started with Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As mentioned previously, you build your trigger either using a SQL script or using your development environment of choice. For all triggers other than SQL scripts, Advantage provides you with project templates for the most popular development environments, just as they do for AEPs. In most cases, you begin your trigger project by using the template, although you could also create your trigger project manually. If you decide to create your trigger project manually, it is a good idea to study the code created by the trigger template, so that you will implement your trigger project correctly for your particular development environment.

These templates include one function that provides you with a prototype for a trigger. This function can be used to create any type of trigger. For example, it could be used to create a BEFORE DELETE trigger or an INSTEAD OF UPDATE trigger.

Normally, you will take this one function and change its name. For those environments, such as Delphi, where you must explicitly export your functions, you also need to change the name of the function that appears in the exports clause.

You will also likely make one or more copies of this trigger, providing each with a different name (and corresponding entry in the exports clause, if applicable). Each of these copies can be used to implement a different trigger. In other words, you can implement many different triggers in a single project.

The next section discusses how to create triggers for your DemoDictionary data dictionary.
