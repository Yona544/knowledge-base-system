---
title: Master Task 7 Test Your Procedure
slug: master_task_7_test_your_procedure
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_7_test_your_procedure.htm
source: Advantage CHM
tags:
  - master
checksum: 78749373af30c5861556ca405871c4adba8ed9c9
---

# Master Task 7 Test Your Procedure

Task 7: Test Your Procedure

Task 7: Test Your Procedure

Advantage Concepts

| Task 7: Test Your Procedure  Advantage Concepts |  |  |  |  |

Its time to test your procedure. Because your AEP container is a library, there are many ways to test your procedure. One of the simplest methods is to designate a host application that will call your AEP container. A host application, tester.exe ("tester" in Linux), has been provided for you, and should have been in the database directory that you copied in Task 1.

Assign Debug Host Application:

| 1. | Select Parameters from the Run menu. |

| 2. | WINDOWS USERS: Enter X:\data\Tester.exe in the Host Application edit box. |

LINUX USERS: Enter ~/data/tester in the Host Application edit box.

| 3. | Click OK. |

Youve now configured Delphi/Kylix to run the tester executable when you debug MyFirstProcedure.dpr. When the code executed in the test application runs your procedure, execution will stop anywhere youve set up a breakpoint.

Set Breakpoints:

| 1. | Set a breakpoint at the top of your Startup function (F5). |

| 2. | Set a breakpoint at the top of your Shutdown function (F5). |

| 3. | Set a breakpoint at the top of your MyProcedure function (F5). |

Debug Your Procedure:

Press [F9] to begin debugging your first AEP. The test application will run. Select the input parameter values then press the Exec Procedure button. Execution should stop at your breakpoint in the Startup function.

Note If execution does not stop on your breakpoint you may need to modify your linker options. Select Options from the Project menu. Select the Linker tab, and verify the Include TD32 Debug Info and the Include Remote Debugging Symbols check boxes are both checked. Rebuild your AEP, and try again.

Press [F9] to continue debugging. This time program execution should stop at your breakpoint in the MyProcedure function. Take a few moments to step through this function and learn how the input parameters were retrieved, and how the output parameters were returned.

Note If you dont want to use the tester application, the Advantage Data Architect (ARC) can also be used to test your procedures. Simply open the SQL interface in ARC and use the EXECUTE PROCEDURE syntax to test your procedure.

Figure 3 tester.exe

Debugging using the Advantage Database Server

The process of debugging an AEP using the Advantage Database Server (as opposed to the Advantage Local Server) is only slightly different. Instead of specifying the tester application as the host debug application, specify the Advantage Database Server (ads.exe in Windows, adsd in Linux) and in the Parameters edit box type "-exe". If the Advantage Database Server is currently running on the computer you will be debugging from, stop it. Now when you start your debug session, Delphi/Kylix will start a copy of the Advantage Database Server (which will run as an executable). Start tester.exe or any other application that will call your AEP as a new process and start debugging.

Alternate Debugging Method

It is also possible to debug your procedure by calling it directly. You could create two Advantage Database Tables (ADTs), one for input parameters and one for output parameters. Populate the input parameter table, and then call your AEP function directly.

Congratulations!

Youve just finished your first AEP. You should now know the fundamentals of AEP development. If you have any other questions feel free to post them on our newsgroups, which can be reached from the Advantage Developer Zone Web site at http://DevZone.AdvantageDatabase.com.
