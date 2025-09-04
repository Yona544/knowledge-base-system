---
title: Master Sp Testreplicationconnection
slug: master_sp_testreplicationconnection
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_testreplicationconnection.htm
source: Advantage CHM
tags:
  - master
checksum: 77f60eb6fbc09836e57a682b8687920c63ed24c6
---

# Master Sp Testreplicationconnection

sp\_TestReplicationConnection

sp\_TestReplicationConnection

Advantage SQL Engine

| sp\_TestReplicationConnection  Advantage SQL Engine |  |  |  |  |

Tests a subscriptions connection to the target database.

Syntax

sp\_TestReplicationConnection( Subscription, CiCharacter, 200; )

Parameters

| Subscription (I) | Subscription to test making a connection for |

Output

| ReturnCode (O) | Error code in the event of a failure. |
| ErrorMessage (O) | Error message in the event of a failure. |

Remarks

sp\_TestReplicationConnection can be used to test a subscription's ability to make a connection.

Example

EXECUTE PROCEDURE sp\_TestReplicationConnection( 'sub1' );

See Also

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.md)
