Configuring Replication




Advantage Database Server 12  

 

     Configuring Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Configuring Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Configuring Replication Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Configuring\_Replication Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Configuring Replication / Dear Support Staff, |  |
| Configuring Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As mentioned at the beginning of this chapter, Advantage replication is a push technology. Specifically, replication is always the responsibility of the source data dictionary.

You configure replication from a data dictionary using three objects: publications, articles, and subscriptions. A data dictionary that replicates must have at least one publication. A publication defines which articles (tables and their fields) are to be replicated, and which fields of those tables will be used to locate their corresponding records at the target database.

A subscription specifies the target data dictionary for replication. It also controls how failures are handled, and whether or not this subscription should forward records to the target that this data dictionary receives through replication.

A given subscription must be associated with exactly one publication. To put this another way, the subscription defines who to send the data to and how to send it, and the publication defines what data to send.

In some cases, a single data dictionary may have more than one subscription. For example, the hub of a hub and spoke strategy will have one subscription for each spoke.

Whether a replicating data dictionary has more than one publication depends on your replication design. If a hub data dictionary needs to send all data to all spokes, without filtering, all of a hub's subscriptions may refer to a single publication. On the other hand, if each spoke must receive data specific to only that spoke, your hub data dictionary will have one publication (and its corresponding subscription) for each spoke.

There are three steps to implementing replication. These are:

Creating one or more publications.

Configuring your one or more publications. In some cases, this step is unnecessary.

Creating one or more subscriptions.

These steps are described in the following sections.