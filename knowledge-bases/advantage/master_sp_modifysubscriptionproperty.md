sp\_ModifySubscriptionProperty




Advantage Database Server 12  

sp\_ModifySubscriptionProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifySubscriptionProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifySubscriptionProperty Advantage SQL Engine master\_Sp\_modifysubscriptionproperty Advantage SQL > System Procedures > Procedures > sp\_ModifySubscriptionProperty / Dear Support Staff, |  |
| sp\_ModifySubscriptionProperty  Advantage SQL Engine |  |  |  |  |

Set the property of an existing subscription in the data dictionary.

Syntax

sp\_ModifySubscriptionProperty(

SubscriptionName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

 

Parameters

|  |  |
| --- | --- |
| SubscriptionName (I) | The name of a subscription in the database. |
| Property (I) | Name of the property to set. See Remarks for allowed values. |
| Value (I) | Value to be stored in the data dictionary in string format. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in Property is not a valid subscription property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The subscription specified by SubscriptionName cannot be located in the data dictionary. |

Remarks

sp\_ModifySubscriptionProperty sets one property for the specified subscription in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values for Property.

|  |  |
| --- | --- |
| Property | Description |
| COMMENT | Changes the subscription description. |
| PUBLICATION | Changes the publication that this subscription uses. The value should be the name of an existing publication object in the data dictionary. |
| TARGET | Changes the target database for the replication updates. |
| TARGET\_USERNAME | Changes the user name that Advantage Database Server uses when making a replication connection to the target. |
| TARGET\_PASSWORD | Changes the password that Advantage Database Server uses when making a replication connection to the target. |
| FORWARD | Sets the flag that specifies whether or not replication updates are forwarded. The value can be True or False. |
| ENABLED | Sets the flag that specifies whether or not this subscription is enabled. The value can be True or False. |
| REPLICATION\_QUEUE | Changes the replication queue that stores pending replication updates. If the queue is currently not empty, the error AE\_SUBSCRIPTION\_QUEUE\_NOT\_EMPTY will be returned. |
| OPTIONS | Set the additional options that control the subscription behavior. The value is a 4 byte integer that can contain the following values ORed together: ADS\_DEFAULT (0), ADS\_SUBSCR\_QUEUE\_IS\_STATIC (1), ADS\_SUBSCR\_AIS\_TARGET (2), ADS\_SUBSCR\_IGNORE\_FAILED\_REP (4), and ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA (8). See [sp\_CreateSubscription](master_sp_createsubscription.htm) for additional information on the subscription options. |
| PAUSED | Sets the flag that specifies whether or not this subscription is paused. Paused subscriptions place replication updates in the queue, but the updates do not get sent to the target server until the subscription is un-paused. The value can be True or False. |
| USER\_DEFINED\_PROP | Changes the user defined subscription property. The user-defined property is set, read, and interpreted by the application. It is not used by Advantage. |
| TCP/IP | Sets the flag that enables or disables TCP/IP communication to the target.  The Value can be True or False.  Note that only one subscription communication type can be enabled at a time.  Setting one to True will automatically set the others to False. |
| UDP/IP | Sets the flag that enables or disables UDP/IP communication to the target.  The Value can be True or False.  Note that only one subscription communication type can be enabled at a time.  Setting one to True will automatically set the others to False. |
| IPX | Sets the flag that enables or disables IPX communication to the target.  The Value can be True or False.  Note that only one subscription communication type can be enabled at a time.  Setting one to True will automatically set the others to False. |
| TLS | Sets the flag that enables or disables [Transport Layer Security](master_communications_encryption.htm)  (TLS) communications. When using TLS, it is also necessary to supply the TLS certificate path and the TLS common name via the CONNECTION\_STRING property. |
| CONNECTION\_STRING | Specifies a connection string to use for connecting to the target. This can be used in place of or in conjunction with the other connection-related properties. This property was added primarily so that [Transport Layer Security](master_communications_encryption.htm) options could be specified. Refer to [AdsConnect101](ace_adsconnect101.htm) for information on valid connection string properties. If a connection string property is provided in addition to a specifically defined property, the specific property will be used. For example, if "Data Source" is provided in the connection string and TARGET is also specified, then the path provided by TARGET will be used. |

Example

// Turn on forwarding

EXECUTE PROCEDURE sp\_ModifySubscriptionProperty( 'mysub', 'forward', 'true' );

 

// change the replication queue name

EXECUTE PROCEDURE sp\_ModifySubscriptionProperty( 'mysub',

'replication\_queue', 'newqueue.adt' );

 

See Also

[sp\_CreateSubscription](master_sp_createsubscription.htm)

[system.subscriptions](master_system_subscriptions.htm)