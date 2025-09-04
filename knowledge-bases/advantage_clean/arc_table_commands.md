---
title: Arc Table Commands
slug: arc_table_commands
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_table_commands.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: dae011fc2b55ab295551e880def658178d82ad98
---

# Arc Table Commands

Table Commands

Table Commands

Advantage Data Architect

| Table Commands  Advantage Data Architect |  |  |  |  |

Encrypt Table

Encrypts the current table with the password supplied by the user.

Decrypt Table

Decrypts the current table after the user supplies the correct password.

Pack Table

Pack Table removes all deleted records from this table instance. Internal fragmentation in memo files will also be eliminated. The table is then re-indexed. If using non-structural indexes, the indexes must be opened during the pack or they will become logically invalid. Note that if encryption was ever enabled on the table, the table cannot be packed unless the encryption is enabled with the correct password.

Empty Table

Empty Table will remove all records from the table; ARC then re-indexes the table. If using non-structural indexes, the indexes must be opened during the empty or they will become invalid.

Recall Current Record

Recalls the current record if it is deleted. This is only a valid command on DBF tables.

Recall All Records

Recalls all deleted records inside the current table. This is only a valid command on DBF tables.

Re-Index

Rebuilds all indexes associated with the current table.

Environment Settings

Use Database | Environment Settings to specify various options for Advantage Data Architect.
