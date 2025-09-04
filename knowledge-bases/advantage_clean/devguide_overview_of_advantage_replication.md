---
title: Devguide Overview Of Advantage Replication
slug: devguide_overview_of_advantage_replication
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_overview_of_advantage_replication.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3d82d6b8017daeff0131f46e33624057595a1e71
---

# Devguide Overview Of Advantage Replication

Overview of Advantage Replication

 

     Overview of Advantage Replication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Overview of Advantage Replication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage uses a push model of replication. In a push model, the source data dictionary is responsible for implementing the replication. Specifically, the source data dictionary knows which data to replicate, and to which data dictionary this data will be replicated.

When a record is inserted to, updated in, or deleted from one of the tables involved in replication on the source database, information about that record is added to a special table on the source data dictionary called the replication queue. This information includes the record that was involved in the operation, as well as a CRC (cyclic redundancy check), an integer value produced by a calculation on all fields in that record. How the CRC is used is discussed later in this section.

When a record arrives in the replication queue, an ADS thread attempts to apply the change to the corresponding table in the target data dictionary. If the change cannot be applied, a replication error results. How these errors are handled is discussed later in this chapter.

You should note that replication is not the same as synchronization. Synchronization attempts to keep two databases identical. Depending on how you configure your replication, your source and target databases might actually remain identical, but replication by itself cannot assure this.

For example, if the source database and the target database start out as identical copies of one and other, and the target database is a readonly database (meaning that no changes other than through replication will ever be applied to it), there is a high likelihood that the two databases will remain more or less identical. The databases will become out of sync if the connection between them is lost, but they should become identical once again shortly after the connection is restored.

However, even when the target is readonly, if the two databases do not start out identical, the odds are against them ever becoming identical through replication.

Replication is also not a substitute for backing up your data. While replication can copy records from one database to another, replication is unaware of the structure, or metadata, or your database. Replication is also unaware of changes to data dictionary objects that you might use, such as RI definitions, SQL stored procedures, or SQL triggers. If your intent is to back up your database, you need to use ADS's backup functionality.

While the discussion so far has focused on replication between two data dictionaries, in reality replication may involve more than two databases. Furthermore, when you are replicating two or more databases, you have a number of different strategies that you can employ. The basic replication strategies are discussed in the following section.
