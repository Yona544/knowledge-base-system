sp\_ModifyArticleProperty




Advantage Database Server 12  

sp\_ModifyArticleProperty

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_ModifyArticleProperty  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_ModifyArticleProperty Advantage SQL Engine master\_Sp\_modifyarticleproperty Advantage SQL > System Procedures > Procedures > sp\_ModifyArticleProperty / Dear Support Staff, |  |
| sp\_ModifyArticleProperty  Advantage SQL Engine |  |  |  |  |

Set the property of an existing article in the data dictionary.

Syntax

sp\_ModifyArticleProperty(

PublicationName,CHARACTER,200,

ObjectName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

 

Parameters

|  |  |
| --- | --- |
| PublicationName (I) | The name of the publication in the database. |
| ObjectName (I) | The name of an article in the specified publication. |
| Property (I) | Name of the property to set. See Remarks for allowed values. |
| Value (I) | Value to be stored in the data dictionary in string format. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in Property is not a valid article property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary, or the article specified by ObjectName does not exist in the publication. |

Remarks

sp\_ModifyArticleProperty sets one property for the specified article in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values for Property.

|  |  |
| --- | --- |
| Property | Description |
| FILTER | Changes the replication filter for the article. |
| IDENT\_COLUMNS | Changes the identification columns to the given semicolon or comma delimited list of columns. |
| INCLUDE\_COLUMNS | Sets the vertical filter for the article to the given semicolon or comma-delimited list of columns. Only columns specified in the list will be replicated. If the property is NULL or is an empty string, the existing vertical filter is removed. Note that INCLUDE\_COLUMNS and EXCLUDE\_COLUMNS are mutually exclusive. Setting one property will clear the other. |
| EXCLUDE\_COLUMNS | Sets the vertical filter for the article to be all columns not in the given semicolon or comma-delimited list of columns. All columns not specified in the list will be replicated. If any columns are added to the table after setting this vertical filter, the new columns will be replicated because they will not be in the exclusion list. If the property is NULL or is an empty string, the existing filter is removed. Note that INCLUDE\_COLUMNS and EXCLUDE\_COLUMNS are mutually exclusive. Setting one property will clear the other. |
| UPDATE\_MERGE | Sets the flag that specifies whether or not this article uses SQL MERGE statements when performing UPDATEs at the target. |
| INSERT\_MERGE | Sets the flag that specifies whether or not this article uses SQL MERGE statements when performing INSERTs at the target. |

Example

// set the replication filter to a specific department

EXECUTE PROCEDURE sp\_ModifyArticleProperty( 'mypub', 'table1',

'filter', 'Department = 5' );

// Set a vertical filter to replicate only four columns in the table

EXECUTE PROCEDURE sp\_ModifyArticleProperty( 'mypub', 'table1',

'include\_columns', 'empid;lastname;firstname;department' );

 

See Also

[sp\_CreateArticle](master_sp_createarticle.htm)

[system.articles](master_system_publicationarticles.htm)