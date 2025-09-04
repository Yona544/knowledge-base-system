---
title: Master Debugging Triggers
slug: master_debugging_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_debugging_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: 1eb477f6ecf7e3931ae336c43815e19fee857dcc
---

# Master Debugging Triggers

Debugging Triggers

Debugging Triggers

Advantage Concepts

| Debugging Triggers  Advantage Concepts |  |  |  |  |

For information on how to debug SQL script triggers refer to [Debugging a Database Object](arc_debugging_a_database_object.md). All other trigger containers can be debugged using two different methods (depending on which Advantage server type you are using).

Advantage Local Server

Open the trigger project in your development environment. Specify either a test application or the Advantage Data Architect (ARC) as the host application for debugging. Set breakpoints in your trigger function and run the debugger.

Advantage Database Server

Open the trigger project in your development environment. Specify the Advantage server executable (ads.exe) as the host application for debugging. Set the command line parameters for the host application to "-exe". If the Advantage Database Server is currently running on the computer you will be debugging from, stop it. Set breakpoints in your trigger function and run the debugger. This will start the Advantage Database Server as an executable (as opposed to a service). Start your application and perform an operation that will cause the trigger to fire. The debugger will stop on your first breakpoint.

 

Note for TDataSet Descendant users If execution does not stop on your breakpoint you may need to modify your linker options. Select Options from the Project menu. Select the Linker tab and verify that the Include TD32 Debug Info and the Include Remote Debugging Symbols check boxes are both checked. Rebuild your project, and try again. These options will greatly increase the size of your DLL or shared object, so be sure to turn them off when you are finished debugging (or in your release build).

 

Note You must disable DLL Caching before debugging DLL triggers using Advantage Database Server. DLL Caching will cause Advantage Database Server to load a copy of the trigger container rather than the original container. See [DLL Caching](master_dll_caching.md) for more information.
