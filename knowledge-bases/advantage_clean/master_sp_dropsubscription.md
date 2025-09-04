---
title: Master Sp Dropsubscription
slug: master_sp_dropsubscription
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_dropsubscription.htm
source: Advantage CHM
tags:
  - master
checksum: a9c11ce398a90fffd70701c0981cf5304b1fd25d
---

# Master Sp Dropsubscription

sp\_DropSubscription

sp\_DropSubscription

Advantage SQL Engine

| sp\_DropSubscription  Advantage SQL Engine |  |  |  |  |

Delete a subscription object from the database.

Syntax

sp\_DropSubscription(SubscriptionName,CHARACTER,200 )

 

Parameters

| SubscriptionName (I) | Name of the subscription object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The subscription specified by SubscriptionName cannot be located in the data dictionary. |

Remarks

sp\_DropSubscription removes an existing subscription from the database.

Example

EXECUTE PROCEDURE sp\_DropSubscription( 'mysub' )

 

See Also

[sp\_CreateSubscription](master_sp_createsubscription.md)
