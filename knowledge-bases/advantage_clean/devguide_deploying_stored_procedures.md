---
title: Devguide Deploying Stored Procedures
slug: devguide_deploying_stored_procedures
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_deploying_stored_procedures.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6a4f8c0c5bf8d9cf03d47b57513bf26e8d639d8c
---

# Devguide Deploying Stored Procedures

Deploying Stored Procedures

     Deploying Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Deploying Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

SQL stored procedures are saved entirely inside your data dictionary definition. When you deploy your data dictionary, you are also deploying any SQL stored procedures contained within it.

What steps you need to take when deploying an AEP library depend on the type of AEP it is. The easiest AEP containers to deploy are those that are created as DLLs or shared object libraries, especially if you store them in the same directory as the data dictionary. Simply copy the DLL or shared object library to that directory. If you store your DLL or shared object library in a directory different from where your data dictionary files are, ensure that your stored procedure object definition includes the path to that library.

AEP containers deployed as COM objects or .NET class libraries are somewhat more complicated to deploy. Although your COM object or .NET assembly can be placed in any directory, it must be registered with the Windows Registry. As you learned earlier in this chapter, you register a .NET assembly with regasm.exe, which ships with the .NET framework, and is therefore available on any machine on which the .NET framework has been deployed. The .NET framework must be installed on any machine to which you deploy an AEP container created as a .NET-managed assembly. (COM objects are registered using RegSvr32.exe, which is on the DOS search path by default on Windows machines.)

   
NOTE: A number of development environments include an installation builder that can take responsibility for registering your COM objects and .NET class libraries.  
 

Note that if you are deploying updated AEP containers that are either COM or .NET class libraries, it is a good idea to first unregister your older versions before replacing and registering the new versions. Failure to unregister older versions before replacing them may leave unwanted entries in that machine's Windows Registry.

The problem of AEP installation is magnified if you are using ALS instead of ADS. When you use ALS, the COM object or .NET-managed assembly must be installed on all client machines. Furthermore, the .NET framework must be present on all client machines as well.

ALS-based clients that employ DLLs or Linux shared object libraries normally do not require any client-specific installations. Only when these AEPs rely on additional external modules (DLLs or so libraries) must you perform client-specific installations.

 

In the next chapter, you will learn about Advantage triggers.
