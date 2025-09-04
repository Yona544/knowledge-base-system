AdsDDDeleteSubscription




Advantage Database Server 12  

AdsDDDeleteSubscription

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeleteSubscription  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeleteSubscription Advantage Client Engine ace\_Adsdddeletesubscription Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeleteSubscription  Advantage Client Engine |  |  |  |  |

Delete a subscription object from the database.

Syntax

UNSIGNED32 AdsDDDeleteSubscription( ADSHANDLE hDictionary,

UNSIGNED8 \*pucSubscriptionName );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | Handle of a database connection. |
| pucSubscriptionName (I) | Name of the subscription object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The subscription specified by pucSubscriptionName cannot be located in the data dictionary. |

Remarks

AdsDDDeleteSubscription removes an existing subscription from the database.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDDeleteSubscription( hConn, "mysub" );

 

See Also

[AdsDDCreateSubscription](ace_adsddcreatesubscription.htm)