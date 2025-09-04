Creating Tables




Advantage Database Server 12  

     Creating Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Tables Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Tables Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > Creating Tables / Dear Support Staff, |  |
| Creating Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A table is a structured file that holds data about a particular subject. For example, you might have one table that contains information about customers and another table that contains information about sales.

Tables are organized by rows and columns. Each row contains information about one object. The customer table, for example, will contain one row for each customer. These rows are commonly referred to as records, but the terms are interchangeable.

A table may have zero or more records. A table with zero records is referred to as an empty table.

Each row in a table consists of one or more columns, with every row in a given table having the same number of columns. Each column is used to hold a particular piece of information about the subject associated with the table. For example, the customer table may have one column that holds the customer's account number, and another column that holds the customer's name, and so on. Columns are also referred to as fields.

Memo files are special files that hold a table's variable-length data (binary, image, and memo fields in Advantage). For example, your customer table may have a memo field used to hold a description of each customer. While some, or even all customer records may not have a description, whenever a description is present, it is stored in the memo file. With Advantage tables, all binary, image, and memo fields for a particular table are stored in a single memo file. In addition, a table and its associated memo file (if present) have the same name. Only their file extensions differ.

In most cases, your application will reference the tables directly, but does not have to explicitly refer to any index or memo files. In most cases, Advantage takes complete responsibility for accessing the indexes and memo files. For example, so long as you have only one structural index file for a table, any time you access that table through Advantage, Advantage opens the table, and opens its structural index and memo files if these files are present.

   
NOTE: The term "structural index" is originally a FoxPro term used to refer to the index file that has the same filename as its associated table. We have adopted this term to refer to any index file for an Advantage table that has the same name as its associated table. While some people prefer to refer to these index files as "auto-open" index files, we feel that the term auto-open is less appropriate now that all of a table's indexes are auto-opened when you access the Advantage table through a data dictionary.