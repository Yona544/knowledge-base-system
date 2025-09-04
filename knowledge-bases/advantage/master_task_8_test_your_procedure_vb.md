Task 8: Test Your Procedure




Advantage Database Server 12  

Task 8: Test Your Procedure

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 8: Test Your Procedure  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 8: Test Your Procedure Advantage Concepts master\_Task\_8\_test\_your\_procedure\_vb Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Visual Basic Tutorial > Task 8:  Test Your Procedure / Dear Support Staff, |  |
| Task 8: Test Your Procedure  Advantage Concepts |  |  |  |  |

Its time to test your procedure. Because your AEP container is a library, there are many ways to test it. One of the simplest methods is to designate a host application that will call your AEP container. A host application, aep\_tester.exe, has been provided for you, and should have been in the database directory that you copied in Task 1.

Assign Debug Host Application

|  |  |
| --- | --- |
| 1. | Right-click AdvantageAEP1 in the Solution Explorer and select Properties from the menu. |

|  |  |
| --- | --- |
| 2. | Select Debugging from the Configuration Properties folder. |

|  |  |
| --- | --- |
| 3. | Choose Start External Program as the Start Action, and enter the path to aep\_tester.exe |

|  |  |
| --- | --- |
| 4. | Click OK. |

Youve now configured Visual Studio to run the aep\_tester executable when you debug AdvantageAEP1. When the code executed in the test application runs your procedure, execution will stop anywhere youve set up a breakpoint.

Set Breakpoints

|  |  |
| --- | --- |
| 1. | Set a breakpoint at the top of your Startup function (F9). |

|  |  |
| --- | --- |
| 2. | Set a breakpoint at the top of your Shutdown function (F9). |

|  |  |
| --- | --- |
| 3. | Set a breakpoint at the top of your MyProcedure function (F9). |

Debug Your Procedure

Press [F5] to begin debugging your first AEP. The test application will run. Select the input parameter values then press the Exec Procedure button. Execution should stop at your breakpoint in the Startup function.

Press [F5] to continue debugging. This time program execution should stop at your breakpoint in the MyProcedure function. Take a few moments to step through this function and learn how the input parameters were retrieved, and how the output parameters were returned.

Note If you dont want to use the tester application, the Advantage Data Architect (ARC) can also be used to test your procedures. Simply open the SQL interface in ARC and use the EXECUTE PROCEDURE syntax to test your procedure.

Figure 3 tester.exe

Debugging using the Advantage Database Server

The process of debugging an AEP using the Advantage Database Server (as opposed to the Advantage Local Server) is only slightly different. Instead of specifying the tester application as the host debug application, instead specify the Advantage Database Server (ads.exe in Windows, adsd in Linux) and in the Parameters edit box type "-exe". If the Advantage Database Server is currently running on the computer you will be debugging from, stop it. Now when you start your debug session, Visual Studio will start a copy of the Advantage Database Server (which will run as an executable). Start aep\_tester.exe or any other application that will call your AEP as a new process and start debugging.

Alternate Debugging Method

It is also possible to debug your procedure by calling it directly. You could create two Advantage Database Tables (ADTs), one for input parameters and one for output parameters. Populate the input parameter table, and then call your AEP function directly.

Congratulations!

Youve just finished your first AEP. You should now know the fundamentals of AEP development. If you have any other questions feel free to post them on our newsgroups, which can be reached from the Advantage Developer Zone Web site at http://DevZone.AdvantageDatabase.com.