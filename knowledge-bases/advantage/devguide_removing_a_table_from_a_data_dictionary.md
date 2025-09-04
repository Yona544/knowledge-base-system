Removing a Table from a Data Dictionary




Advantage Database Server 12  

     Removing a Table from a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Removing a Table from a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Removing a Table from a Data Dictionary Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Removing\_a\_Table\_from\_a\_Data\_Dictionary Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Removing a Table from a Data Dictionary / Dear Support Staff, |  |
| Removing a Table from a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You remove a table from a data dictionary by selecting the table you want to remove from the TABLES node of the corresponding data dictionary connection and pressing the Delete key. Removing a table from a data dictionary frees the table, but does not delete it. If you want to erase a table that you have removed from the data dictionary in this way, you can do so by manually deleting the table's files from the directory (using Windows Explorer, for example).

You can also use the SQL DROP TABLE statement to remove a table from a data dictionary. This approach both removes the table from the dictionary and deletes it permanently.

   
CAUTION: There is a utility called FREEADT.EXE that can be used to free tables from a data dictionary. (This utility is located in the same directory as the Advantage Data Architect executable.) This utility should normally only be used when a data dictionary has been deleted, but the associated tables are still marked as bound to a database.