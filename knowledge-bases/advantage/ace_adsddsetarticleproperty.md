AdsDDSetArticleProperty




Advantage Database Server 12  

AdsDDSetArticleProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDSetArticleProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDSetArticleProperty Advantage Client Engine ace\_Adsddsetarticleproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDSetArticleProperty  Advantage Client Engine |  |  |  |  |

Set the property of an existing article in the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDSetArticleProperty( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucObjectName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

 

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of a publication in the database. |
| pucObjectName (I) | The name of an article in the specified publication. |
| usPropertyID (I) | Index of the property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to property value to be stored in the data dictionary. |
| pusPropertyLen (I) | Length of the property pointed to by the pvProperty parameter. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid article property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by pucPublicationName cannot be located in the data dictionary, or the article specified by pucObjectName does not exist in the publication. |

Remarks

AdsDDSetArticleProperty sets one property for the specified article in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Changes the article description. The pvProperty is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the description is removed. |
| ADS\_DD\_ARTICLE\_FILTER | Changes the replication filter for the article. If pvProperty is NULL or an empty string, the existing filter is removed. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_ARTICLE\_ID\_COLUMNS | Changes the identification columns to the given semicolon- or comma-delimited list of columns. Empty strings are not allowed for this property. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_ARTICLE\_INCLUDE\_COLUMNS | Sets the vertical filter for the article to the given semicolon or comma-delimited list of columns. Only columns specified in the list will be replicated. If pvProperty is NULL or is an empty string, the existing vertical filter is removed. usPropertyLen is the length of the string including the NULL terminator. Note that ADS\_DD\_ARTICLE\_INCLUDE\_COLUMNS and ADS\_DD\_ARTICLE\_EXCLUDE\_COLUMNS are mutually exclusive. Setting one property will clear the other. |
| ADS\_DD\_ARTICLE\_EXCLUDE\_COLUMNS | Sets the vertical filter for the article to be all columns not in the given semicolon or comma-delimited list of columns. All columns not specified in the list will be replicated. If any columns are added to the table after setting this vertical filter, the new columns will be replicated because they will not be in the exclusion list. If pvProperty is NULL or is an empty string, the existing filter is removed. usPropertyLen is the length of the string including the NULL terminator. Note that ADS\_DD\_ARTICLE\_INCLUDE\_COLUMNS and ADS\_DD\_ARTICLE\_EXCLUDE\_COLUMNS are mutually exclusive. Setting one property will clear the other. |
| ADS\_DD\_ARTICLE\_UPDATE\_MERGE | Sets the flag that specifies whether or not this article uses SQL MERGE statements when performing UPDATEs at the target. pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE). |
| ADS\_DD\_ARTICLE\_INSERT\_MERGE | Sets the flag that specifies whether or not this article uses SQL MERGE statements when performing INSERTs at the target. pvProperty is expected to contain a 2 byte (UNSIGNED16) value that is 0 (FALSE) or 1 (TRUE). |

Example

// set the replication filter to a specific department

strcpy( aucFilter, "Department = 5" );

ulRetVal = AdsDDSetArticleProperty( hConn, "mypub", "table1",

ADS\_DD\_ARTICLE\_FILTER, aucFilter,

(UNSIGNED16)( strlen(aucFilter) + 1 ));

strcpy( aucVerticalFilter, "empid;lastname;firstname;department" );

ulRetVal = AdsDDSetArticleProperty( hConn, "mypub", "table1",

ADS\_DD\_ARTICLE\_INCLUDE\_COLUMNS, aucVerticalFilter,

(UNSIGNED16)( strlen(aucVerticalFilter) + 1 ) );

 

See Also

[AdsDDCreateArticle](ace_adsddcreatearticle.htm)

[AdsDDGetArticleProperty](ace_adsddgetarticleproperty.htm)