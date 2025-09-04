---
title: Ace Adsddsetsubscriptionproperty
slug: ace_adsddsetsubscriptionproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetsubscriptionproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 42f8d30e89f8aa2d3c009a1c4be17e3c7553c7e6
---

# Ace Adsddsetsubscriptionproperty

AdsDDSetSubscriptionProperty

AdsDDSetSubscriptionProperty

Advantage Client Engine

| AdsDDSetSubscriptionProperty  Advantage Client Engine |  |  |  |  |

Set the property of an existing subscription in the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDSetSubscriptionProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucSubscriptionName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

 

Parameters

| hDictionary (I) | A data dictionary connection. |
| pucSubscriptionName (I) | The name of a subscription in the database. |
| usPropertyID (I) | Index of the property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to property value to be stored in the data dictionary. |
| usPropertyLen (I) | Length of the property pointed to by the pvProperty parameter. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid article property, or the specified property cannot be retrieved. |
| AE\_INVALID\_OBJECT\_NAME | The subscription specified by pucSubscriptionName cannot be located in the data dictionary. |

Remarks

AdsDDSetSubscriptionProperty sets one property for the specified subscription in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the subscription description. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the description is removed. |
| ADS\_DD\_SUBSCR\_PUBLICATION\_NAME | Changes the publication that this subscription uses. pvProperty must point to a NULL terminated string that is the name of an existing publication object in the data dictionary. |
| ADS\_DD\_SUBSCR\_TARGET | Changes the target database for the replication updates. pvProperty cannot be NULL or an empty string for this option. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_SUBSCR\_USERNAME | Changes the user name that Advantage Database Server uses when making a replication connection to the target. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the user name is removed. |
| ADS\_DD\_SUBSCR\_PASSWORD | Changes the password that Advantage Database Server uses when making a replication connection to the target. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the password is removed. |
| ADS\_DD\_SUBSCR\_FORWARD | Sets the flag that specifies whether or not replication updates are forwarded. pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE). |
| ADS\_DD\_SUBSCR\_ENABLED | Sets the flag that specifies whether or not this subscription is enabled. pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE). |
| ADS\_DD\_SUBSCR\_QUEUE\_NAME | Changes the replication queue that stores pending replication updates. If the current queue is currently not empty, the error AE\_SUBSCRIPTION\_QUEUE\_NOT\_EMPTY will be returned. pvProperty cannot be NULL or an empty string for this option. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_SUBSCR\_OPTIONS | Set the additional options that control the subscription behavior. pvProperty is expected to contain a 4 byte (UNSIGNED32) value that can contain the following values ORed together: ADS\_DEFAULT, ADS\_SUBSCR\_QUEUE\_IS\_STATIC, ADS\_SUBSCR\_AIS\_TARGET, ADS\_SUBSCR\_IGNORE\_FAILED\_REP, and ADS\_SUBSCR\_LOG\_FAILED\_REP\_DATA. See [AdsDDCreateSubscription](ace_adsddcreatesubscription.md) for additional information on the subscription options. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined subscription property. If pvProperty is NULL, the user-defined property is removed. The user-defined property is set, read, and interpreted by the application. It is not used by Advantage. |
| ADS\_DD\_SUBSCR\_PAUSED | Sets the flag that specifies whether or not this subscription is paused. Paused subscriptions place replication updates in the queue, but the updates do not get sent to the target server until the subscription is un-paused. pvProperty is expected to contain a 2 bytes (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE). |
| ADS\_DD\_SUBSCR\_COMM\_TCP\_IP | Sets the flag that enables or disables TCP/IP communication to the target database.  pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE).  Note that only one subscription communication type can be enabled at a time.  Setting one to TRUE will automatically set the others to FALSE. |
| ADS\_DD\_SUBSCR\_COMM\_UDP\_IP | Sets the flag that enables or disables UDP/IP communication to the target database.  pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE).  Note that only one subscription communication type can be enabled at a time.  Setting one to TRUE will automatically set the others to FALSE. |
| ADS\_DD\_SUBSCR\_COMM\_IPX | Sets the flag that enables or disables IPX communication to the target database.  pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE).  Note that only one subscription communication type can be enabled at a time.  Setting one to TRUE will automatically set the others to FALSE. |
| ADS\_DD\_SUBSCR\_COMM\_TLS | Sets the flag that enables or disables [Transport Layer Security](master_communications_encryption.md)  (TLS) communications. When using TLS, it is also necessary to supply the TLS certificate path and the TLS common name via the ADS\_DD\_SUBSCR\_CONNECTION\_STR property. |
| ADS\_DD\_SUBSCR\_CONNECTION\_STR | Specifies a connection string to use for connecting to the target. This can be used in place of or in conjunction with the other connection-related properties. This property was added primarily so that [Transport Layer Security](master_communications_encryption.md) options could be specified. Refer to [AdsConnect101](ace_adsconnect101.md) for information on valid connection string properties. If a connection string property is provided in addition to a specifically defined property, the specific property will be used. For example, if "Data Source" is provided in the connection string and ADS\_DD\_SUBSCR\_TARGET is also specified, then the path provided in ADS\_DD\_SUBSCR\_TARGET will be used. |

Example

// Turn on forwarding

usVal = TRUE;

ulRet = AdsDDSetSubscriptionProperty( hConn, "mysub",

  ADS\_DD\_SUBSCR\_FORWARD, &usVal, 2 );

 

// change the replication queue name

strcpy( aucBuf, "myrepqueue.adt" );

ulRet = AdsDDSetSubscriptionProperty( hConn, "mysub",

  ADS\_DD\_SUBSCR\_QUEUE\_NAME,

  aucBuf, (UNSIGNED16)( strlen(aucBuf) + 1 ));

 

See Also

[AdsDDCreateSubscription](ace_adsddcreatesubscription.md)

[AdsDDGetSubscriptionProperty](ace_adsddgetsubscriptionproperty.md)
