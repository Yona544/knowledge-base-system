AdsDDCreatePublication




Advantage Database Server 12  

AdsDDCreatePublication

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDCreatePublication  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDCreatePublication Advantage Client Engine ace\_Adsddcreatepublication Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDCreatePublication  Advantage Client Engine |  |  |  |  |

Add a new publication to the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDCreatePublication( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucComments,

UNSIGNED32 ulOptions );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of the publication to be created. |
| pucComments (I) | Optional description of the publication. |
| ulOptions (I) | This is reserved for future use. It should be ADS\_DEFAULT (0). |

Remarks

This function creates a new publication object for holding replication articles. The publication itself is just a container object and has no specific properties associated with it. See [Replication](master_replication_overview.htm) for more details.

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

[AdsDDGetPublicationProperty](ace_adsddgetpublicationproperty.htm)

[AdsDDSetPublicationProperty](ace_adsddsetpublicationproperty.htm)

[AdsDDDeletePublication](ace_adsdddeletepublication.htm)

[AdsDDCreateArticle](ace_adsddcreatearticle.htm)

[AdsDDCreateSubscription](ace_adsddcreatesubscription.htm)