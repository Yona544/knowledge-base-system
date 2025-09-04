AdsDDGetArticleProperty




Advantage Database Server 12  

AdsDDGetArticleProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetArticleProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetArticleProperty Advantage Client Engine ace\_Adsddgetarticleproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetArticleProperty  Advantage Client Engine |  |  |  |  |

Retrieve a property of a published article from the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDGetArticleProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucObjectName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of an existing publication in the dictionary. |
| pucObjectName (I) | The name of an article in the specified publication. |
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

This function retrieves a property of the specified article in the specified publication from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and pusPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | The comment for the article. |
| ADS\_DD\_ARTICLE\_FILTER | The function returns the replication filter for the specified article.  Encoded as ANSI data. |
| ADS\_DD\_ARTICLE\_FILTER\_W | The function returns the replication filter for the specified article.  Encoded as UTF-16 data. |
| ADS\_DD\_ARTICLE\_ID\_COLUMNS | The function returns the semicolon-delimited list of fields that are used to identify the record in the target table. |
| ADS\_DD\_ARTICLE\_INCLUDE\_COLUMNS | If the table has an inclusive vertical filter, this option retrieves the semicolon-delimited list of fields included in replication. This will be empty if there is no vertical filter or if the vertical filter is defined as an exclusion list of columns. |
| ADS\_DD\_ARTICLE\_EXCLUDE\_COLUMNS | If the table has an exclusive vertical filter, this option retrieves the semicolon-delimited list of fields excluded from replication. This will be empty if there is no vertical filter or if the vertical filter is defined as an inclusion list of columns. |
| ADS\_DD\_ARTICLE\_UPDATE\_MERGE | The function returns the flag that specifies whether or not this subscription uses SQL MERGE statements when performing UPDATEs. It is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusProperty must be 2 on input. |
| ADS\_DD\_ARTICLE\_INSERT\_MERGE | The function returns the flag that specifies whether or not this subscription uses SQL MERGE statements when performing INSERTs. It is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusProperty must be 2 on input. |

Example

// retrieve the replication filter for an article

usLen = sizeof( aucBuf );

ulRetVal = AdsDDGetArticleProperty( hConn, "mypub", "table1",

 ADS\_DD\_ARTICLE\_FILTER, aucBuf, &usLen );

 

See Also

[AdsDDCreateArticle](ace_adsddcreatearticle.htm)

[AdsDDSetArticleProperty](ace_adsddsetarticleproperty.htm)