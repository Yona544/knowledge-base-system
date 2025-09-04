Getting Dictionary Information




Advantage Database Server 12  

     Getting Dictionary Information

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Getting Dictionary Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Getting Dictionary Information Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Getting\_Dictionary\_Information Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > Getting Dictionary Information / Dear Support Staff, |  |
| Getting Dictionary Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You retrieve the properties of your data dictionary using the system.dictionary table. This table has one record, which contains one field for each property of the data dictionary to which you are connected. The following is how a query of this system table looks:

SELECT \* FROM system.dictionary

If you are connected to the data dictionary using the administrator's account (or a user with ALTER database privileges), every column in this record is populated with the associated property value. If you are connected on any other account, only the Version\_major and Version\_minor columns of this table are populated--all other columns contain NULL values.

Full text search defaults are also a data dictionary property. To list the full text search defaults for your data dictionary, query system.fts. This table returns one record.