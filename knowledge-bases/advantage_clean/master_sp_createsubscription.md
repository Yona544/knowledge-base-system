---
title: Master Sp Createsubscription
slug: master_sp_createsubscription
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_createsubscription.htm
source: Advantage CHM
tags:
  - master
checksum: 8c4a1c093ecb4aea0186af09bcf9eb275c35f767
---

# Master Sp Createsubscription

sp\_CreateSubscription

sp\_CreateSubscription

Advantage SQL Engine

| sp\_CreateSubscription  Advantage SQL Engine |  |  |  |  |

Add a new subscription to the data dictionary.

Syntax

sp\_CreateSubscription(

SubscriptionName,CHARACTER,200,

PublicationName,CHARACTER,200,

Target,CHARACTER,260,

UserName,CHARACTER,50,

Password,CHARACTER,20,

ReplicationQueue,CHARACTER,260,

Forward,LOGICAL,

Comments,MEMO,

Options,Integer )

 

sp\_CreateSubscription(

SubscriptionName,CHARACTER,200,

PublicationName,CHARACTER,200,

Target,CHARACTER,260,

UserName,CHARACTER,50,

Password,CHARACTER,20,

ReplicationQueue,CHARACTER,260,

ConnectionString,MEMO,

Forward,LOGICAL,

Comments,MEMO,

Options,Integer )

 

Parameters

| SubscriptionName (I) | The name of the subscription to be created. |
| PublicationName (I) | The name of an existing publication object. The articles (tables) in this publication will be replicated according to the subscription definition. |
| Target (I) | The full connection path to the target database; the path must include the target data dictionary name. This is where the data will be replicated to. Generally, this should be a UNC style path. |
| UserName (I) | This is the user name to use when Advantage Database Server connects to the target database (specified by Target) to perform replication updates. This is sometimes referred to as the replication user. This user must exist in the data dictionary identified by Target. |
| Password (I) | The password associated with UserName. |
| ReplicationQueue (I) | The name of the replication queue that stores pending replication updates. This must be a valid table name. If no path is provided, the table will be located in the same directory as the data dictionary. |
| ConnectionString (I) | Specifies a connection string to use for connecting to the target. This can be used to supplement the other connection-related properties. This property was added primarily so that [Transport Layer Security](master_communications_encryption.md) options could be specified. Refer to [AdsConnect101](ace_adsconnect101.md) for information on valid connection string properties. |
| Forward (I) | This flag (TRUE/FALSE) determines if replication updates are forwarded from this data dictionary. If this flag is TRUE and an update is made to a table through replication (as opposed to a direct client update), the update will be forwarded to the table in Target. |
| Comments (I) | Optional description of the subscription. |
| Options (I) | Bit field of options for creating this subscription. The options can be ORed together. The options are:  ADS\_DEFAULT (0): If no options are needed, this value can be used.  ADS\_SUBSCR\_QUEUE\_IS\_STATIC (1): Specifies that the name of the replication queue specified by ReplicationQueue should be stored as a full path. If this option is not provided, the path stored will be relative to the data dictionary.  ADS\_SUBSCR\_AIS\_TARGET (2): Specifies that the connection to the target server is an AIS (ADS\_AIS\_SERVER) connection. If it is not provided, the connection will be of type ADS\_REMOTE\_SERVER.  ADS\_SUBSCR\_IGNORE\_FAILED\_REP (4): If this option is specified, then replication updates that fail to update the target record are removed from the replication queue and replication will continue. If this option is not specified, the pending update will not be removed from the queue; the update will be periodically retried until it succeeds or is manually removed from the replication queue. Regardless of this setting, the replication failure is logged to the Advantage error log.  ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA (8): If this option is specified, the data from the searchable columns of failed replication updates is logged with the replication failure. If this is not specified, only the failed SQL statement is logged (with no data). |

Remarks

This function creates a new subscription object for defining where a publication is to be replicated. See [Replication](master_replication_overview.md) for more details. After a subscription is created, tables (articles) that are in the publication specified by PublicationName will be marked for replication once they are physically opened by Advantage Database Server. If the tables are currently open, they will not be marked for replication until they are closed and re-opened again.

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

[system.subscriptions](master_system_subscriptions.md)

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.md)

[sp\_DropSubscription](master_sp_dropsubscription.md)

[sp\_CreatePublication](master_sp_createpublication.md)
