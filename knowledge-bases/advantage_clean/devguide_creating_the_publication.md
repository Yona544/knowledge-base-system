---
title: Devguide Creating The Publication
slug: devguide_creating_the_publication
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_the_publication.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 32cdaff88e9c856e2e4be7a5ab25be4fcb6fe3e0
---

# Devguide Creating The Publication

Creating the Publication

     Creating the Publication

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating the Publication  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you have already learned, a publication defines which articles are replicated (tables, and sometimes which records and fields that participate in a replication). Note that currently in ADS, all articles are tables, but in the future, other objects might be articles as well. In order to implement replication, your data dictionary must have at least one publication.

You create a publication using the Advantage Publication Wizard. You access this wizard by right-clicking the PUBLICATIONS node from your active administrative connection in the Connection Repository. The Select Row Identification Method page of the Advantage Publication Wizard is shown in Figure 10-5.

Figure 10-5: The Select Row Identification Method page of the Advantage Publication Wizard

In order to replicate updates and deletions, it is necessary for the source server to know how to identify the corresponding records on the target database.

In most cases, target record identity is provided by one or more fields whose values represent the uniqueness of each record, and whose values rarely if ever change. Such a key is often referred to as a primary key.

When you are designing your indexes, Advantage permits you to specifically designate one of your indexes as the primary index. If you define primary indexes, set the Select Row Identification Method to Primary Key. The publication will then use the primary index designation to identify the fields that uniquely identify records between the source and destination databases. For those tables that do not have a defined primary index, this option will automatically select all fields.

If there are no primary indexes on any fields, or if any of your primary indexes are not sufficient to uniquely identify the corresponding record on the target database, select the All Columns radio button.

There are three reasons why most developers will select Primary Key to define the row identification method. First, the use of primary keys reduces the amount of data that has to be transferred between the source and target. Second, all columns will be used by default for tables that do no have primary keys. Third, you can always manually adjust which fields are used to identify destination rows at a later time.

Click Next to advance to the Select Tables to Publish page of the Advantage Publication Wizard, shown in Figure 10-6.

Figure 10-6: The Select Tables to Publish page of the Advantage Publication Wizard

You use this page of the Wizard to identify which tables (articles) of your data dictionary you want to replicate. If there are some tables that you do not want to replicate, uncheck the checkbox next to those table names. For example, you probably would not want to publish the TriggerTest table shown in Figure 10-6.

When you are through customizing which tables to publish, click Next to continue to the Enter Publication Name and Description page of the Advantage Publication Wizard shown in Figure 10-7.

Figure 10-7: The Enter Publication Name and Description page of the Advantage Publication Wizard

You use this page to define a name for your publication, and a description if you like. If your data dictionary is going to have only one publication (regardless of how many subscriptions you will have), you can leave the publication set to the default, which is the same as your Administrative connection name. If you anticipate having more than one publication, you should rename this publication, using a name that best describes the data that you are publishing.

When you are done, click Next to move to the Complete Publication page of the Advantage Publication Wizard shown in Figure 10-8.

The Complete Publication page permits you to review what operations the Advantage Publication Wizard will perform. If you have many tables, you can use the scroll bar on the right side of this page to scroll in order to view the remaining details.

If you discover you want to change something as you examine this information, you can click Previous to return to one of the earlier pages in this Wizard. (Alternatively, you can make this adjustment by changing the publication's properties at a later time, as described in the following section). Once you are done examining this information, click Finish.

Figure 10-8: The Complete Publication page of the Advantage Publication Wizard

After you click Finish, the Advantage Publication Wizard will display a progress dialog box that includes a progress bar and a running output of the articles it is creating in the publication. When this process is complete, the OK button becomes enabled. Click OK to close the progress dialog box. This also closes the Advantage Publication Wizard.
