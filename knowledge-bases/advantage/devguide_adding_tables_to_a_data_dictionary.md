Adding Tables to a Data Dictionary




Advantage Database Server 12  

 

     Adding Tables to a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Adding Tables to a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Adding Tables to a Data Dictionary Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Adding\_Tables\_to\_a\_Data\_Dictionary Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Adding Tables to a Data Dictionary / Dear Support Staff, |  |
| Adding Tables to a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While a data dictionary provides you with access to a number of different types of objects, these aren't very useful unless you have tables for them to work with. As a result, adding tables to a newly created data dictionary is often one of your first tasks.

You can add any of the ADS-supported table types to a data dictionary, but it is nearly always preferable to use ADT tables. Not only do ADT tables have superior characteristics compared to DBF tables, but when used with data dictionaries, the definitions for these tables that you save to your data dictionary will always be respected.

There are a number of different ways that tables can be added to a data dictionary. You can right-click the TABLES node in the Connection Repository and select Create. Doing so displays the Table Designer dialog box demonstrated in Chapter 2. You use this dialog box to define the structure of the new table you want created, as well as to set table properties and define indexes. When you click OK from this dialog box, the new table is created and bound to the data dictionary associated with the connection (assuming of course that the connection is a data dictionary connection).

Alternatively, you can add existing free tables to the data dictionary. This second approach is the one that you are going to use in the following section.