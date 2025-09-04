---
title: Devguide Creating The Subscription
slug: devguide_creating_the_subscription
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_the_subscription.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6ff76f66c13114044ed1a37e0274a78b1bd1fe66
---

# Devguide Creating The Subscription

Creating the Subscription

     Creating the Subscription

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating the Subscription  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While a publication defines the tables that will be replicated (and also which fields and records), a subscription defines which data dictionary the replicated data will be forwarded to.

You create a subscription by right-clicking the SUBSCRIPIONS node from your active Administrative connection in the Connection Repository and selecting Create. The Advantage Data Architect responds by displaying the Subscription dialog box, shown in Figure 10-11.

Figure 10-11: The Subscription dialog box

From the General page of the Subscription dialog box, you provide a name for the publication. If your data dictionary is going to replicate to only one database, you can set the name of your subscription to the same name as your connection. If you are replicating to multiple databases, set the name to something meaningful.

You then use the Publication dropdown menu to select which publication this subscription is associated with. Remember that each subscription can be associated with only one publication, but the same publication can be used by multiple subscriptions.

You use the Target Database section of the General page of the Subscription dialog box to specify to which data dictionary you want to replicate. In Path, enter the location of your target data dictionary. This value will often be a UNC (universal naming convention) reference to the server and target data dictionary, though it can also make use of server-side aliases. (A directory path can also be provided if the data dictionary is on the same machine as your replicating data dictionary, but that is an unusual arrangement.)

You also must provide a user name and password (if required) that will be used to connect to the target data dictionary. At a minimum, this user name must have sufficient rights to insert, update, and delete records from all target tables involved in the replication.

The Disable Subscription option is initially disabled when you are creating the subscription. Once you create the subscription and save it, you can temporarily disable the subscription by right-clicking the subscription, selecting Properties from the displayed context menu, and then checking the Disable Subscription checkbox.

You use the Advanced page of the Subscription dialog box, shown in Figure 10-12, to customize how the subscription is implemented.

Figure 10-12: The Advanced page of the Subscription dialog box

Use the Queue Table field to select the name of the replication queue, the table that will hold replications while they await forwarding. The default name of this table is the name of the subscription. If you do not include a path for this table, the queue table will be stored in the same directory as the data dictionary.

Use Target Connection Type options to define how you are connecting to the target data dictionary server. Select Advantage Remote Server to connect to a data dictionary on your local area network (LAN) or virtual private network (VPN), or select Advantage Internet Server to connect to a data dictionary over the Internet.

   
NOTE: In order to replicate to a data dictionary over the Internet, the target data dictionary must be configured to allow Internet connections. Configuring a data dictionary for Internet connectivity is described in Chapter 4.  
 

If you place a check next to Ignore Replication Failures, a replication queue table record that fails to update the expected number of records (one) is removed from the queue table. If this checkbox is unchecked, a failed replication that updates an unexpected number of records will remain in the queue until the record is successfully applied. Since queue table records are processed in the order in which they appear in the queue table, if the failed record cannot be successfully replicated, no other records will be replicated until an administrator deletes the failed record.

You can configure Advantage to ignore additional types of errors. Configuring Advantage to ignore additional errors is described later in this chapter.

When a record fails to replicate, an error is written to the ads\_err.adt table on the source server (in previous versions of ADS, this table was named ads\_err.dbf). If the Log Data for Failed Replication Updates option is checked, the actual SQL statement that failed to execute on the target is included in the error record. Since this information may contain sensitive data, this option is un-checked by default.

Finally, use the Forward Replicated Records option to control what the source data dictionary should do with records that it receives through replication. If you want the source data dictionary to forward records it receives through replication onto the target of this subscription, check the Forward Replicated Records option. Leave this option unchecked if you do not want to forward records received through replication.
