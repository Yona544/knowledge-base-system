AEP Interface Version Comparison




Advantage Database Server 12  

AEP Interface Version Comparison

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AEP Interface Version Comparison  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - AEP Interface Version Comparison Advantage Concepts master\_Aep\_interface\_version\_comparison Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > AEP Interface Version Comparison / Dear Support Staff, |  |
| AEP Interface Version Comparison  Advantage Concepts |  |  |  |  |

AEP Interface versions are used to specify which pre-defined interface the Advantage server should use when executing an AEP. With the introduction of Advantage v7.0 (which included an updated AEP interface), a mechanism to determine the format of the AEP functions (Startup, Shutdown, and user functions) was necessary.

If the AEP container (Win32 DLL, .NET Assembly, etc.) exports a function called GetInterfaceVersion, the Advantage server will use the return value from this function to determine what format to use when calling the AEPs in that container. If the AEP container does not export the GetInterfaceVersion function, the Advantage server will assume it is dealing with a version 1 interface.

A description of each interface is included below.

AEP Interface Version 1

This AEP interface was the first AEP interface, and is supported only for backwards-compatibility. For a definition of the function prototypes used by version 1 AEPs, consult the Advantage v6.0 v6.2 help documentation.

AEP Interface Version 2

This AEP interface includes the following enhancements over the version 1 interface:

|  |  |
| --- | --- |
| · | AEP is passed an active connection handle, as opposed to a username and password. This active connection handle can be used to perform all data operations. No additional connections are required. |

|  |  |
| --- | --- |
| · | AEPs can be called inside a transaction, and all operations performed using the active connection handle passed to the AEP are included in the context of the transaction. |

|  |  |
| --- | --- |
| · | Input and output parameters are passed through the virtual tables \_\_input and \_\_output, no more parsing input/output table paths. |

|  |  |
| --- | --- |
| · | An additional connection to read the input and output tables is no longer necessary. |

|  |  |
| --- | --- |
| · | An in-memory table (\_\_error) can be used to return descriptive error messages to the client application. |

|  |  |
| --- | --- |
| · | The number of rows affected can be returned and used from the client application just like it can with traditional SQL INSERT/UPDATE/DELETE statements. |