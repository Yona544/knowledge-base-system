---
title: Vo Ax Usingclientserver
slug: vo_ax_usingclientserver
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_usingclientserver.htm
source: Advantage CHM
tags:
  - vo
checksum: 75605d47662a9b131f3bd4f200c17aeff241b2e5
---

# Vo Ax Usingclientserver

AX\_UsingClientServer()

AX\_UsingClientServer()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_UsingClientServer()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Indicates whether the current work area is using the Advantage Database Server

Syntax

AX\_UsingClientServer() -> logical

Returns

AX\_UsingClientServer returns a .T. if the current Advantage work area is accessing the Advantage Database Server. Returns .F. if the current Advantage work area has opened the database file using the local RDD.

Description

AX\_UsingClientServer indicates whether the current Advantage work area is accessing the Advantage Database Server in "client/server" mode.

Example

oDB1 := AxDBServer{ "TEST1", .F., .F., "AXDBFNTX" }

if AX\_UsingClientServer()

? "File open in Client/Server mode."

else

? "Warning: File opened in Local mode."

endif
