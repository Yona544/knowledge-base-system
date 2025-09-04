7074 The table ID stored in the ADT table does not match the ID stored in the Advantage Data Dictionary file




Advantage Database Server 12  

7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened Advantage Error Guide error\_7074\_the\_table\_id\_stored\_in\_the\_adt\_table\_does\_not\_match\_the\_id\_stored\_in\_the\_advantage\_data\_dictionary\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened  Advantage Error Guide |  |  |  |  |

Problem: When opening a database table, the table ID stored in the .ADT table header does not match the corresponding table ID stored in the Advantage Data Dictionary. The cause of this error is likely the result of overwriting an existing .ADT table or overwriting an existing data dictionary file.

Solution: Avoid using the file system to overwrite an existing [database table](javascript:hhpopuplink.TextPopup(popid_174150351X,FontFace,-1,-1,-1,-1)) file or data dictionary file. Use the Advantage Client Engine API or the Advantage Data Dictionary Management Utility to copy a table and modify the data dictionary file. If a table file is inadvertently deleted without it being removed from the Advantage Data Dictionary first, it can be restored by using the table's [auto-creation](master_advantage_data_dictionary.htm) property. The Advantage Data Architect also has this functionality built into it and can be accessed in the table's properties.

Problem: When opening a database table, the table ID stored in the data dictionary of a DBF table does not match the table ID of the previously opened instance of the same DBF table. This error is the result of having same DBF table in two different data dictionaries.

Solution: Do not add same DBF table to two different data dictionaries.