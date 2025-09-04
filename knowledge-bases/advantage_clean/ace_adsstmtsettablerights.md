---
title: Ace Adsstmtsettablerights
slug: ace_adsstmtsettablerights
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablerights.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2805b1facb5308f18f332525baef8211d11a68a3
---

# Ace Adsstmtsettablerights

AdsStmtSetTableRights

AdsStmtSetTableRights

Advantage Client Engine

| AdsStmtSetTableRights  Advantage Client Engine |  |  |  |  |

This API has been deprecated, the documentation below has been left as reference material. This API has no affect.

Sets the rights checking mode used by the statement

Syntax

| UNSIGNED32 | AdsStmtSetTableRights( ADSHANDLE hStatement,  UNSIGNED16 usCheckRights ) |

Parameters

| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| usCheckRights (I) | Indicates if the server is to use rights checking for the file open. Options are ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. If ADS\_CHECKRIGHTS is given, then the Advantage Database Server will use the rights of the connected user when creating the file, and if the user does not have rights to the directory or server, then the creation will fail. If ADS\_IGNORERIGHTS is used, then the Advantage Database Server will ignore the connected user's rights and create the table regardless. This way an application developer can allow only Advantage-based applications to access specific data. |

Remarks

The default value for newly created statement handles is ADS\_CHECKRIGHTS.

Note An open cursor cannot be associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.md) before calling this API.

Example

[Click Here](ace_more_examples.md#adsstmtsettablerightsexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.md)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.md)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.md)

[AdsStmtSetTableType](ace_adsstmtsettabletype.md)
