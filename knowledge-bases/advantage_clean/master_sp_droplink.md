---
title: Master Sp Droplink
slug: master_sp_droplink
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_droplink.htm
source: Advantage CHM
tags:
  - master
checksum: 071c1faa6e882d6bef2344f8d6f0d33a3646d333
---

# Master Sp Droplink

sp\_DropLink

sp\_DropLink

Advantage SQL Engine

| sp\_DropLink  Advantage SQL Engine |  |  |  |  |

Removes either a local link or a global link from the current connection.

Syntax

sp\_DropLink (

Name, CHARACTER, 200,

Global, LOGICAL )

Parameters

| Name (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| Global (I) | True to remove the global link alias from the data dictionary. This parameter can only be set to True for a database connection with administrative permissions. If this parameter is True, the Name parameter must specify the link alias in the data dictionary. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error may be returned if the Global parameter is True and the specified link cannot be found in the data dictionary. |

Remarks

This function can be used to either drop an active link from the current connection or remove a global link from the data dictionary. Since the database server maintains information on the active links, dropping active links from the current connection will free some resources consumed by the server.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database. The implicit link is then dropped.

SELECT Max(LastDate) FROM "n:\MyData\ARCHIVE\ARCHIVE.ADD".Table1;

 

EXECUTE PROCEDURE sp\_DropLink ( 'n:\MyData\ARCHIVE\ARCHIVE.ADD', FALSE );

 

See Also

[sp\_CreateLink](master_sp_createlink.md)

[sp\_ModifyLink](master_sp_modifylink.md)
