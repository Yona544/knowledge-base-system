Testing and Debugging an Advantage Extended Procedure




Advantage Database Server 12  

Testing and Debugging an Advantage Extended Procedure

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Testing and Debugging an Advantage Extended Procedure  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Testing and Debugging an Advantage Extended Procedure Advantage Concepts master\_Testing\_and\_debugging\_an\_advantage\_extended\_procedure Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Testing and Debugging an Advantage Extended Procedure / Dear Support Staff, |  |
| Testing and Debugging an Advantage Extended Procedure  Advantage Concepts |  |  |  |  |

Because Advantage Extended Procedures are libraries, there are many ways to test them. One of the simplest methods is to use the [Advantage Local Server](master_advantage_local_server.htm) and designate a host application that will call the AEP. A host application can be a simple client application that calls your procedure. You can then assign the test application to be the host debug application for your debug session. This feature is available in virtually all development environments.

If your development environment does not provide this functionality, or if you would prefer to keep Advantage out of the picture until your procedure is fully developed, it is also possible to debug your procedure by calling it directly. You can create two Advantage Database Tables (ADTs), one for input parameters and one for output parameters. Populate the input parameter table, and then call your AEP function directly.

Note to TDataSet Descendant users If execution does not stop on your breakpoints, you may need to modify your linker options. See [Task 7 - Test your Procedure](master_task_7_test_your_procedure.htm) for more information about debugging an Advantage Extended Procedure.

Debugging using the Advantage Database Server

The process of debugging an AEP using the Advantage Database Server (as opposed to the Advantage Local Server) is only slightly different. Instead of specifying the tester application as the host debug application, instead specify the Advantage Database Server (ads.exe in Windows, adsd in Linux) and in the Parameters edit box type "-exe". If the Advantage Database Server is currently running on the computer you will be debugging from, stop it. Now when you start your debug session, Delphi/Kylix will start a copy of the Advantage Database Server (which will run as an executable). Start tester.exe or any other application that will call your AEP as a new process and start debugging.

Note You must disable DLL Caching before debugging AEPs using Advantage Database Server. DLL Caching will cause Advantage Database Server to load a copy of the AEP container rather than the original container. See [DLL Caching](master_dll_caching.htm) for more information.