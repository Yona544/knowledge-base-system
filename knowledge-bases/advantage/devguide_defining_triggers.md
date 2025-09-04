Defining Triggers




Advantage Database Server 12  

     Defining Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Defining Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Defining Triggers Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Defining\_Triggers Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Defining Triggers / Dear Support Staff, |  |
| Defining Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A trigger is similar to a stored procedure in many respects. Like a stored procedure, a trigger is an object that is defined in a data dictionary. However, unlike stored procedures, triggers are not executed by client applications. Instead, they are executed by Advantage in response to row-level data operations.

In this chapter, you will learn how to create and register triggers. We begin with a look at the types of triggers that are supported by Advantage. Next, you will find trigger examples written in SQL, Delphi, C#, and VB for .NET. Finally, you will learn how to register and configure triggers.

   
NOTE: If you are unfamiliar with SQL, you may also want to refer to Chapters 10 through 14 while reading this chapter.