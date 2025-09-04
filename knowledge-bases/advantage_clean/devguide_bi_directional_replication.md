---
title: Devguide Bi Directional Replication
slug: devguide_bi_directional_replication
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_bi_directional_replication.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9f9a8d231c2d7565fd10b62c27a5f6da8c482c5f
---

# Devguide Bi Directional Replication

Bi-Directional Replication

     Bi-Directional Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Bi-Directional Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

With bi-directional replication, each source is also a target. Figure 10-3 depicts a simple bi-directional replication between two databases.

Figure 10-3: Bi-directional replication between two databases

Using Figure 10-3 for reference, when a record is changed in a replicated table on Database A, that change is replicated to Database B. In turn, a change made to a record in a replicated table on Database B will be replicated to Database A.

Unlike with unidirectional replication, where target databases are often readonly, databases in a bi-directional replication scenario are typically read/write databases. It is the bi-directional nature of the interaction that preserves the consistency between the databases participating in bi-directional replication.

If a record on Database B is changed, that change is replicated to Database A. Now, Database A and Database B both have the same values on that replicated record. If a change to that same record is now made to Database A, the change can successfully replicate to Database B, since the matching record will be found.

But it is in the bi-directional nature of this type of replication where some of the more complicated problems arise. Specifically, what if a record is changed on Database A, and that same corresponding record is changed on Database B before it receives the replication.

Such a scenario is indicative of the complexity of bi-directional replication. So long as the key fields in both records remain intact, it is possible that the change to the record in Database A overwrites the corresponding record in Database B, and that the concurrent change to the record in Database B overwrites the record in Database A. A situation like this emphasizes the differences between replication and synchronization.

But wait, you might say, what is the likelihood that the corresponding record is changed on both databases at the same time? The answer is that the changes might not happen simultaneously. They might happen hours apart, but during a period when replication is not occurring due to a loss of connection between the databases.

As is the case with unidirectional replication, bi-directional replication is not limited to just two databases. However, as the number of databases involved in bi-directional replication increases, the potential for conflicts increases as well.
