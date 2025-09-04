Exporting Table Structures As Code




Advantage Database Server 12  

     Exporting Table Structures As Code

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Exporting Table Structures As Code  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Exporting Table Structures As Code Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Exporting\_Table\_Structures\_As\_Code Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > Exporting Table Structures As Code / Dear Support Staff, |  |
| Exporting Table Structures As Code  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

At the beginning of this chapter, you learned that you can either create tables at design time using the Advantage Data Architect, or you can create tables in code at runtime. As mentioned during that discussion, creating tables in code at runtime requires that you create, debug, and maintain the code that defines the table structures.

Fortunately, the Advantage Data Architect can help. Specifically, so long as you have an existing Advantage table structure, the Tables to Code dialog box of the Advantage Data Architect can generate code that will create that table at runtime, including the indexes. You can then use that code in your client application to create the table and its indexes at runtime.

Use the following steps to generate a SQL script that can re-create your CUST.ADT table at runtime from a client application:

From the Advantage Data Architect main menu, select Tools | Export Table Structures as Code. The Advantage Data Architect responds by displaying the Tables To Code dialog box shown in Figure 2-12.

Figure 2-12: The Tables To Code dialog box

Click the Add Table(s) button to display a browser window. The tables associated with your FreeTableConnection connection are displayed. Select CUST.ADT and click Open. (You can select two or more tables if your current connection points to more than one table.)

The name of your selected table appears in the Tables To Code dialog box. If your free table has more than one index file, you can right-click in the Tables To Code dialog box and select those additional indexes. Currently there are no index files for the CUST.ADT table.

You can generate code in one of three formats: Delphi, C++Builder, or SQL script. At the Select Type of Output Code option, select SQL.

The generated code can either create the table, or it can create the table and populate it with data. If you have selected to output the generated code using SQL scripts, you can check the Include Existing Data checkbox to populate the generated table with its current data. Leave this checkbox unchecked for this demonstration. Click OK to continue with your code generation.

If you select Delphi or C++ Builder formats, you will see an Output Code window where you can copy the code to the Windows Clipboard or save your code to a file. When you select the SQL script format, your code is displayed in the SQL Utility as shown in Figure 2-13. From this window you can use to the SQL Utility toolbar to copy the code, edit it, or verify syntax, or to save the code to a file.

Figure 2-13: The SQL output code to generate the CUST.ADT table in the SQL Utility

   
CAUTION: Testing the code output by the Table to Code generator may produce errors if you attempt to create a new table using the same name as your existing table. This code is normally intended to be executed from a client application to create a table where no table currently exists.  
 

 

In the next chapter, you will learn about the importance of ADS indexes and how to create them for your tables.