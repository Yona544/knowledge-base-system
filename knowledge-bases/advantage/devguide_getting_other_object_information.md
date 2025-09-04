Getting Other Object Information




Advantage Database Server 12  

     Getting Other Object Information

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Getting Other Object Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Getting Other Object Information Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Getting\_Other\_Object\_Information Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > Getting Other Object Information / Dear Support Staff, |  |
| Getting Other Object Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are nine additional system tables that you use to retrieve information about data dictionary objects. The system.relations table can be queried from the administrative account or from user accounts where the user has ALTER permissions on both tables involved in a referential integrity relationship. From other accounts, this table will return an empty result set.

The system.articles, system.functions, system.links, system.packages, system.publications, system.publicationarticles, system.storedprocedures, system.subscriptions, and system.views tables can be accessed using either the administrative account or a user account. From a user account, the contents of these tables will be based on the specific rights the user has to the associated objects. Records will appear only for objects the user has rights to, and some columns may be NULL, depending on the specific permissions that user has to those objects.

You use system.relations to return one record for each referential integrity relationship defined in your data dictionary. Columns returned in this result set include RI name, parent table, child table, parent table primary index order name, child table foreign key index order name, update rule, delete rule, and related error messages. The update and delete rule values are integers. The values for these fields are listed in Table 14-8.

 

|  |  |
| --- | --- |
| Type | Value |
| ADS\_DD\_RI\_CASCADE | 1 |
| ADS\_DD\_RI\_RESTRICT | 2 |
| ADS\_DD\_RI\_SETNULL | 3 |
| ADS\_DD\_RI\_SETDEFAULT | 4 |

Table 14-8: Update and Delete Rule Codes

You use the system.functions table to retrieve one record for each function defined in the data dictionary. Data returned in this result set includes the function name, input parameters, and function result data type.

You use the system.links table to retrieve one record for each available data dictionary link. Data returned in this result set includes the link name, path to the linked dictionary, link options, and user name associated with the link. Link options are represented by an integer value. The value that appears in the system.links table is the sum of the link options listed in Table 14-9.

 

|  |  |
| --- | --- |
| Type | Value |
| ADS\_LINK\_GLOBAL | 1 |
| ADS\_LINK\_AUTH\_ACTIVE\_USER | 2 |
| ADS\_LINK\_PATH\_IS\_STATIC | 4 |

Table 14-9: Data Dictionary Link Option Codes