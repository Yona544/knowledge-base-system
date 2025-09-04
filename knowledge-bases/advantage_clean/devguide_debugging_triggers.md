---
title: Devguide Debugging Triggers
slug: devguide_debugging_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_debugging_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 171f94ca0db499028addbf76f47fafe50281fc57
---

# Devguide Debugging Triggers

Debugging Triggers

     Debugging Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Debugging Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You cannot debug SQL script triggers. For all other trigger types, the process is nearly identical to that which you use when you debug an AEP. Specifically, while in your development environment, set up a host or calling application. Then, with your trigger project open and breakpoints set, start the debugger, which will automatically launch the host or calling application. See your development environment's documentation for details on how to do this.

Also, recall that most developers debug trigger containers using ALS, but with ADS 7.0 and later, you can use the -exe command-line option with the ads.exe host or calling application to debug triggers using ADS.

   
NOTE: As is the case with Delphi AEPs, some development environments may require that you change your project options before you can successfully debug your project. For example, with triggers written in Delphi, you often have to enable debugger-related linker options. Remember to disable these options before you distribute your trigger libraries, as these options cause your projects to be very large.
