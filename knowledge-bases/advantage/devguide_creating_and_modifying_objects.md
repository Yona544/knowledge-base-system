Creating and Modifying Objects




Advantage Database Server 12  

 

     Creating and Modifying Objects

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating and Modifying Objects  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Creating and Modifying Objects Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_and\_Modifying\_Objects Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Creating and Modifying Objects / Dear Support Staff, |  |
| Creating and Modifying Objects  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Which came first, the table or the data? The data, of course, which is why you need the table in the first place. But seriously, you can't have a database without one or more tables. Furthermore, tables are not much use if you do not have indexes for them. After that, views, stored procedures, triggers, and the like prove quite valuable.

This section covers three essential SQL statements: CREATE, ALTER, and DROP. You use CREATE to create tables and data dictionary objects, ALTER to modify the structure of an existing table, and DROP to destroy objects. Each of these statements is covered in the following sections.