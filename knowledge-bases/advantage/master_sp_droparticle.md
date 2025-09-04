sp\_DropArticle




Advantage Database Server 12  

sp\_DropArticle

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropArticle  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropArticle Advantage SQL Engine master\_Sp\_droparticle Advantage SQL > System Procedures > Procedures > sp\_DropArticle / Dear Support Staff, |  |
| sp\_DropArticle  Advantage SQL Engine |  |  |  |  |

Delete a published article from the database.

Syntax

sp\_DropArticle(

PublicationName,CHARACTER,200,

ObjectName,CHARACTER,200 )

 

Parameters

|  |  |
| --- | --- |
| PublicationName (I) | Name of the publication object that contains the article to delete. |
| ObjectName (I) | The name of the article to delete from the specified publication. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary, or the article specified by ObjectName does not exist in the publication. |

Remarks

sp\_DropArticle removes an existing article from a publication.

Example

EXECUTE PROCEDURE sp\_DropArticle( 'mypub', 'table1' )

 

See Also

[sp\_CreateArticle](master_sp_createarticle.htm)

[sp\_DropPublication](master_sp_droppublication.htm)