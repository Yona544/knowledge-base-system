---
title: Master Network Attached Storage Nas Devices
slug: master_network_attached_storage_nas_devices
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_network_attached_storage_nas_devices.htm
source: Advantage CHM
tags:
  - master
checksum: 8879571f636f62e6902af350de9010c7f926a2ea
---

# Master Network Attached Storage Nas Devices

Network Attached Storage (NAS) Devices

Network Attached Storage (NAS) Devices

Advantage Concepts

| Network Attached Storage (NAS) Devices  Advantage Concepts |  |  |  |  |

Advantage Database Server provides support for Network Attached Storage (NAS) devices through the [server-side alias](master_server_side_aliases.md) functionality. If a NAS device can be accessed via a Universal Naming Convention (UNC) path from the server that is hosting Advantage Database Server, then the NAS device can be used as the storage location for the Advantage data.

Note that server-side aliasing can also be used for Storage Area Network (SAN) solutions although SANs typically are implemented such that they appear to be local devices on the server itself. If this is the case, then no special aliasing is typically required to access the data. But, if the SAN is not viewable as a share on the server, server-side aliases can be used to provide access to the data.

To access data on a NAS device:

- Define a [server-side alias](master_server_side_aliases.md) that points to the NAS device, and use the alias in place of a share name in all paths in your application.

- Turn off [rights checking](master_database_security.md). When using server-side aliasing to access NAS data, the path is meaningless to the client. If rights checking is turned on, you will get 5004 errors.

Example

Suppose Advantage Database Server is running on a server named ADSServer and data is located on a NAS device accessible via the UNC name \\mynas\adsdata. Define an alias in adsserver.ini such as:

[ServerAliases]

NASData=\\mynas\adsdata

 

Then, in your application, you can use "NASData" as you would any share accessible to Advantage Database Server. For example, you can connect to \\ADSServer\NASData\appdata1\mydata.add and then execute SQL statements on that connection or open tables directly. When accessing tables directly in a free connection), use the alias that points to the NAS data just like you do for the connection path; include the name as the share name (e.g., \\ADSServer\NASData\appdata1\table.adt).

Note that the server-side alias can include path information if you do not want to include the additional path information in the client application. For example, the alias could be defined as:

[ServerAliases]

NASData=\\mynas\adsdata\appdata1

 

Then the connection path equivalent to the above example would be \\ADSServer\NASData\mydata.add.

Performance and Data Integrity

Because NAS implementations typically are file-based and use standard networking protocols to read and write data, performance will generally not be as good as when the data is stored on a local drive on the server. Each physical data request will go through the IP stack and the NIC on the server. Advantage Database Server has high performance caching algorithms that can significantly reduce this traffic, however, all table updates are written immediately to maintain data integrity, so the cost will always be greater than when using a disk that is local to the server.

It is also important to note that the reliability of the data stored on a NAS device is dependent on the reliability of the network connection between the server and the NAS device. If the connection is lost, then data corruption can occur.

Limitations

- This functionality relies on server-side aliases, which are only available on Advantage Database Server.

- [Rights checking](master_database_security.md) must be turned off in order to use this functionality.

- When using free connections), table lists will not be returned to the client. Generating a list of tables for free connections is client-side functionality, and a connection path that includes a server-side alias means nothing to the client software. If you use a database connection), your application can retrieve table lists.
