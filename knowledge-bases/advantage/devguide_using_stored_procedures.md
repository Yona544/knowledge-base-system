Using Stored Procedures




Advantage Database Server 12  

 

     Using Stored Procedures

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Using Stored Procedures Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Stored\_Procedures Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Using Stored Procedures / Dear Support Staff, |  |
| Using Stored Procedures  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Once you have written your stored procedures, and in the case of AEPs, compiled it and installed it on the machines from which it will be executed, you will need to add one stored procedure object to your data dictionary for each stored procedure function that you want to call. For example, if you have an AEP library with five stored procedure functions, and want to be able to call all of them from your client applications, you will need to create five stored procedure objects. Creating stored procedure objects for AEPs is discussed in the next section.

In addition to creating stored procedure objects, if your data dictionary is set up to require logins and check user rights, you will need to grant permissions to the groups and/or users who need to execute the stored procedures. Granting permissions to stored procedures is discussed later in this section.

Installing the SQL stored procedure was described earlier in this chapter in the section "Creating and Installing SQL Stored Procedures." Consequently, the following discussion applies specifically to AEPs.