Deleting Records




Advantage Database Server 12  

     Deleting Records

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Deleting Records  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Deleting Records Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Deleting\_Records Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Deleting Records / Dear Support Staff, |  |
| Deleting Records  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You delete records from a table using the DELETE statement. With DELETE, you use the optional WHERE clause to define which records to delete. If you omit the WHERE clause, all records are deleted from the table.

For example, the following query will remove all records from the #TEMP table where the Active field contains the value False:

DELETE FROM #TEMP  
  WHERE Active = False

You can use a subquery to delete records from a table based on values in another table. For example, the following DELETE statement removes all records from #TEMP where the Full Name field is associated with an employee whose department code is 104:

DELETE FROM #TEMP  
  WHERE [Full Name] IN   
    (SELECT RTRIM(Emp.[First Name]) + ' ' +   
         RTRIM(Emp.[Last Name])  
       FROM EMPLOYEE Emp  
       WHERE Emp.[Department Code] = 104)