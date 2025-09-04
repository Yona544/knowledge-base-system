Creating AEPs Using Visual Basic 6




Advantage Database Server 12  

     Creating AEPs Using Visual Basic 6

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating AEPs Using Visual Basic 6  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating AEPs Using Visual Basic 6 Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_AEPs\_Using\_Visual\_Basic\_6 Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Creating AEPs Using Visual Basic 6 / Dear Support Staff, |  |
| Creating AEPs Using Visual Basic 6  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage provides a template for creating COM objects with Visual Basic 6. In short, the process is very similar to the process you use when you implement a .NET class library in VB for .NET.

There is one very important difference between COM objects created with Visual Basic 6 and those created with Visual Studio .NET, C#Builder, Delphi, Kylix, and C++Builder. The COM objects that Visual Basic 6 produces create the COM object in a single threaded apartment (STA). All calls made to stored procedures in an STA are performed using the Windows message queue, which has the effect of serializing these calls.

The fact that calls to Visual Basic 6created COM objects are serialized dramatically reduces the value of these types of AEPs. Recall that stored procedures in an AEP are called from a thread on the Advantage Database Server. Many threads can be running concurrently, and if two or more threads need to call a stored procedure in a specific AEP at the same time, the execution of these calls normally proceeds concurrently.

This concurrent processing does not happen when the AEP is compiled as a COM object using Visual Basic 6. Instead, the first thread to call a stored procedure will begin executing it, and a second thread must wait until that execution is complete before being able to proceed with the stored procedure execution. As a result, Visual Basic 6 AEP COM objects represent a potentially serious performance bottleneck.

If you are a Visual Basic 6 developer, and your AEP is called only occasionally or by only one client, there is probably little harm in creating your AEP using Visual Basic 6. However, if your AEP is one that is called frequently from several different clients, you will be much better off creating your AEP using one of the other development environments, even if your client applications are written in Visual Basic 6.