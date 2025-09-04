---
title: Master Sp Createpublication
slug: master_sp_createpublication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_createpublication.htm
source: Advantage CHM
tags:
  - master
checksum: 6223dd91c4f1fbf4ef06f0f15276012216567696
---

# Master Sp Createpublication

sp\_CreatePublication

sp\_CreatePublication

Advantage SQL Engine

| sp\_CreatePublication  Advantage SQL Engine |  |  |  |  |

Add a new publication to the data dictionary.

Syntax

sp\_CreatePublication(

PublicationName, CHARACTER, 200,

Comments, MEMO,

Options, INTEGER )

 

Parameters

| PublicationName (I) | The name of the publication to be created. |
| Comments (I) | Optional description of the publication. |
| Options (I) | This is reserved for future use. It should be 0. |

Remarks

sp\_CreatePublication creates a new publication object for holding replication articles. The publication itself is just a container object and has no specific properties associated with it. See [Replication](master_replication_overview.md) for more details.

Example

EXECUTE PROCEDURE sp\_CreatePublication( 'mypub', 'test publication', 0 );

// identify by all columns (ADS\_IDENTIFY\_BY\_ALL = 2)

EXECUTE PROCEDURE sp\_CreateArticle( 'mypub', 'table1', NULL, NULL, 2 );

EXECUTE PROCEDURE sp\_CreateSubscription( 'mysub', 'mypub',

'\\server\share\path\target.add', 'username', 'password',

'repqueue.adt', FALSE,

// ADS\_SUBSCR\_IGNORE\_FAILED\_REP +

// ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA = 12

'test subscription', 12 );

 

See Also

[system.publications](master_system_publications.md)

[sp\_ModifyPublicationProperty](master_sp_modifypublicationproperty.md)

[sp\_DropPublication](master_sp_droppublication.md)

[sp\_CreateArticle](master_sp_createarticle.md)

[sp\_CreateSubscription](master_sp_createsubscription.md)
