---
title: Ace Adsdddeletepublication
slug: ace_adsdddeletepublication
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdddeletepublication.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 93f05bf9afa4df6ee36dbc7edfc8a7aa366658fb
---

# Ace Adsdddeletepublication

AdsDDDeletePublication

AdsDDDeletePublication

Advantage Client Engine

| AdsDDDeletePublication  Advantage Client Engine |  |  |  |  |

Delete a publication object from the database.

Syntax

UNSIGNED32 AdsDDDeletePublication( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName );

 

Parameters

| hDictionary (I) | Handle of a database connection. |
| pucPublicationName (I) | Name of the publication object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The publication specified by pucPublicationName cannot be located in the data dictionary, or the publication is in use by one or more subscriptions. |

Remarks

AdsDDDeletePublication removes an existing publication from the database.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDDeletePublication( hConn, "mypub" );

 

See Also

[AdsDDCreatePublication](ace_adsddcreatepublication.md)

[AdsDDSetSubscriptionProperty](ace_adsddsetsubscriptionproperty.md)

[AdsDDDeleteSubscription](ace_adsdddeletesubscription.md)
