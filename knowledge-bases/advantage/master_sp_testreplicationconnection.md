sp\_TestReplicationConnection




Advantage Database Server 12  

sp\_TestReplicationConnection

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_TestReplicationConnection  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_TestReplicationConnection Advantage SQL Engine master\_Sp\_TestReplicationConnection Advantage SQL > System Procedures > Procedures > sp\_TestReplicationConnection / Dear Support Staff, |  |
| sp\_TestReplicationConnection  Advantage SQL Engine |  |  |  |  |

Tests a subscriptions connection to the target database.

Syntax

sp\_TestReplicationConnection( Subscription, CiCharacter, 200; )

Parameters

|  |  |
| --- | --- |
| Subscription (I) | Subscription to test making a connection for |

Output

|  |  |
| --- | --- |
| ReturnCode (O) | Error code in the event of a failure. |
| ErrorMessage (O) | Error message in the event of a failure. |

Remarks

sp\_TestReplicationConnection can be used to test a subscription's ability to make a connection.

Example

EXECUTE PROCEDURE sp\_TestReplicationConnection( 'sub1' );

See Also

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.htm)