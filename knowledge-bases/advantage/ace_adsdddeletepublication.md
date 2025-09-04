AdsDDDeletePublication




Advantage Database Server 12  

AdsDDDeletePublication

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeletePublication  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeletePublication Advantage Client Engine ace\_Adsdddeletepublication Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeletePublication  Advantage Client Engine |  |  |  |  |

Delete a publication object from the database.

Syntax

UNSIGNED32 AdsDDDeletePublication( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | Handle of a database connection. |
| pucPublicationName (I) | Name of the publication object to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by pucPublicationName cannot be located in the data dictionary, or the publication is in use by one or more subscriptions. |

Remarks

AdsDDDeletePublication removes an existing publication from the database.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDDeletePublication( hConn, "mypub" );

 

See Also

[AdsDDCreatePublication](ace_adsddcreatepublication.htm)

[AdsDDSetSubscriptionProperty](ace_adsddsetsubscriptionproperty.htm)

[AdsDDDeleteSubscription](ace_adsdddeletesubscription.htm)