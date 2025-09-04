Defining Users and Groups




Advantage Database Server 12  

     Defining Users and Groups

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Defining Users and Groups  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Defining Users and Groups Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Defining\_Users\_and\_Groups Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Defining Users and Groups / Dear Support Staff, |  |
| Defining Users and Groups  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

An administrative user is created when you first create a data dictionary. The user name for the user is ADSSYS, and this user is specifically designed to manage the configuration of the data dictionary.

In most cases, you do not use this user name for regular data access. For nonadministrative access to a data dictionary, you should establish one or more regular users. (Regular user, as the term is used here, is any user other than ADSSYS.) In the simplest case, you create a single regular user and provide that user name and password (the password could even be blank) for all of your users. If there is going to be only one user, and that user is you, this approach is usually more than adequate.

   
NOTE: Some applications, such as Web server extensions, are inherently more secure as long as you've installed them correctlyfor example, placing them in a virtual directory of your Web server, and configuring that directory with execute, but not read, privileges. For applications like these, a single regular user account is sufficient to permit your application to connect to the data dictionary through ADS while preventing access by unauthorized local users.  
 

If your client application is used by more than one user, you should consider having more than one nonadministrative user. Having more than one user permits you to exert greater control over access to your database.

For example, imagine that you are writing a database application that will be used by several employees in your company. If one of those employees is subsequently terminated or leaves, you probably want to revoke their access to the database, particularly if the database contains sensitive information. If each employee has their own user name and password, you can revoke the former employee's access by removing their associated user name from the data dictionary.

Granted, if security is not an issue, you may conclude that the benefits of multiple passwords are not worth the additional administration. Nonetheless, if you do opt for multiple user names, you should also consider making use of groups. Groups are discussed later in this section.

   
TIP: Best practices dictate that you should never grant a user more rights than they need. As a result, it is considered bad form to permit a client application to log into a data dictionary using the ADSSYS account. If you need a user account that has rights to manage data dictionary objects, including creating and granting rights to users, create a special user account with all available rights. That account would then have to rights to perform any necessary task with the exception of enabling/disabling query logging and disabling/enabling data dictionary logins.