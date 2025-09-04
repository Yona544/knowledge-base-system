Application Identification




Advantage Database Server 12  

     Application Identification

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Application Identification  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Application Identification Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Application\_Identification Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Application Identification / Dear Support Staff, |  |
| Application Identification  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Client applications can now be programmatically identified using Advantage's new application identification feature. By default, application identification resolves to the name of the executable that is connected to Advantage. If you want, you can also programmatically set the application identification for a particular client application through the sp\_SetApplicationID system stored procedure.

There are two ways to read the application ID. You can use the Advantage SQL scalar function APPLICATIONID, or the sp\_GetApplicationID system stored procedure. These functions are particularly useful from within triggers and stored procedures, permitting you to note which of your client applications is causing the routine to execute.