---
title: Master Replication Library
slug: master_replication_library
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_replication_library.htm
source: Advantage CHM
tags:
  - master
checksum: 65742959650db7099cccdbf26304c54098d11e8b
---

# Master Replication Library

Replication\_Library

Replication\_Library

Advantage Database Server

| Replication\_Library  Advantage Database Server |  |  |  |  |

Default = none

The replication engine (beginning with v11 of Advantage) has the ability to load a specific version of the Advantage Client Engine library. This provides the capability to replicate to an older version of Advantage Database Server (e.g., replicate from v11.0 to v10.1). Specify the path and file name of the desired client library.  See [Replicating to Older Servers](master_replicating_to_older_servers.md) for more details.

For Windows:

Add the following string value using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\REPLICATION\_LIBRARY=c:\pathtolibrary\ace64.dll

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf):

REPLICATION\_LIBRARY=/usr/lib/libace.so.10
