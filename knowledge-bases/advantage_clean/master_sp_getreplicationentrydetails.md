---
title: Master Sp Getreplicationentrydetails
slug: master_sp_getreplicationentrydetails
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getreplicationentrydetails.htm
source: Advantage CHM
tags:
  - master
checksum: b3d6bc6d501eb19daf0555d6e7f26faedc32cda8
---

# Master Sp Getreplicationentrydetails

sp\_GetReplicationEntryDetails

sp\_GetReplicationEntryDetails

Advantage SQL Engine

| sp\_GetReplicationEntryDetails  Advantage SQL Engine |  |  |  |  |

Retrieves extra information from a replication entry.

Syntax

sp\_GetReplicationEntryDetails(

      Subscription, CiCharacter, 200;

      EntryID,INTEGER;

      UseParamsForIdentifiers,Logical;

      UseParamsForValues,Logical )

Parameters

| Subscription (I) | Subscription to get entry details for |
| EntryID (I) | ID from the replication queue to retrieve extra details |
| UseParamsForIdentifiers(I) | When true SQL statements are generated with parameters instead of values for identifiers |
| UseParamsForValues (I) | When true SQL statements are generated with parameters instead of values for values. |

Output

| EntryID (O) | Replication entry ID for the details being returned. |
| ValuesTempTableName (O) | Name of a temporary table containing the replication values for the queue entry. |
| IdentityTempTableName (O) | Name of a temporary table containing the identification values of the queue entry. |
| SourceSelectStmt (O) | SQL SELECT statement that can be used to retrieve the source record for a table. |
| TargetSelectStmt (O) | SQL SELECT statement that can be used to retrieve the destination record for a table. |
| InsertStmt (O) | SQL INSERT statement that can be used to append a record to the destination table with the values from the entry. |
| UpdateStmt(O) | SQL UPDATE statement that can be used to update a record in the destination table with the values from the entry. |
| DeleteStmt (O) | SQL DELETE statement that can be used to delete a record in the destination table. |
| MergeStmt (O) | SQL MERGE statement that can be used to merge a record in the destination table. |

Remarks

sp\_GetReplicationEntryDetails can be used to retrieve extra information from a replication table entry.  The subscription must be paused before extra information about an entry can be determined.  The stored procedure should be executed on a connection to the source server.  A second connection to the destination server will be needed to resolve any problems.  The stored procedure will create two temporary tables on the source connection and returns their names.  If the necessary information is available a record will be added to the table with the values from that field.  Up to 6 SQL statements will also be added to the table depending on the information available.

The first table contains the values to be inserted in the destination table.  This table will not be populated if the replication operation is a delete.

The second table contains the values used to identify a row in the destination table.  These values may also be used to identify a row in the source table if the identity fields have not changed.  This  table table will not be populated if the operation is an insert.

To retrieve replication entry information, the user must be logged in as the administrative user, ADSSYS or be a member of the DB:Admin group.

When deal

Example

EXECUTE PROCEDURE sp\_GetReplicationEntryDetails( 'sub1', 42, FALSE, FALSE );

See Also

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.md)
