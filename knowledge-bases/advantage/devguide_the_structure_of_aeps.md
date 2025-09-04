The Structure of AEPs




Advantage Database Server 12  

     The Structure of AEPs

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| The Structure of AEPs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      The Structure of AEPs Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_The\_Structure\_of\_AEPs Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > The Structure of AEPs / Dear Support Staff, |  |
| The Structure of AEPs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

AEPs represent one of Advantage's strengths over other database servers. Specifically, most database servers that support stored procedures limit how you can create them. While most database servers support stored procedures written in SQL, if there are additional options, they are usually limited. For example, for those database servers that permit stored procedures to be written in languages other than SQL, they often limit you to either a proprietary language, such as Interbase's GDL, or a general framework, such as Java or .NET.

By comparison, Advantage provides you with unparalleled flexibility when it comes to creating stored procedures. As mentioned earlier in this chapter, stored procedures can be implemented using SQL scripts, or as AEPs. Furthermore, AEPs can be written as Windows DLLs, Linux shared object libraries, .NET class libraries, or in-process COM objects. But the critical issue is that it does not matter which language you use to create these AEPs.

Because you can use your language of choice to create your stored procedures, AEPs can be far more sophisticated than those used by most other database servers. Instead of being restricted to conditional SQL, your AEPs can use the full breadth of capabilities of the development tool you choose. You can even perform tasks that have little or nothing to do with your database, such as sending an automated email message, if your development environment supports that.

For example, a Delphi developer can use practically any VCL (visual component library) class or RTL (runtime library) routine. Similarly, developers using a .NET language, such as C# for .NET, VB for .NET, or Delphi for .NET, can use any of the classes in the FCL (framework class library), as well as any invocable managed or unmanaged code.

Being able to use your development language of choice provides you with additional benefits. First, you do not have to learn another language before you can write stored procedures. Second, you get to use the tools with which you are already comfortable.

Regardless of the language you use to create your AEP libraries, all have similar characteristics. Each library must export at least four functions: Startup, Shutdown, GetInterfaceVersion, and one or more stored procedure functions. The names of the stored procedure functions are arbitrary.

   
NOTE: ADS 7.0 introduced version 2 AEPs, which greatly improved the performance of stored procedures. AEPs prior to ADS 7.0 are now called version 1 AEPs, and both their functions and the function parameters are significantly different from version 2 AEPs. Since version 1 AEPs have been deprecated, they are not discussed further in this book.  
 

In addition to these functions, all AEPs have an object that is used to manage one or more client connections. This object is created when the AEP is first loaded by Advantage, and destroyed when the AEP container is released. The default name of this object depends on which AEP template you use to create your AEP container. (And you are free to rename this object, if you like.) For example, with .NET languages, the default object is a HashTable named colClientInfo. For the convenience of the following discussion, we will refer to this object generically as the connection manager.

The following sections describe the four types of functions exported by AEP libraries in greater detail.

The Startup Function

The startup function is called the first time a given client application calls one of the stored procedure functions in a particular AEP library from a given connection. If a client application has two connections to Advantage, and calls a routine from an AEP from each connection, the startup function will be called twiceonce for each connection. The purpose of the startup function is to initialize an object that is used to maintain client state information about the connection, and to save this object to the connection manager.

The startup function is passed two parameters. The first parameter is a unique integer that is generated by the server prior to the invocation of the startup function. This value uniquely identifies the client's connection that is invoking the AEP. This same value is passed as the first parameter in the shutdown function and as the first parameter in the stored procedure functions for all subsequent calls from the same client over the same connection. Consequently, this value is used to identify the state maintenance object that is managed by the connection manager.

The second parameter is a handle to an active Advantage connection. This Advantage connection has a one-to-one mapping to the connection from which the client is invoking the stored procedure. As a result, if the client's connection has an active transaction, any data manipulation performed with the connection whose handle is passed in the second parameter will be performed in that same transaction.

In most AEP libraries, the startup function will create an instance of a state maintenance object, initialize a connection using the connection handle passed in the second parameter, and then save the state maintenance object so that it can be accessed from within the stored procedure functions and the shutdown function.

The startup function returns a 32-bit integer. Advantage currently does not use this value, but it should be set to the value 0 (zero) in order to maintain compatibility with potential changes in later releases of Advantage.

The Shutdown Function

