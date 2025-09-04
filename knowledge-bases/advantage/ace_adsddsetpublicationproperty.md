AdsDDSetPublicationProperty




Advantage Database Server 12  

AdsDDSetPublicationProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDSetPublicationProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDSetPublicationProperty Advantage Client Engine ace\_Adsddsetpublicationproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDSetPublicationProperty  Advantage Client Engine |  |  |  |  |

Set the property of an existing publication in the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDSetPublicationProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of a publication in the database. |
| usPropertyID (I) | Index of the property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to property value to be stored in the data dictionary. |
| pusPropertyLen (I) | Length of the property pointed to by the pvProperty parameter. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid publication property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by pucPublicationName cannot be located in the data dictionary. |

Remarks

AdsDDSetPublicationProperty sets one property for the specified publication in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the publication description. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the description is removed. |
| ADS\_DD\_PUBLICATION\_OPTIONS | This is reserved for future use. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined publication property. If pvProperty is NULL, the user-defined property is removed. The user-defined property is set, read, and interpreted by the application. It is not used by Advantage. |

Example

strcpy( aucDesc, "This is a test publication." );

ulRetVal = AdsDDSetPublicationProperty( hConn, "mypub",

ADS\_DD\_COMMENT, aucDesc,

(UNSIGNED16)( strlen(aucDesc) + 1 ));

 

See Also

[AdsDDCreatePublication](ace_adsddcreatepublication.htm)

[AdsDDGetPublicationProperty](ace_adsddgetpublicationproperty.htm)