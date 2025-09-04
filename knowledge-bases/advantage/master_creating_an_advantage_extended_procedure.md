Creating an Advantage Extended Procedure




Advantage Database Server 12  

Creating an Advantage Extended Procedure

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating an Advantage Extended Procedure  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Creating an Advantage Extended Procedure Advantage Concepts master\_Creating\_an\_advantage\_extended\_procedure Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Creating an Advantage Extended Procedure / Dear Support Staff, |  |
| Creating an Advantage Extended Procedure  Advantage Concepts |  |  |  |  |

This section provides a high-level overview of creating an Advantage Extended Procedure. TDataSet users will find a step-by-step [Advantage TDataSet Descendant tutorial](master_advantage_extended_procedures_tdataset_tutorial.htm), along with examples installed with the Advantage TDataSet Descendant product. Visual Basic users will find a [Visual Basic step-by-step tutorial](master_advantage_extended_procedures_visual_basic_tutorial.htm), along with the examples installed with the Advantage OLEDB Provider (for ADO). C programmers will find detailed example applications included with the installation of the Advantage Client Engine (ACE).

Create an AEP Source File

Advantage Extended Procedures containers are implemented as Windows DLLs, COM libraries, .NET assemblies, or Linux shared objects. Create a new DLL project, COM library, .NET assembly, or shared object using the development environment of your choice. Possible development environments include Microsoft Visual C++, Microsoft Visual Basic .NET, Borland Delphi, Borland C++Builder, Borland Kylix, CA Visual Objects, and any other environment capable of generating Windows DLLs, COM libraries, .NET assemblies, or Linux shared objects.

In Windows, the default extension of the library generated will be .dll. Modify the project to generate an output library with an AEP extension. For example, MyFirstProc.aep. Note, however, this step is only necessary if creating a standard Windows DLL. If you are creating a COM library the extension should be left as .dll.

In Linux, the default name of the library will be libmytest.so.X.YY.Z, where X, Y, and Z are version numbers. Modify the project to generate a library of the form mytest.aep.

TDataSet Descendant users

An AEP template has been provided for you, which makes generating your AEP as simple as creating a new project. After installing the Advantage TDataSet Descendant, select New from the File menu. Select the Advantage tab, and choose to create a new Advantage Extended Procedure.

Visual Basic and Visual C# .NET users

An AEP template has been provided for you, which makes generating your AEP as simple as creating a new project. After installing the Advantage .NET Data Provider, select New->Project from the VB or the C# File menu. Select AdvantageAEP from the list of templates.

Visual Basic 6 users

An AEP template class has been provided for you in the <oledb-provider-install-path>\examples\vb6aep\_template directory. To use this template select New Project from the File menu. Choose to create a new ActiveX dll project. Remove the default class (Class1) from the project. Add the vb6aep\_procedures.cls class from the examples directory to the project.

In Visual Basic 6 (as opposed to VB .NET) all ActiveX DLLs run in a single-threaded apartment. This means all global variables are safe because only one Advantage thread can be calling a stored procedure at any instance. While this makes writing an AEP simple (no need to protect global variables from other threads), it can cause major performance problems in a multi-user environment. It is recommended you use VB .NET or Visual C# .NET to write all Advantage AEPs.

Define Startup and Shutdown Functions

AEP containers can implement two special procedures; Startup and Shutdown. These functions are not required, but it is often necessary to perform initialization and clean-up tasks for each thread that uses your AEP. The Startup function will be called by Advantage, on a per-connection basis, the first time a procedure inside of the AEP container is called. The Shutdown function will be called, on a per-connection basis, as each connection that has used the AEP container is closed. This means the Startup function is called once for each Advantage connection that begins using procedures inside of the AEP container, and the Shutdown function is also called once for each Advantage connection that has used procedures inside of the AEP container.

Its important when developing AEPs to keep in mind that they will be run by a multi-threaded server (Advantage). The Advantage Database Server does not necessarily use the same thread every time it executes requests for the client, so thread variables are not a suitable solution for providing client-specific storage in an AEP. All AEP functions are passed the unique identifier, ulConnectionID. This parameter can be used by the developer to uniquely identify a client connection. Resources allocated on behalf of the client (connections, open tables, etc.) can be tied to this unique connection ID, and retrieved at a later time.

