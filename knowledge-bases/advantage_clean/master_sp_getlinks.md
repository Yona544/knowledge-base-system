---
title: Master Sp Getlinks
slug: master_sp_getlinks
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getlinks.htm
source: Advantage CHM
tags:
  - master
checksum: 2dc997e97e07ab61716e399d98f6d8f9f41afb15
---

# Master Sp Getlinks

sp\_GetLinks

sp\_GetLinks

Advantage SQL Engine

| sp\_GetLinks  Advantage SQL Engine |  |  |  |  |

Retrieve the links in the current dictionary.

Syntax

sp\_GetLinks()

Parameters

None

Output

| LinkAlias (O) | The link alias name |
| Path (O) | The path to the linked data dictionary. This path will be converted to a UNC path if the original connection path is not to the local machine. |

Remarks

Calls to this procedure are only allowed if the current connection is to the active [root dictionary](master_root_dictionary.md) and the user is a member of the SERVER:Monitor group.

The UNC conversion will be based on the connection path used by the current connection. For example, assume dictionary c:\d1\dictionary.add has a link alias D2 which uses a relative path to c:\d2\dictionary2.add and that there are two distinct shares or server side aliases pointing to the same directory.

If User A Connects to \\server\XYZ\d1\dictionary.add, the UNC conversion for relative link D2 will be \\server\XYZ\d2\dictionary2.add.

If User B connects using \\server\serveralias\d1\dictionary.add, the UNC conversion for relative link D2 will be \\server\serveralias\d2\dictionary.add.

See Also

[sp\_CreateLink](master_sp_createlink.md)