The shutdown function is called when a client that had invoked at least one of the stored procedure functions in the AEP is closing its connection. The shutdown function is used to perform any cleanup operations on connection-specific objects that were created during the client's use of the AEP.

Like the startup function, the shutdown function is passed two parameters. The first parameter is the unique connection ID for this client connection. The second parameter is a handle of an active connection. The shutdown function uses the connection ID to remove the state maintenance object for this connection from the connection manager, and to destroy it.

The shutdown function returns a 32-bit integer value. As with the startup function, this value should be 0 (zero).

The GetInterfaceVersion Function

This simple function returns a 32-bit integer and is used to inform Advantage of the AEP version of the library. Version 2 AEPs, the current AEP version, return a value of 2. If this function is absent from the AEP, Advantage assumes that the AEP version is 1. The GetInterfaceVersion function takes no parameters.

Stored Procedure Functions

Each AEP library can have one or more stored procedure functions. These functions contain the code that performs the operations that you want to execute on the server when the stored procedure is called by the client application.

When an AEP library contains two or more stored procedure functions, each must have a unique name. Which stored procedure function gets invoked by Advantage depends on which stored procedure object is referenced by the client. Each stored procedure object in a data dictionary is specifically associated with one (and only one) stored procedure function in an AEP library.

Stored procedure functions are passed three parameters. The first and second parameters contain the connection ID and the associated connection handle, respectively. The connection ID is typically used to retrieve the state maintenance object for the connection that is calling this procedure. In most cases, this state maintenance object holds an active connection, so usually you do not need to use the second parameter of your stored procedure object.

The third parameter is a 32-bit integer that serves as an optional output parameter. If your stored procedure can modify one or more records, you can use this parameter to return the number of records affected by the stored procedure's execution.

As you learned earlier, stored procedures can be passed parameters and can return a result set. Both the input parameters and the results set returned by stored procedure functions are passed between the AEP and Advantage using in-memory ADT tables. The table containing the input parameters is named \_ \_input, and the table you use to return a result set is named \_ \_output. (Both of these table names are preceded by two consecutive underscore characters.)

These tables can be accessed from within your stored procedure function through the connection handle. Recall that this same connection handle is passed to the startup and shutdown functions, as well as to the stored procedure functions. For efficiency, most developers initialize this connection in the state maintenance object that is saved in the startup function. From within a given stored procedure, the state maintenance object for this connection ID is retrieved, and the connection is then used to read the input parameters from the \_ \_input table, if necessary. (Not all stored procedures use input parameters.)

As the stored procedure executes, any data that it needs to return to the invoking client is inserted into the \_ \_output table. As must be obvious, the \_ \_output table is always an empty table when the stored procedure function begins executing.

The structures of the \_ \_input and \_ \_output tables are defined when you register your stored procedure in a data dictionary. When registering a stored procedure in a data dictionary, you provide names and data types for all of your input and output parameters. The \_ \_input table will have one field for each input parameter, and the \_ \_output table will have one field for each output parameter.

If you are passing at least one input parameter to your stored procedure function, the \_ \_input table will have exactly one record. The \_ \_output table, by comparison, is always empty when your stored procedure function is entered. If your stored procedure function returns data, it must insert one or more records into the \_ \_output table.

How many records a stored procedure function inserts into the \_ \_output table is up to you. If your stored procedure simply needs to return a completion code, indicating whether or not an operation was successful, you might write a single record containing a single logical field to \_ \_output. On the other hand, if your stored procedure function is designed to return one record for each invoice associated with a given customer, \_ \_output may include hundreds (or thousands or millions) of records.

There is a third temporary table accessible through the connection handle. This table, named \_ \_error, is an in-memory table. Unlike the \_ \_input and \_ \_output tables, the \_ \_error table is available to the startup and shutdown functions as well.

The \_ \_error table has two fields. The first field is an integer field named ERRORNO, and the second is a memo field named MESSAGE. If you want to return a custom error message, you add a single record to this table, setting ERRORNO to your custom error number and setting MESSAGE to your error message. If you want to return a custom message, but want to use Advantage's standard AEP error code, leave ERRORNO empty.

By default, the \_ \_error table is empty. If you write to \_ \_error, you only write a single record. Writing a record to \_ \_error causes Advantage to raise an exception on the client connection, returning the error code and message.