The Startup and Shutdown functions must be implemented using a standard function prototype defined by Advantage. Below you will find the Object Pascal, VB.NET, C#.NET, and the C prototypes for these functions:

Object Pascal

function Startup( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE )

: UNSIGNED32; stdcall;

function Shutdown( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE )

: UNSIGNED32; stdcall;

Visual Basic .NET

Public Function Startup(ByVal ulConnectionID As Int32, \_

ByVal hConnection as Int32) As Int32

Public Function Shutdown(ByVal ulConnectionID As Int32, \_

ByVal hConnection as Int32) As Int32

Visual C# .NET

public Int32 Startup( Int32 ulConnectionID,

Int32 hConnection )

public Int32 Shutdown( Int32 ulConnectionID,

Int32 hConnection )

 

C

UNSIGNED32 \_declspec( dllexport ) WINAPI Startup

(

UNSIGNED32 ulConnectionID,

 

ADSHANDLE hConnection

)

UNSIGNED32 \_declspec( dllexport ) WINAPI Shutdown

(

UNSIGNED32 ulConnectionID,

 

ADSHANDLE hConnection

)

|  |  |
| --- | --- |
| Parameter | Description |
| ulConnectionID | A unique identifier that can be used to associate a user/connection with state-specific variables and other connection-specific information. |
| hConnection | Contains an active connection handle that can be used to perform all data operations. |

Define Your AEP EntryPoint

All Advantage Extended Procedures must be declared using the following prototype:

Object Pascal

function ProcedureName( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE;

pulNumRowsAffected: PUNSIGNED32 ): UNSIGNED32;

Visual Basic .NET

Public Function ProcedureName(ByVal ulConnectionID As Int32, \_

ByVal hConnection As Int32, \_

ByRef ulNumRowsAffected As Int32) As Int32

Visual C# .NET

public Int32 ProcedureName( Int32 ulConnectionID,

Int32 hConnection,

ref Int32 ulNumRowsAffected )

C

UNSIGNED32 \_declspec( dllexport ) WINAPI ProcedureName

(

UNSIGNED32 ulConnectionID,

ADSHANDLE hConnection,

UNSIGNED32 \*pulNumRowsAffected

)

 

|  |  |
| --- | --- |
| Parameter | Description |
| ulConnectionID | A unique identifier that can be used to associate a user/connection with state-specific variables and other connection-specific information. |
| hConnection | An active connection that can be used for all data operations. |
| ulNumRowsAffected | Optional output parameter that can be used to specify how many rows were updated. |

Implement Your Procedure Logic

Once youve declared your procedure youre free to implement your business logic in any manor you see fit. You have the complete functionality of your development environment at your fingertips.

Note to .NET users: It is important to clean up all AdsCommand (IDbCommand) objects by calling the Dispose method. The Dispose method ensures that the underlying statement handles are cleaned up. If Dispose is not called, then it is possible for the .NET garbage collector to dispose the object. Because these assemblies are executed within the Advantage Database Server process space, this means that the call will come into the server code on an unexpected thread and can result in undefined behavior.

Return Any Errors Using the \_\_error Table

The \_\_error table is an in-memory table and is used to return an error code and/or error string from inside of a procedure. The \_\_error table has the following table definition:

INTEGER errno

MEMO  message

If your procedure code writes a row to this table, the Advantage server will read the error number and message from the \_\_error table and return them to the client as a native exception or error code (depending on which client you are using). The errno field is optional, and if left empty, a default procedure failure error code will be returned to the client.

Register Your Procedure with a Data Dictionary

The final step in generating a new AEP is to register the procedure in your Advantage Data Dictionary. There are several ways to accomplish this task.

The Advantage Data Architect (ARC) provides a graphical interface that can be used to register your procedures. Reference the Advantage Data Architect Help (ARC.HLP or arc.htm) for more details. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

It is also possible to use SQL commands to register your procedure. See [CREATE PROCEDURE](master_create_procedure.htm) for details.