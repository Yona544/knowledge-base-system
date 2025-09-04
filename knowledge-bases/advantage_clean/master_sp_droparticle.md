---
title: Master Sp Droparticle
slug: master_sp_droparticle
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_droparticle.htm
source: Advantage CHM
tags:
  - master
checksum: 8fb04b1be5032f3873482342bbb8f33bcc8a5672
---

# Master Sp Droparticle

sp\_DropArticle

sp\_DropArticle

Advantage SQL Engine

| sp\_DropArticle  Advantage SQL Engine |  |  |  |  |

Delete a published article from the database.

Syntax

sp\_DropArticle(

PublicationName,CHARACTER,200,

ObjectName,CHARACTER,200 )

 

Parameters

| PublicationName (I) | Name of the publication object that contains the article to delete. |
| ObjectName (I) | The name of the article to delete from the specified publication. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary, or the article specified by ObjectName does not exist in the publication. |

Remarks

sp\_DropArticle removes an existing article from a publication.

Example

EXECUTE PROCEDURE sp\_DropArticle( 'mypub', 'table1' )

 

See Also

[sp\_CreateArticle](master_sp_createarticle.md)

[sp\_DropPublication](master_sp_droppublication.md)
