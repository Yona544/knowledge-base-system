---
title: Ace Adsdddeletesubscription
slug: ace_adsdddeletesubscription
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdddeletesubscription.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d4c6dc53a543a9550881603214a740512f276a55
---

# Ace Adsdddeletesubscription

AdsDDDeleteSubscription

AdsDDDeleteSubscription

Advantage Client Engine

| AdsDDDeleteSubscription  Advantage Client Engine |  |  |  |  |

Delete a subscription object from the database.

Syntax

UNSIGNED32 AdsDDDeleteSubscription( ADSHANDLE hDictionary,

UNSIGNED8 \*pucSubscriptionName );

 

Parameters

| hDictionary (I) | Handle of a database connection. |
| pucSubscriptionName (I) | Name of the subscription object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The subscription specified by pucSubscriptionName cannot be located in the data dictionary. |

Remarks

AdsDDDeleteSubscription removes an existing subscription from the database.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDDeleteSubscription( hConn, "mysub" );

 

See Also

[AdsDDCreateSubscription](ace_adsddcreatesubscription.md)
