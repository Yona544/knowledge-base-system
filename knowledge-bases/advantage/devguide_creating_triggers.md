Creating Triggers




Advantage Database Server 12  

 

     Creating Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Creating Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Creating Triggers / Dear Support Staff, |  |
| Creating Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you are creating SQL script triggers, you can write and configure your triggers entirely in the Advantage Data Architect. In fact, if you needed to, you can create your triggers at runtime using SQL. However, creating triggers, like stored procedures, is often part of your overall database design process, which means that you are most likely to create and register your triggers at design time.

For any trigger other than SQL scripts, creating and registering the trigger requires two distinct steps. In the first step, you create the trigger library using your development environment of choice. You can then register the trigger for your data dictionary using the Advantage Data Architect, although this registration can also be performed programmatically at runtime, if necessary. If you are creating your triggers using SQL scripts, you define your SQL and configure the trigger all within the provided Triggers dialog box in the Advantage Data Architect.