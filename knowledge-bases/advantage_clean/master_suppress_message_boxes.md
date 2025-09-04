---
title: Master Suppress Message Boxes
slug: master_suppress_message_boxes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_suppress_message_boxes.htm
source: Advantage CHM
tags:
  - master
checksum: 2416ece23963914fbb4699e5cab8a998fc9d95e3
---

# Master Suppress Message Boxes

Suppress Message Boxes

Suppress Message Boxes

Advantage Database Server

| Suppress Message Boxes  Advantage Database Server |  |  |  |  |

Default = 0

If the SUPPRESS\_MESSAGE\_BOXES configuration parameter is set to a non-zero value, then the Advantage Database Server will not display error message boxes caused by startup errors, exceptions, or shutdown errors. For example, when a request is made to shut down Advantage Database Server while it has active connections, it will, by default, prompt with a Yes/No message box asking if that is desired. If this configuration parameter has a non-zero value, then the server will log an entry to the application event log and silently shut down. This may be useful in a clustered environment where the cluster manager is responsible for starting and stopping Advantage Database Server automatically without human interaction.

Note This parameter is only applicable to Advantage Database Server for Windows.
