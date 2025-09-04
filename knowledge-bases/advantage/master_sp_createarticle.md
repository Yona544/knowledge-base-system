sp\_CreateArticle




Advantage Database Server 12  

sp\_CreateArticle

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_CreateArticle  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_CreateArticle Advantage SQL Engine master\_Sp\_createarticle Advantage SQL > System Procedures > Procedures > sp\_CreateArticle / Dear Support Staff, |  |
| sp\_CreateArticle  Advantage SQL Engine |  |  |  |  |

Add a new article to an existing publication in the data dictionary.

Syntax

sp\_CreateArticle(

PublicationName,CHARACTER,200,

ObjectName,CHARACTER,200,

IdentColumns,MEMO,

Filter,MEMO,

Options,Integer )

 

sp\_CreateArticle(

PublicationName,CHARACTER,200,

ObjectName,CHARACTER,200,

IdentColumns,MEMO,

Filter,NMEMO,

Options,Integer )

 

 

Parameters

|  |  |
| --- | --- |
| PublicationName (I) | The name of an existing publication in the dictionary. |
| ObjectName (I) | The name of the object to be published. Currently this can only be an existing data dictionary-bound table. |
| IdentColumns (I) | Optional semicolon- or comma-delimited list of column names that are to be used to identify the record in the target table. |
| Filter (I) | Optional horizontal filter to be applied to the record data to determine if it should be replicated. |
| Options (I) | Bit field of options for creating this publication article. The options can be ORed together. The options are:  ADS\_DEFAULT (0): If no options are needed, this value (0) can be used.  ADS\_IDENTIFY\_BY\_PRIMARY (1): If this option is given, the tables primary key will be used to identify the record for updating in the target table. If fields are given in IdentColumns, they will be also be used.  ADS\_IDENTIFY\_BY\_ALL (2): If this option is given, all searchable columns will be used for identifying the record for updating in the target table. If this option is provided, the IdentColumns parameter is ignored. Note that this option will not include ROWVERSION and MODTIME fields; those fields are not generally useful for replication purposes. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the given publication does not exist in the data dictionary or if the object (table) to be published does not exist in the data dictionary. |

Remarks

This function adds an existing table as an article to an existing publication. See [Replication](master_replication_overview.htm) for more details. Currently only tables can be published.

When a replicated table is updated, the corresponding record in the target table is located by using the specified identification columns. Therefore, the identification columns must uniquely and accurately define the record. The most efficient choice is probably to use the primary key of the table since it is usually indexed. If all searchable columns are used and the target record has already been modified, the record will not be found for replication.

If you do not want to replicate all columns in the table, you can define a vertical filter to specify which columns of data should be replicated. To define a vertical filter, use [sp\_ModifyArticleProperty](master_sp_modifyarticleproperty.htm) to modify the article after it has been created.

Example

EXECUTE PROCEDURE sp\_CreatePublication( 'mypub', 'test publication', 0 );

 

// publish table1 and use all searchable columns for identification. Specify

// a filter to only replicate a subset of the data

EXECUTE PROCEDURE sp\_CreateArticle( 'mypub', 'table1', NULL,

'CountryCode=[SE]', 2 );

 

// publish table2 and use the primary key for identification

EXECUTE PROCEDURE sp\_CreateArticle( 'mypub', 'table2', NULL,

NULL, 1 );

// publish table3 and use the specified columns for identification

EXECUTE PROCEDURE sp\_CreateArticle( 'mypub', 'table3',

'employeeid;lastname;firstname',

NULL, 0 );

 

See Also

[sp\_CreatePublication](master_sp_createpublication.htm)

[sp\_CreateSubscription](master_sp_createsubscription.htm)

[sp\_ModifyArticleProperty](master_sp_modifyarticleproperty.htm)

[system.articles](master_system_publicationarticles.htm)

[sp\_DropArticle](master_sp_droparticle.htm)