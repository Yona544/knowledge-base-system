---
title: Master Sp Droppublication
slug: master_sp_droppublication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_droppublication.htm
source: Advantage CHM
tags:
  - master
checksum: c3c91274e7872ac5d86f9730ba1e45452af184c1
---

# Master Sp Droppublication

sp\_DropPublication

sp\_DropPublication

Advantage SQL Engine

| sp\_DropPublication  Advantage SQL Engine |  |  |  |  |

Delete a publication object from the database.

Syntax

sp\_DropPublication( PublicationName,CHARACTER,200 )

Parameters

| PublicationName (I) | Name of the publication object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary, or the publication is in use by one or more subscriptions. |

Remarks

AdsDDDeletePublication removes an existing publication from the database.

Example

EXECUTE PROCEDURE sp\_DropPublication( 'mypub' )

 

See Also

[sp\_CreatePublication](master_sp_createpublication.md)

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.md)

[sp\_DropSubscription](master_sp_dropsubscription.md)
