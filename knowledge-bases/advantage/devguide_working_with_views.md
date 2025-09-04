Working with Views




Advantage Database Server 12  

    Working with Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Working with Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -     Working with Views Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Working\_with\_Views Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Working with Views / Dear Support Staff, |  |
| Working with Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A view is an object that contains a SQL SELECT statement that produces a result set containing zero or more records and at least one field. From the perspective of your applications, a view is like a table in your database.

This chapter shows you how to create and configure views. It begins by showing you how to define views. Later topics in this chapter include testing views, controlling view rights, querying views, and using views to link to tables outside of your data dictionary.

   
NOTE: If you are unfamiliar with SQL, you may also want to refer to Chapters 11, 12, 13, and 14 while reading this chapter.