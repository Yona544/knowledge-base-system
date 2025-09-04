---
title: Vo Using The Advantage Local Server
slug: vo_using_the_advantage_local_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_using_the_advantage_local_server.htm
source: Advantage CHM
tags:
  - vo
checksum: f9d525cd2c2097f7687daf66688bb1aab5ded674
---

# Vo Using The Advantage Local Server

Using the Advantage Local Server

Using the Advantage Local Server

Advantage Visual Objects and Vulcan.NET RDD

| Using the Advantage Local Server  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

By default, the Advantage RDDs will not use the Advantage Local Server. This local server can be used programmatically by calling the [AX\_SetServerType()](vo_ax_setservertype.md) function. However, the DB Server Editor within the Visual Objects IDE and various Report Writers also use the RDD. See [Advantage Local Server](master_advantage_local_server.md) for more information about Advantage server types.

To use the Advantage Local Server, you will need to change this default. Copy the ADS.INI file from the directory where Advantage was installed (C:\CAVO\ADS or C:\CAVO25\ADS by default) to the application directory, the Windows System directory, the Windows directory, or the client's path. The file contains this text:

[SETTINGS]

ADS\_SERVER\_TYPE = 7

The ADS\_SERVER\_TYPE value is set to 7. You may adjust this value to indicate what types of Advantage servers should be eligible for connecting. To calculate the value, add all of the constants representing the Advantage Server types that you wish to be eligible to connect:

1for the Advantage Local Server

2for the Advantage Database Server

4for the Advantage Internet Server

By default, the Advantage RDDs will connect to the Advantage Database Server and the Advantage Internet Server, so the default value would be equal to 6, which is 2 + 4. The value of 7, which equals 1 + 2 + 4, indicates all servers should be eligible.
