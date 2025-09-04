AdsDDCreateSubscription




Advantage Database Server 12  

AdsDDCreateSubscription

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDCreateSubscription  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDCreateSubscription Advantage Client Engine ace\_Adsddcreatesubscription Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDCreateSubscription  Advantage Client Engine |  |  |  |  |

Add a new subscription to the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDCreateSubscription(

ADSHANDLE hDictionary,

UNSIGNED8 \*pucSubscriptionName,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucTarget,

UNSIGNED8 \*pucUser,

UNSIGNED8 \*pucPassword,

UNSIGNED8 \*pucReplicationQueue,

UNSIGNED16 usForward,

UNSIGNED8 \*pucComments,

UNSIGNED32 ulOptions );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucSubscriptionName (I) | The name of the subscription to be created. |
| pucPublicationName (I) | The name of an existing publication object. The articles (tables) in this publication will be replicated according to the subscription definition. |
| pucTarget (I) | The full connection path to the target database; the path must include the target data dictionary name. This path is where the data will be replicated to. Generally, this should be a UNC style path. |
| pucUser (I) | This is the user name to use when Advantage Database Server connects to the target database (specified by pucTarget) to perform replication updates. This is sometimes referred to as the replication user. This user must exist in the data dictionary identified by pucTarget. |
| pucPassword (I) | The password associated with pucUser. |
| pucReplicationQueue (I) | The name of the replication queue that stores pending replication updates. This must be a valid table name. If no path is provided, the table will be located in the same directory as the data dictionary. |
| usForward (I) | This flag (TRUE/FALSE) determines if replication updates are forwarded from this data dictionary. If this flag is TRUE and an update is made to a table through replication (as opposed to a direct client update), then the update will be forwarded to the table in pucTarget. |
| pucComments (I) | Optional description of the subscription. |
| ulOptions (I) | Bit field of options for creating this subscription. The options can be ORed together. The options are:  ADS\_DEFAULT: If no options are needed, this value (0) can be used.  ADS\_SUBSCR\_QUEUE\_IS\_STATIC: Specifies that the name of the replication queue specified by pucReplicationQueue should be stored as a full path. If this option is not provided, the path stored will be relative to the data dictionary.  ADS\_SUBSCR\_AIS\_TARGET: Specifies that the connection to the target server is an AIS (ADS\_AIS\_SERVER) connection. If it is not provided, the connection will be of type ADS\_REMOTE\_SERVER.  ADS\_SUBSCR\_IGNORE\_FAILED\_REP: If this option is specified, replication updates that fail to update the target record are removed from the replication queue and replication will continue. If this option is not specified, the pending update will not be removed from the queue; the update will be periodically retried until it succeeds or is manually removed from the replication queue. Regardless of this setting, the replication failure is logged to the Advantage error log.  ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA: If this option is specified, the data from the searchable columns of failed replication updates is logged with the replication failure. If this is not specified, only the failed SQL statement is logged (with no data). |

Remarks

This function creates a new subscription object for defining where a publication is to be replicated. See [Replication](master_replication_overview.htm) for more details. After a subscription is created, tables (articles) that are in the publication specified by pucPublicationName will be marked for replication once they are physically opened by Advantage Database Server. If the tables are currently open, they will not be marked for replication until they are closed and re-opened again.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDCreatePublication( hConn, "mypub", "test publication",

ADS\_DEFAULT );

ulRetVal = AdsDDCreateArticle( hConn, "mypub", "table1", NULL, NULL,

  ADS\_IDENTIFY\_BY\_ALL );

ulRetVal = AdsDDCreateSubscription( hConn, "mysub", "mypub",

"\\\\server\\share\\path\\target.add",

"username", "password", "repqueue.adt", FALSE,

"test subscription",

ADS\_SUBSCR\_IGNORE\_FAILED\_REP |

ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA );

 

See Also

[AdsDDGetSubscriptionProperty](ace_adsddgetsubscriptionproperty.htm)

[AdsDDSetSubscriptionProperty](ace_adsddsetsubscriptionproperty.htm)

[AdsDDDeleteSubscription](ace_adsdddeletesubscription.htm)

[AdsDDCreatePublication](ace_adsddcreatepublication.htm)