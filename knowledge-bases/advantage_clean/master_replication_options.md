---
title: Master Replication Options
slug: master_replication_options
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_replication_options.htm
source: Advantage CHM
tags:
  - master
checksum: 44827e7cf69c4365e874dc01fb57f9663e7b4fa7
---

# Master Replication Options

Replication Options

Replication Options

Advantage Concepts

| Replication Options  Advantage Concepts |  |  |  |  |

This section describes the options that are used when creating publications and subscriptions and what some of the tradeoffs might be.

Publication Options

Once a publication is created in Advantage Data Architect, it is possible to make further changes to it such as adding or removing tables or setting filters on tables.

Identification Columns

When defining an article in a publication, you have the option of using the primary key as the identification column(s), using all searchable columns, or you can choose any desired subset of columns. The goal is to be able to uniquely identify the record in the target table using the identification columns. At a minimum, you should include the primary key for the table; otherwise, it might be possible for an update to affect multiple records at the target. To reduce the possibility of updating the wrong record at the target, you can include all searchable fields as the identification columns. The potential drawback to this method is that it can be more costly. It requires that more information be sent over the network and the update at the target may be more expensive because of the additional search fields.

Note If the identification columns do not uniquely identify the target record, then multiple records may be updated. An error will be logged, but the update will not be undone unless transactions are used at the source.

Article Filter

A filter that can be associated with an article (table) defines whether or not a given updated record is to be replicated. It is sometimes referred to as a horizontal filter. If no filter is specified, all updated records are replicated. The filter should be a logical expression. If it evaluates to TRUE for a given record, then the record will be replicated. For updated records, the filter is evaluated against the original record data. See the topic titled [Advantage Expression Engine](master_advantage_expression_engine.md) for information about expression syntax.

In general, it is probably a good idea to filter on some unchanging portion of the record (e.g., the primary key or a static site code). If a filter uses a portion of the data that changes, then a given record may be replicated in response to one update but not the next.

Vertical Filter

A vertical filter can be defined for each publication article to specify which columns of the table should be replicated. If no vertical filter is defined, all columns in the table will be replicated. These filters are useful if the target table has a subset of the columns of the source table, or if there is certain data, such as a large BLOB field, that you do not want to replicate. A vertical filter can be specified as a list of columns to be included or excluded from replication. An exclusion list will allow any new columns to be added to the table in the future to be replicated, while an inclusion list would prevent new columns from being replicated unless you specifically add the new columns to the vertical filter. Note that if a table has a vertical filter, fields not in the filter (either explicitly excluded or not explicitly included) will not be used as part of the identification columns. So, for example, if you are using the primary key as the identification column(s), then you should include the column(s) of the primary key in the vertical filter.

Note Conflict detection is not currently possible when using a vertical filter. The detection scheme is based on a CRC of the record. If the source and target table structures are not identical, the CRC values will always be different, which means that the conflict trigger will always fire even if the original replicated fields matched at the source and target.

UPDATE and INSERT MERGE

The SQL MERGE statement provides additional functionality to INSERT or UPDATE operations. A MERGE statement merges the records of one record set with another by updating existing records and inserting others. By enabling the MERGE UPDATE article option, if a record being updated is not found at the target, it is then inserted instead of returning an error. Likewise with the MERGE INSERT article option enabled, if a record being inserted already exists at the target, it will be updated rather than returning an error. MERGE uses the identification columns of the article to determine if the target record exists prior to the INSERT or UPDATE operation. These options are both disabled by default. Note that MERGE replication updates are expected to update or insert only one record at the target just like normal INSERT or UPDATE replication updates.

Subscription Options

Target Database Path

This is the full path to the target data dictionary. Typically, this should be a UNC path that includes the target server name (or IP address and port), share, and path. A drive letter path, for example, would probably not be valid because the connection to the target is made by Advantage Database Server running at the source. It is probable that the drive letter would not be meaningful in that situation.

The target must be to a valid Advantage Data Dictionary. For security reasons, Advantage will not replicate to a free connection.

Target Database Username and Password

When Advantage Database Server connects to the target database for replication, it will use this username and password for authentication. It must be a valid username at the target database and should have sufficient rights and privileges to update the replicated tables at the target.

The replication user must have INSERT, UPDATE, and DELETE permissions in order to make the necessary updates (assuming that all of those operations can occur at the source). In addition, the replication user must have SELECT (READ) permissions on the identification columns in order to be able to locate the record that is to be updated.

Source Queue Path

This is the replication queue. It is the file in which the replication updates are queued prior to being sent to the target database. It must be a valid ADT file name. If no path is specified, it will be created in the same directory as the data dictionary. Advantage creates this table with administrator privileges as a data dictionary-bound table. If table encryption is enabled and the "Encrypt New Tables" option is selected, this table will be encrypted when Advantage creates it. It is also possible to encrypt the table by right-clicking on it in the Connection Repository and choosing Encrypt.

Static Queue Path

If this option is selected, the path for the replication queue will be stored as given. Otherwise, the path will be converted and stored as a path relative to the data dictionary.

Disable Subscription

If this option is selected, subsequent record updates will not be stored in the replication queue. Note that if the queue still has existing record updates, they will continue to be processed and sent to the target database.

Target Connection Type

The connection to the target database must be to Advantage Database Server (Advantage Local Server is not supported). The connection can either be an "Internet" (AIS) connection or a regular LAN connection.

Ignore Replication Failures

This option controls whether or not Advantage will retry failed replication updates. If an update to the target fails to update the expected number of records and this option is selected, the update will still be removed from the queue. If the ignore option is not selected, the update will not be removed from the queue; it will be attempted again at a later point. Because the updates are processed in order, no other updates will be processed until the failed update succeeds or is removed from the queue by the administrator.

By default, the only replication failures that are controlled by this option are updates where the updated record count is unexpected (error 7137). Other types of errors, such as a failure to find the table at the target, are not ignored. However, it is possible to modify this behavior with the [PERMITTED\_REP\_ERRORS](master_permitted_rep_errors.md) server configuration parameter. Using this configuration option, you can control which specific errors are ignored during replication.

Log Data for Failed Replication Updates

When replication errors are logged, the SQL statement that was attempted is logged as part of the information. If this option is selected, field data will be logged with the SQL statement. For security reasons, this option is off by default.

Forward Replicated Updates

This option controls whether Advantage will forward replication updates to subsequent target databases. It is useful for setting up a chain of replication servers. For example, if A replicates to B and B replicates to C, then the forwarding option at B will control if the updates from A are passed on to C.

If you have two servers that are replicating to each other (two-way replication), it is not necessary to turn on this option. If it is turned on in this situation, each server will echo the replication updates back to the original source and either be ignored, or result in replication failures.

Pause Subscription

If this option is selected, record updates stored in the replication queue are not sent to the target server. Rather, the updates are stored in the queue until the subscription is un-paused at which point the queue entries are processed and sent to the target server.

See Also

[Replication Overview](master_replication_overview.md)
