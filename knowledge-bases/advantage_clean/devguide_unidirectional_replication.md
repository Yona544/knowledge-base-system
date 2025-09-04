---
title: Devguide Unidirectional Replication
slug: devguide_unidirectional_replication
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_unidirectional_replication.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 0ab507954856407cf33622a09ee0c5b72861f127
---

# Devguide Unidirectional Replication

Unidirectional Replication

     Unidirectional Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Unidirectional Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

With unidirectional replication, changes applied to one or more tables of one database are replicated to corresponding tables of another database. Figure 10-1 depicts a simple version of unidirectional replication, in which records from Database A are replicated to Database B.

Figure 10-1: Unidirectional replication between two databases

Unidirectional replication is often used in scenarios where changes are never or rarely applied to the target database. For example, you might use unidirectional replication to create an offsite copy of your database records. This copy could then be used to restore your data if there were a catastrophic failure of the original database. (Note that this is different from a backup.)

Another situation where unidirectional replication is useful is when you want to maintain a server exclusively for generating reports against large amounts of data. By replicating from the live data to a reporting database, the large queries against the reporting database have little impact on the performance in the live data.

Unidirectional replication does not assume that only two databases are involved. Figure 10-2 represents a reasonable unidirectional replication between three databases.

Figure 10-2: Unidirectional replication can include two or more databases

When unidirectional replication involves more than two databases, middle databases that receive data from a source in turn replicate that data on to a new target. This chain of replications assures that changes made at the original source will make their way to a final target database.

Here is a scenario that includes unidirectional replication between more than two databases. Imagine that you have a national chain of auto parts stores. An individual store may replicate its data to a regional office. The regional database, in turn, may replicate data it receives on to the national headquarters. With this example of unidirectional replication, the replicated data would typically be treated as readonly, and be used to generate reports and graphs depicting the performance and trends at the individual stores (from the regional database) and in regions (from the corporate database).
