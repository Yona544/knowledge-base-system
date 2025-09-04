---
title: Master Sp Mggetallindexes
slug: master_sp_mggetallindexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetallindexes.htm
source: Advantage CHM
tags:
  - master
checksum: 4977f4e41094f5a3aac4f818b6acc2c9260f216c
---

# Master Sp Mggetallindexes

sp\_mgGetAllIndexes

sp\_mgGetAllIndexes

Advantage SQL Engine

| sp\_mgGetAllIndexes  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all the index files that are currently opened on the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetAllIndexes()

Parameters

| IndexName (O) | Full path and file name of each index file currently open on the server. |

Remarks

This procedure returns the fully qualified path names of all index files that are opened on the server by all users.

Note With Advantage Local Server, sp\_mgGetAllIndexes will only return information about indexes opened by the instance of Advantage Local Server currently loaded into memory. Information about indexes opened by other instances of Advantage Local Server will not be returned.

Example

EXECUTE PROCEDURE sp\_mgGetAllIndexes();

See Also

[sp\_mgGetTableIndexes](master_sp_mggettableindexes.md)

[sp\_mgGetUserIndexes](master_sp_mggetuserindexes.md)

[sp\_mgGetAllTables](master_sp_mggetalltables.md)
