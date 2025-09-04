Hub and Spoke Replication




Advantage Database Server 12  

     Hub and Spoke Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Hub and Spoke Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Hub and Spoke Replication Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Hub\_and\_Spoke\_Replication Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Hub and Spoke Replication / Dear Support Staff, |  |
| Hub and Spoke Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Hub and spoke replication is a more complex example of bi-directional replication. Hub and spoke replication is similar to the auto parts chain example given earlier in the unidirectional section of this chapter, except that the regional and corporate databases are not readonly.

In a typical hub and spoke scenario, two or more satellite offices (stores, for example) replicate their data to a central database (the regional office). In addition, changes made to data at the regional office will be replicated to the individual stores.

This replication at the regional office is often filtered. Specifically, when a record is changed at the regional office, and that record only applies to one of the stores, that record is replicated only to the associated store. For records that apply to all stores, changes to those records are replicated to all stores. Figure 10-4 depicts a simple hub and spoke replication.

Figure 10-4: A simple hub and spoke replication

Hub and spoke replication scenarios contain many of the complexities present in bi-directional replication. The most significant of which is the possibility that conflicting changes can be made to the various databases.

Fortunately, in the typical hub and spoke replication implementation, there are relatively strict operational procedures for changing data. For example, sales data that is replicated from a store simply should not be changed at headquarters (this rule could be enforced through the client application used to work with the data at headquarters). Similarly, only headquarters can change an employee record, and that change will be replicated only to the store where the employee is assigned.