AdsDDGetSubscriptionProperty




Advantage Database Server 12  

AdsDDGetSubscriptionProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetSubscriptionProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetSubscriptionProperty Advantage Client Engine ace\_Adsddgetsubscriptionproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetSubscriptionProperty  Advantage Client Engine |  |  |  |  |

Retrieve a property of a subscription from the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDGetSubscriptionProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucSubscriptionName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucSubscriptionName (I) | The name of a subscription in the database. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid article property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

This function retrieves a property of the specified subscription from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and pusPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | The comment for the subscription. |
| ADS\_DD\_SUBSCR\_PUBLICATION\_NAME | The function returns the name of the publication this subscription is using. The name is returned as a NULL terminated string in pvProperty. |
| ADS\_DD\_SUBSCR\_TARGET | The function returns the target database this subscription is replicating to. The path is returned as a NULL terminated string in pvProperty. |
| ADS\_DD\_SUBSCR\_USERNAME | The function returns the user name for the target database. The name is returned as a NULL terminated string in pvProperty. |
| ADS\_DD\_SUBSCR\_FORWARD | The function returns the flag that specifies whether or not replication updates are forwarded. It is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_ENABLED | The function returns the flag that specifies whether or not this subscription is enabled. It is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_QUEUE\_NAME | The function returns the replication queue that stores pending replication updates. The name is returned as a NULL terminated string in pvProperty. |
| ADS\_DD\_SUBSCR\_OPTIONS | The function returns a bit field of the options for the specified subscription. This property is returned as a 4-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 4 on input when calling this function with this property. The options are ORed together into the bit field. See [AdsDDCreateSubscription](ace_adsddcreatesubscription.htm) for additional information on the subscription options. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined subscription property in pvProperty. The user defined property is set, read, and interpreted by the application. It is not used by Advantage. |
| ADS\_DD\_SUBSCR\_PAUSED | The function returns the flag that specifies whether or not this subscription is paused. It is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_COMM\_TCP\_IP | The function returns the flag that specifies whether or not this subscription uses TCP/IP communication with the target database.  It is returned as a 2-byte integer (UNSIGNED16) in the buffer pointed to by pvProperty.  \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_COMM\_UDP\_IP | The function returns the flag that specifies whether or not this subscription uses UDP/IP communication with the target database.  It is returned as a 2-byte integer (UNSIGNED16) in the buffer pointed to by pvProperty.  \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_COMM\_IPX | The function returns the flag that specifies whether or not this subscription uses IPX communication with the target database.  It is returned as a 2-byte integer (UNSIGNED16) in the buffer pointed to by pvProperty.  \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_COMM\_TLS | This function returns the flag that specifies whether or not this subscription uses [Transport Layer Security](master_communications_encryption.htm) (TLS) communications with the target database.It is returned as a 2-byte integer (UNSIGNED16) in the buffer pointed to by pvProperty.  \*pusPropertyLen must be 2 on input. |
| ADS\_DD\_SUBSCR\_CONNECTION\_STR | The function returns the connection string stored with this subscription. The value is returned as a NULL terminated string in pvProperty. See [AdsDDSetSubscriptionProperty](ace_adsddsetsubscriptionproperty.htm) for more information on this property. |

Example

// retrieve the target database for a subscription

usLen = sizeof( aucBuf );

ulRetVal = AdsDDGetSubscriptionProperty( hConn, "mysub",

ADS\_DD\_SUBSCR\_TARGET, aucBuf, &usLen );

 

See Also

[AdsDDCreateSubscription](ace_adsdddeletesubscription.htm)

[AdsDDSetSubscriptionProperty](ace_adsddsetsubscriptionproperty.htm)