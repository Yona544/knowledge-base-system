Creating Stored Procedures




Advantage Database Server 12  

     Creating Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Creating Stored Procedures / Dear Support Staff, |  |
| Creating Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A stored procedure is a subroutine that performs a unit of work. By creating stored procedures, you create reusable operations that can be called from any of your client applications.

Advantage provides you with great flexibility when it comes to creating stored procedures. Unlike most relational database servers, which often provide only one or two mechanisms for writing stored procedures, the stored procedures that you create for Advantage can be written using SQL scripts, as well as almost any language from which you can compile Windows DLLs (dynamic link libraries), Linux so (shared object) libraries, in-process COM (component object model) servers, or .NET class libraries.

This chapter provides you with an in-depth look at stored procedures. It begins with a detailed overview of the benefits that stored procedures can bring to your applications. Next, you learn about a special type of stored procedure supported by Advantage called Advantage Extended Procedures, or AEPs.

Later in this chapter, you will find step-by-step instructions on how to create stored procedures using SQL, Delphi, C# for .NET, and VB for .NET. This chapter concludes by describing how to install, test, debug, and deploy your newly created stored procedures.