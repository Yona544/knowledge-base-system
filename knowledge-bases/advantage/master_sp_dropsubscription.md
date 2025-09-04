sp\_DropSubscription




Advantage Database Server 12  

sp\_DropSubscription

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropSubscription  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropSubscription Advantage SQL Engine master\_Sp\_dropsubscription Advantage SQL > System Procedures > Procedures > sp\_DropSubscription / Dear Support Staff, |  |
| sp\_DropSubscription  Advantage SQL Engine |  |  |  |  |

Delete a subscription object from the database.

Syntax

sp\_DropSubscription(SubscriptionName,CHARACTER,200 )

 

Parameters

|  |  |
| --- | --- |
| SubscriptionName (I) | Name of the subscription object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The subscription specified by SubscriptionName cannot be located in the data dictionary. |

Remarks

sp\_DropSubscription removes an existing subscription from the database.

Example

EXECUTE PROCEDURE sp\_DropSubscription( 'mysub' )

 

See Also

[sp\_CreateSubscription](master_sp_createsubscription.htm)