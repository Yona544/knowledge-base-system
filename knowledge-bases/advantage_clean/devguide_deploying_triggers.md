---
title: Devguide Deploying Triggers
slug: devguide_deploying_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_deploying_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c443c942a91a51d2a3fef1c37cd332db9e501fcb
---

# Devguide Deploying Triggers

Deploying Triggers

     Deploying Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Deploying Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Your triggers that are implemented as SQL scripts are stored in your data dictionary. There is nothing special that you need to do to deploy your SQL script triggers, other than deploy your updated data dictionary.

If your triggers are entirely SQL based, and you are adding triggers to an existing dictionary, it is not necessary to redeploy that data dictionary. Instead, you can write a simple SQL script that adds one or more triggers to your existing data dictionary. If you decide to take this approach, you do not even have to write the SQL manually. You can right-click on a table in the Connection Repository in the Advantage Data Architect and select Generate SQL Script. In addition to SQL that defines the table and its indexes, the generated code will include the SQL that defines each of the SQL triggers associated with that table.

For all other types of triggers, the issues of deployment are the same for triggers as they are for AEPs. Specifically, you will need to deploy your trigger libraries to the machines on which they will be executed. Furthermore, for COM and .NET class libraries, you must register the library in order for ADS or ALS to load it. You might also want to consider signing and using strong names for .NET class libraries. If your development environment has an installer builder, you should be able to use it to register your .NET class libraries and COM objects.

When deploying .NET triggers that run under ALS, each client machine must have the .NET framework installed, and the triggers must also be registered on each machine.

Note that if you are deploying updated COM or .NET class library triggers, it is highly recommended that you first unregister your older versions before replacing and registering the new versions. Failure to unregister older versions before replacing them may leave unwanted entries in that machine's Windows Registry.
