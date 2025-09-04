sp\_DropPublication




Advantage Database Server 12  

sp\_DropPublication

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropPublication  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropPublication Advantage SQL Engine master\_Sp\_droppublication Advantage SQL > System Procedures > Procedures > sp\_DropPublication / Dear Support Staff, |  |
| sp\_DropPublication  Advantage SQL Engine |  |  |  |  |

Delete a publication object from the database.

Syntax

sp\_DropPublication( PublicationName,CHARACTER,200 )

Parameters

|  |  |
| --- | --- |
| PublicationName (I) | Name of the publication object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary, or the publication is in use by one or more subscriptions. |

Remarks

AdsDDDeletePublication removes an existing publication from the database.

Example

EXECUTE PROCEDURE sp\_DropPublication( 'mypub' )

 

See Also

[sp\_CreatePublication](master_sp_createpublication.htm)

[sp\_ModifySubscriptionProperty](master_sp_modifysubscriptionproperty.htm)

[sp\_DropSubscription](master_sp_dropsubscription.htm)