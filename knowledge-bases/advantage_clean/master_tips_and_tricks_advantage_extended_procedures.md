---
title: Master Tips And Tricks Advantage Extended Procedures
slug: master_tips_and_tricks_advantage_extended_procedures
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_tips_and_tricks_advantage_extended_procedures.htm
source: Advantage CHM
tags:
  - master
checksum: 90202fe74ff3e1e921afc2e1f9963fc4ab7f3e61
---

# Master Tips And Tricks Advantage Extended Procedures

Tips and Tricks (Advantage Extended Procedures)

Tips and Tricks (Advantage Extended Procedures)

Advantage Concepts

| Tips and Tricks (Advantage Extended Procedures)  Advantage Concepts |  |  |  |  |

AEP Permissions

Data operations performed inside interface version 2 or greater Advantage Extended Procedures will not check user privileges. This allows you to hide tables or other database objects from the user(s), yet still provide controlled access to them through AEPs.

Utilize the Features of the Advantage Data Architect (ARC)

The database management features of ARC make it very easy to register and maintain Advantage Extended Procedures. It is possible to add/remove procedures through SQL statements, but if youd prefer a visual approach, open the database in ARC and maintain your procedures this way.

TDataSet Descendant Users: Utilize the AEP template provided

Select New from the File menu. Select the Advantage tab. You will see an AEP template project. Use this template to accelerate your AEP development.

If you choose not to use the template, be sure to set the global VCL variable "IsMultiThread" to TRUE somewhere in your DLL startup code. This variable is used by the Delphi VCL memory manager to decide if it needs to be thread-safe. Because the Advantage server, which loads your DLL, is multi-threaded, this variable must be set to TRUE in order to avoid random exceptions in your AEPs.

Visual Basic .NET and Visual C# .NET Users: Utilize the AEP template provided

Select New->Project from the File menu. Select AdvantageAEP from the list of project templates.

Updating an Advantage Extended Procedure

