---
title: Ace Adsddcreatearticle
slug: ace_adsddcreatearticle
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreatearticle.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ce45376b4856708161ad8d0bb7d0938480691f04
---

# Ace Adsddcreatearticle

AdsDDCreateArticle

AdsDDCreateArticle

Advantage Client Engine

| AdsDDCreateArticle  Advantage Client Engine |  |  |  |  |

Add a new article to an existing publication in the data dictionary.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDCreateArticle( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucRowIdentColumns,

UNSIGNED8 \*pucFilter,

UNSIGNED32 ulOptions );

 

UNSIGNED32 ENTRYPOINT AdsDDCreateArticle100( ADSHANDLE hDictionary,

UNSIGNED8 \*pucPublicationName,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucRowIdentColumns,

WCHAR     \*pwcFilter,

UNSIGNED32 ulOptions );

 

Parameters

| hDictionary (I) | A data dictionary connection. |
| pucPublicationName (I) | The name of an existing publication in the dictionary. |
| pucObjectName (I) | The name of the object to be published. Currently, this can only be an existing data dictionary-bound table. |
| pucRowIdentColumns (I) | Optional semicolon or comma delimited list of column names that are to be used to identify the record in the target table. |
| pucFilter (I) | Optional horizontal filter to be applied to the record data to determine if it should be replicated. |
| ulOptions (I) | Bit field of options for creating this publication article. The options can be ORed together. The options are:  ADS\_DEFAULT: If no options are needed, this value (0) can be used.  ADS\_IDENTIFY\_BY\_PRIMARY: If this option is given, the tables primary key will be used to identify the record for updating in the target table. If fields are also given in pucRowIdentColumns, they will be also be used.  ADS\_IDENTIFY\_BY\_ALL: If this option is given, all searchable columns will be used for identifying the record for updating in the target table. If this option is provided, the pucRowIdentColumns parameter is ignored. Note that this option will not include ROWVERSION and MODTIME fields; those fields are not generally useful for replication purposes. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the given publication does not exist in the data dictionary or if the object (table) to be published does not exist in the data dictionary. |

Remarks

This function adds an existing table as an article to an existing publication. See [Replication](master_replication_overview.md) for more details. Currently, only tables can be published.

When a replicated table is updated, the corresponding record in the target table is located by using the specified identification columns. Therefore, the identification columns must uniquely and accurately define the record. The most efficient choice is probably to use the primary key of the table since it is usually indexed. If all searchable columns are used and the target record has already been modified, then the record will not be found for replication.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

If you do not want to replicate all columns in the table, you can define a vertical filter to specify which columns of data should be replicated. To define a vertical filter, use [AdsDDSetArticleProperty](ace_adsddsetarticleproperty.md) to modify the article after it has been created.

Example

ulRetVal = AdsDDCreatePublication( hConn, "mypub", "test publication", 0 );

 

// publish table1 and use all searchable columns for identification. Specify

// a filter to only replicate a subset of the data

ulRetVal = AdsDDCreateArticle( hConn, "mypub", "table1", NULL,

    "CountryCode=[SE]",

    ADS\_IDENTIFY\_BY\_ALL );

// publish table2 and use the primary key for identification

ulRetVal = AdsDDCreateArticle( hConn, "mypub", "table2", NULL, NULL,

    ADS\_IDENTIFY\_BY\_PRIMARY );

// publish table3 and use the specified columns for identification

ulRetVal = AdsDDCreateArticle( hConn, "mypub", "table3",

    "employeeid;lastname;firstname",

    NULL, 0 );

 

See Also

[AdsDDCreatePublication](ace_adsddcreatepublication.md)

[AdsDDCreateSubscription](ace_adsddcreatesubscription.md)

[AdsDDSetArticleProperty](ace_adsddsetarticleproperty.md)

[AdsDDGetArticleProperty](ace_adsddgetarticleproperty.md)

[AdsDDDeleteArticle](ace_adsdddeletearticle.md)
