Implementing Replication




Advantage Database Server 12  

     Implementing Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Implementing Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Implementing Replication Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Implementing\_Replication Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Implementing Replication / Dear Support Staff, |  |
| Implementing Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Replication is the process of moving changes made to one database to another, similar database. For example, imagine that two different databases contain a Customer table, and that these tables contain identical records for the most part. With replication, changes made to a particular customer record on one database, referred to as the source database, are transferred to the other database, the target database.

There are a number of requirements that must be met before you can implement replication. First of all, replication requires that the source database and the target database both use data dictionaries.

Second, both the source data dictionary and the target data dictionary must be accessed by the Advantage Database Server. Replication cannot be implemented using Advantage Local Server.

Finally, an additional replication license must be installed on the source serverand sometimes the target server as well, depending on how you configure your replication. This license is available from your Advantage representative, and is significantly less expensive than your ADS license.

Replication was added in Advantage Database Server 8.