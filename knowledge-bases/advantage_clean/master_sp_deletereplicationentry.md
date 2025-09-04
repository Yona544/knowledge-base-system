---
title: Master Sp Deletereplicationentry
slug: master_sp_deletereplicationentry
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_deletereplicationentry.htm
source: Advantage CHM
tags:
  - master
checksum: f9defea8aef1b0b72199ecafa823de4b324922b1
---

# Master Sp Deletereplicationentry

sp\_DeleteReplicationEntry

sp\_DeleteReplicationEntry

Advantage SQL Engine

| sp\_DeleteReplicationEntry  Advantage SQL Engine |  |  |  |  |

Delete's a replication entry from queue.

Syntax

sp\_DeleteReplicationEntry(

      Subscription, CiCharacter, 200;

      EntryID,INTEGER; )

Parameters

| Subscription (I) | Subscription to delete entry from |
| EntryID (I) | ID of the replication queue entry to delete. |

Remarks

sp\_DeleteReplicationEntry will safely delete a replication entry making sure to remove all entries in a transaction.  The subscription must be paused before an entry can be deleted.

To delete a replication entry, the user must be logged in as the administrative user, ADSSYS or be a member of the DB:Admin group.

Example

EXECUTE PROCEDURE sp\_DeleteReplicationEntry( 'sub1', 42 );

See Also

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.md)
