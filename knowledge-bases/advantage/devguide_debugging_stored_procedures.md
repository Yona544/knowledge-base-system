Debugging Stored Procedures




Advantage Database Server 12  

     Debugging Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Debugging Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Debugging Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Debugging\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Debugging Stored Procedures / Dear Support Staff, |  |
| Debugging Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There is no debugger for SQL stored procedures. As a result, debugging these SQL scripts requires close attention to the errors returned by your stored procedures. Fortunately, the SQL Utility provides you with a convenient tool for executing your stored procedures and viewing any errors returned by them.

For AEPs, you debug these using the debugging features of your development environment. Most development environments permit you to set breakpoints in your code, and then cause an external host to load your compiled application. In Visual Studio .NET, the external application is referred to as the calling application, whereas in Borland products, it is called the host application.

   
NOTE: Most developers debug their AEPs using ALS. However, beginning with ADS 7.0, the Windows NT/2000/2003 and Linux versions of the ADS server have an -exe command-line option, permitting ADS to be used during debugging. See the Advantage documentation for more information on this feature.  
 

When the external application calls your AEP and encounters the breakpoint, your application is loaded into the debugger. From that point, you can use the tools of your development environment's debugger to inspect variables, evaluate expressions, and step into or over individual instructions.

For specific information on debugging DLLs, shared object libraries, COM objects, and .NET class libraries, see the documentation for your particular development environment.

   
NOTE: In some cases you may need to adjust one or more properties of the project before it can be loaded by your development environment's debugger. For example, with a Delphi AEP, you must use the linker page of the Project Options dialog box to instruct the compiler to include TD32 debug info and include remote debug symbols. Once you are through debugging your AEP, be sure to turn off these settings before you deploy your AEP container.