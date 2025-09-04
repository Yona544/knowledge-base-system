Creating the Sample Table




Advantage Database Server 12  

     Creating the Sample Table

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating the Sample Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating the Sample Table Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_the\_Sample\_Table Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Creating the Sample Table / Dear Support Staff, |  |
| Creating the Sample Table  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The three examples of compiled triggers all performed the same task. Specifically, when a record is being inserted into a table to which the trigger is assigned as an INSTEAD OF INSERT trigger, the trigger tests whether or not the first field of the table is null. If so, it assigns a GUID to this field. Of course, this trigger assumes that the first field is a character field large enough to handle a GUID, which is 38 characters in length (36 if you strip off the open and close curly braces that Delphi's GUID generator adds).

You may be wondering why the trigger checks for a null field, instead of simply writing a GUID to the first field unconditionally. The reason is simple. If the table to which the trigger is attached is a parent table of a parent-child relationship, the key field for the parent table must be assigned by your client application. Specifically, your client code must assign a GUID to the first field of the parent table prior to posting (which triggers the INSTEAD OF INSERT trigger) in order to assure that the child records, which are associated with the parent through a foreign key (which is also a GUID), maintain their association with the parent record.

This trigger is especially useful. It ensures that every record contains a unique key, one that will never conflict with any other key. By using the unique GUID key, you avoid the problems associated with auto-increment fields. On the other hand, a GUID is a substantially larger data value than an auto-increment field (36 or 38 bytes versus 4 bytes). Fortunately, disk space is abundant these days, and the guaranteed uniqueness of a GUID key is usually worth the additional storage.

Use the following steps to create a simple table to which your compiled trigger will be assigned:

1.        With the DemoDictionary connected and active in the Connection Repository, right-click the TABLES node and select Create.

|  |  |
| --- | --- |
| 2. | In the Table Designer, leave Table Type set to Advantage (ADT). |

|  |  |
| --- | --- |
| 3. | Create four fields in the new table using the information provided in Table 8-1. |

|  |  |
| --- | --- |
| 4. | When you are through adding fields, select OK to close the Table Designer and create the new table. |

|  |  |
| --- | --- |
| 5. | When prompted for a table name, enter TriggerTest.ADT, and place the table in the same directory as your DemoDictionary data dictionary. |

|  |  |
| --- | --- |
| 6. | When the Advantage Data Architect asks you if you want to open the new table, select No. |

 

|  |  |  |
| --- | --- | --- |
| Field Name | Data Type | Size |
| Key | character | 40 |
| Name | cicharacter | 35 |
| Number | integer |  |
| Last Changed | modtime |  |

Table 8-1: The Structure for the TriggerTest Table