Implementing Security with Data Dictionaries




Advantage Database Server 12  

 

     Implementing Security with Data Dictionaries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Implementing Security with Data Dictionaries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Implementing Security with Data Dictionaries Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Implementing\_Security\_with\_Data\_Dictionaries Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Implementing Security with Data Dictionaries / Dear Support Staff, |  |
| Implementing Security with Data Dictionaries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While encrypting your database tables prevents someone from viewing the data in your table files directly, it does nothing to prevent those tables from being accessed by client applications designed to work with a data dictionary. If you want to control who can access your tables, you have to implement security for your data dictionary.

You can take a number of specific steps to ensure that your data is accessed only by authorized users. These include requiring users to log in prior to providing them with access to your database tables, as well as setting up the user names and passwords that users use to log in. These topics are covered in the following sections.