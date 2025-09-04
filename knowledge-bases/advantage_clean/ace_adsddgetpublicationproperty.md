---
title: Ace Adsddgetpublicationproperty
slug: ace_adsddgetpublicationproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetpublicationproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 65b5d7fdbd1b3bcddb920f2bb9017340532ea16b
---

# Ace Adsddgetpublicationproperty

AdsDDGetPublicationProperty

AdsDDGetPublicationProperty

Advantage Client Engine

| AdsDDGetPublicationProperty  Advantage Client Engine |  |  |  |  |

Retrieve a property of a publication object from the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDGetPublicationProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

 

Parameters

| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of a publication in the database. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid publication property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

This function retrieves a property of the specified publication object from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The comment for the publication. |
| ADS\_DD\_PUBLICATION\_OPTIONS | The function returns a bit field of the options for the specified publication. This property is returned as a 4-byte integer in the buffer pointed to by pvProperty. pusPropertyLen must be 4 on input when calling this function with this property. The options are ORed together into the bit field. See [AdsDDCreatePublication](ace_adsddcreatepublication.md) for additional information on the publication options. |
| ADS\_DD\_USER\_DEFINED\_PROP | The function returns the user defined publication property in pvProperty. The user-defined property is set, read, and interpreted by the application. It is not used by Advantage. |

Example

usLen = sizeof( ulOptions );

ulRetVal = AdsDDGetPublicationProperty( hConn, "mypub",

ADS\_DD\_PUBLICATION\_OPTIONS,

&ulOptions, &usLen );

 

See Also

[AdsDDCreatePublication](ace_adsddcreatepublication.md)

[AdsDDSetPublicationProperty](ace_adsddsetpublicationproperty.md)
