---
title: Master Server Side Aliases
slug: master_server_side_aliases
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_server_side_aliases.htm
source: Advantage CHM
tags:
  - master
checksum: 39cd2b7e4e230102688d363ee75d110f2dd33ca4
---

# Master Server Side Aliases

Server-Side Aliases

Server-Side Aliases

Advantage Concepts

| Server-Side Aliases  Advantage Concepts |  |  |  |  |

Traditionally, Advantage has only supported client-side aliases via entries in the ads.ini file. While convenient, these aliases must exist on every client machine using your application, and they can also pose a security risk if you do not want the path to your data to be visible.

Server-side aliases not only hide the path to your data, but they also allow you to remove all Windows shares and still connect to your Advantage data. This functionality provides increased security and convenience.

Server-side aliases also allow you to connect to data that is not located on the same server that the Advantage Database Server is running on. For details, see the [Network Attached Storage Support](master_network_attached_storage_nas_devices.md) topic.

Server-side aliases are supported on the Windows and Linux platforms. However, the Advantage Local Server does not support server-side aliases.

Configuration

Server-side aliases must be placed in a file called adsserver.ini. This file does not exist by default. Create the file using any text editor. The Advantage server uses the error log path configuration value to locate the adsserver.ini file (the default value is c:\).

An example adsserver.ini file with three aliases:

[ServerAliases]

order\_db=c:\data\orders

bikes=\\server1\shared\_drive\data

flights\_db=c:\data

 

The server-side aliases are in an ini section called [ServerAliases]. Each entry includes the alias name, followed by an equal sign, followed by the path to use when replacing the alias name.

The alias path can be a path including a local drive letter or it can be a Universal Naming Convention (UNC) path. Mapped network drive letters are not supported, and should not be used. Note that when specifying aliases on Linux servers, local filesystem paths or local mount-point paths should always be used, instead of UNC.

Server-side aliases are cached, but changes made to the adsserver.ini file will be automatically detected by the Advantage Database Server. You do not need to restart Advantage to reflect alias changes. If the adsserver.ini file is updated, there may be a lag of up to 10 seconds before the new alias changes are recognized.

Usage

To use a server-side alias, simply reference the alias name where you would normally reference a file share in your connection path.

For example, if your connection string would normally be \\myserver\myshare\mydatadir, to use the "alias\_test" alias, you would change your connection path to \\myserver\alias\_test\mydatadir.

The "share" name in your connection path will be replaced with whatever path you provided for the alias in the adsserver.ini file.

Server-side aliases must always be used in conjunction with the "Ignore Rights" setting of your Advantage client. See the [Database Security](master_database_security.md) topic for details. Failure to do so will result in file existence checks, which will use the server-side alias from the client and fail, resulting in AE\_FILE\_NOT\_FOUND (5004) errors.

Server Discovery

The [AdsFindServers](ace_adsfindservers.md) API can be used in conjunction with a server-side alias to provide a convenient way to build the UNC path requiring little to no end user interaction.

\_\_rootdd System Alias

The \_\_rootdd system alias is an alias provided by the Advantage server that resolves to the path of the [root dictionary](master_root_dictionary.md) configured on the server.  Any connections using this alias will be dictionary connections to the root dictionary requiring valid user credentials.  Simply provide the server name (and port if necessary) followed by the \_\_rootdd alias for any connection path.  For example:

 \\server:port\\_\_rootdd

An example connection string would be:

 Data Source=\\server:port\\_\_rootdd; UserID=AdsSys; Password=secret; CommType=TCP\_IP;
