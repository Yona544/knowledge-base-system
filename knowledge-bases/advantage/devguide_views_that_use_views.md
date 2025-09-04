Views That Use Views




Advantage Database Server 12  

 

     Views That Use Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Views That Use Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Views That Use Views Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Views\_That\_Use\_Views Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 6 - Views > Views That Use Views / Dear Support Staff, |  |
| Views That Use Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Earlier in this chapter, you learned how to execute a SQL SELECT statement against the Employee Tab view using the SQL Utility. Since a view itself is defined using a SQL statement, there is no reason why the SQL SELECT statement used in a view cannot query a view.

Views that use views can be employed in a number of interesting ways. Two of these techniques are covered in this section. In the first technique, you will learn how views can be used to modularize operations on your data. In the second, you will see how a view can be used as a temporary table.