---
title: Vo Ax Setservertype
slug: vo_ax_setservertype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_setservertype.htm
source: Advantage CHM
tags:
  - vo
checksum: 3050dab1351cd6ddc7955ce8736771ecdd6fe82f
---

# Vo Ax Setservertype

AX\_SetServerType()

AX\_SetServerType()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_SetServerType()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Determines which type of Advantage server the client application can use

Syntax

AX\_SetServerType( lUseRemoteServer, lUseInternetServer, lUseLocalServer )

 

| lUseRemoteServer [.T.|.F.] | A logical value that determines if the Advantage Database Server should be used. |
| lUseInternetServer [.T.|.F.] | A logical value that determines if the Internet server should be used. |
| lUseLocalServer [.T.|.F.] | A logical value that determines if the Advantage Local Server should be used. |

Description

AX\_SetServerType determines which types of Advantage servers the client application can use. By default, all three Advantage server types are enabled. The following precedence (by default) is followed when attempting to connect: highest priority is given to the [Advantage Database Server](master_advantage_database_server.md), second priority to the [Advantage Internet Server](master_advantage_internet_server_overview.md), and lowest priority to the [Advantage Local Server](master_advantage_local_server.md). The first parameter enables connections to the Advantage Database Server. The second parameter enables connections to the Advantage Internet Server functionality, and the third parameter enables connections to the Advantage Local Server. If multiple server types are enabled, then the connection type is determined by the precedence mentioned above.

Example

AX\_SetServerType( .T., .T., .T. ) // use all server types

USE test VIA "DBFNTXAX"