By default, AEP containers can be updated without stopping the Advantage Database Server or disconnecting dictionary users. This is possible through the [DLL Caching](master_dll_caching.md) functionality that leaves the original AEP container available for replacement. If Advantage detects a change in the AEP container, it will automatically transition users of the old container to a copy of the new one. However, if [DLL Caching](master_dll_caching.md) is disabled and there are connected users that are using, or who have used, the AEP, they must disconnect before the AEP can be replaced. Be sure to update the Advantage Data Dictionary if exported procedures have been added or removed (see [Register Your Procedure with a Data Dictionary](master_creating_an_advantage_extended_procedure.md#register_your_procedure_with_a_data_dictionary)).

 

Note to Linux users In Linux you can replace the AEP even while it is in use. Keep in mind, clients will not use the new AEP until the Advantage Database Server has unloaded the current version and re-loaded the AEP from disk. If [DLL Caching](master_dll_caching.md) is enabled (the default setting), this will happen once the Advantage Database Server detects a change in the AEP container. If [DLL Caching](master_dll_caching.md) is disabled, this will happen once all users that have called functions in the AEP have disconnected.

 

Note to .NET users The .NET environment keeps assemblies loaded in memory until the application that was using them terminates. Because the Advantage Database Server is the application using the AEPs, it must be stopped before .NET AEPs can be updated.

DOs and DONTs of Advantage Extended Procedures

DO

- Open all input and output tables in a shared mode so that data can be shared with other entities.

- Protect global variables with critical sections.

- Export all procedures. In Delphi this means add them to the exports clause; in C this means declare them as exported entry points.

- Use the connection ID passed to Startup, Shutdown, and all procedures to uniquely identify a connection.

- Use the user name and password parameters when logging into a database from within a procedure.

- TDataSet Descendant users: If using [AEP interface version](master_aep_interface_version_comparison.md) 1 set the TAdsConnection.StoredProcedureConnection property to True on all connections that live inside an AEP data module.

- Visual Basic users: If using [AEP interface version](master_aep_interface_version_comparison.md) 1, pass the "StoredProcedureConnection=TRUE" option in your ADO connection string for any connections that live inside your AEP.

- C users: If using [AEP interface version](master_aep_interface_version_comparison.md) 1, include the ADS\_STORED\_PROC\_CON option in the ulOptions parameter when making Advantage connections from within an AEP.

- .NET users: It is important to clean up all AdsCommand (IDbCommand) objects by calling the Dispose method. The Dispose method ensures that the underlying statement handles are cleaned up. If Dispose is not called, then it is possible for the .NET garbage collector to dispose the object. Because these assemblies are executed within the Advantage Database Server process space, this means that the call will come into the server code on an unexpected thread and can result in undefined behavior.

- Use UNC (\\SERVERNAME\SHARE) when making connections or opening tables from inside an AEP. Also use UNC for any TDataSet aliases that are used from inside an AEP. Failure to do so may result in 7077 and 7008 errors.

- Use the \_\_error table to return an error code and/or error string to the client application.

- When writing a procedure using the .NET Data Provider or the OLE DB provider (for ADO), remember that some statement level settings are specified via the connection string. The settings that you may need to specify explicitly are LockMode and CharType when using DBF (non-ADT) table types. These settings are not inherited from the connection and they are not stored in the data dictionary.

DONT

- Change the .AEP file extension of the Advantage Extended Procedure.

- If writing directly to the Advantage Client Engine API do not call AdsOpenTable or AdsCreateTable and pass a connection handle of zero. Always pass a connection handle retrieved from a previous call to AdsConnect60.

- If writing an AEP using the Advantage TDataSet Descendant, always use a TAdsConnection component. Do not open tables without first pointing them to a TAdsConnection component.

- Use thread local storage (threadvars). A single client can have multiple different Advantage Database Server threads performing actions on its behalf. You are never guaranteed the thread that performed work for your last request will also be performing the work for your next request.

- Raise messages boxes or wait for user input from within an AEP. This will hang the Advantage worker thread, and you will have to restart the Advantage server to reclaim the thread. AEPs are a server-side process, and should never require user interaction.

- Visual Basic 6 users: Call DoEvents or any other function/procedure that will yield control of the processor inside of an AEP. Ways in which your code can yield control of the processor include:

- Calling DoEvents

- Invoking the properties or methods of an object on another thread, or in another process

- Raising an event thats handled by an object on another thread, or in another process

- Invoking a cross-thread or cross-process method from within a method

- Showing a form

- Use drive letters when making connections or opening tables from inside an AEP. Use UNC (\\SERVERNAME\SHARE) instead. Failure to do so may result in 7077 and 7008 errors.

COM and .NET AEP Notes

- Objects containing the AEPs must be registered on the server running Advantage Database Server. See Microsoft documentation on regsvr32.exe (for COM DLLs), regasm.exe (for .NET assemblies), and other registration methods.

- If using the Advantage Local Server, the object containing the AEPs must be registered on each client machine.

- Advantage uses ProgID values to identify COM and .NET classes. A ProgID is a programmer-friendly string value used to identify a class, and is easier to work with than a ClassID (GUID).

- In Visual Basic 6 (as opposed to VB .NET) all ActiveX DLLs run in a single-threaded apartment. This means all global variables are safe because only one Advantage thread can be calling a stored procedure at any instance. While this makes writing an AEP simple (no need to protect global variables from other threads) it can cause major performance problems in a multi-user environment. AEPs written in VB6 will be executed in a synchronous fashion. This means only one AEP will be allowed to run at a time. It is recommended you use VB.NET or Visual C# .NET to write all Advantage AEPs.

- If using Advantage Local Server the client application and the AEP must use the same "ShowDeleted" setting. If both the client and AEP are written in the same language this is usually not a problem. If the settings are mismatched you may receive a 6619 (comm layer was busy) error.

- The Advantage Database Server makes a call to the COM library approximately every 10 seconds asking it to free any unused COM objects (AEP libraries). We have seen various behaviors depending on the version of Windows in use. You may have to unload ADS in order to update AEP libraries, depending on the behavior of the COM library on your server.

- The .NET environment keeps assemblies loaded in memory until the application that was using them terminates. Because the Advantage Database Server is the application using the AEPs, it must be stopped before .NET AEPs can be updated.

 

Transaction Tips

Version 2 AEPs (which you will most likely be writing unless you are maintaining compatibility with an older version of Advantage) cannot start new transactions, or rollback or commit transactions using the connection handle that they are passed. You can, however, declare a new connection inside of your AEP and use transactions on that connection if necessary.

Keep in mind that all operations performed inside your AEP using the connection passed in are done under the context of the existing transaction (if one exists). This means if the client rolls back the transaction all operations performed by the AEP will also be rolled back.

Other AEP Tips

While a data dictionary is required to register an AEP, the tables that the AEP works on do NOT have to be bound to the data dictionary. An AEP can open and update tables that are not part of the data dictionary that the AEP belongs to.
