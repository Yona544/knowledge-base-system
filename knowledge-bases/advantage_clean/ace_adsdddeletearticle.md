---
title: Ace Adsdddeletearticle
slug: ace_adsdddeletearticle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdddeletearticle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 731d78a94f0e2ebcc6863ea5db2906e45a4799ed
---

# Ace Adsdddeletearticle

AdsDDDeleteArticle

AdsDDDeleteArticle

Advantage Client Engine

| AdsDDDeleteArticle  Advantage Client Engine |  |  |  |  |

Delete a published article from the database.

Syntax

UNSIGNED32 AdsDDDeleteArticle( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucObjectName );

 

Parameters

| hDictionary (I) | Handle of a database connection. |
| pucPublicationName (I) | Name of the publication object that contains the article to delete. |
| pucObjectName (I) | The name of the article to delete from the specified publication. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The publication specified by pucPublicationName cannot be located in the data dictionary, or the article specified by pucObjectName does not exist in the publication. |

Remarks

AdsDDDeleteArticle removes an existing article from a publication.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

ulRetVal = AdsDDDeleteArticle( hConn, "mypub", "table1" );

 

See Also

[AdsDDCreateArticle](ace_adsddcreatearticle.md)

[AdsDDDeletePublication](ace_adsdddeletepublication.md)
