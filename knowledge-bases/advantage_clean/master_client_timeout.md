---
title: Master Client Timeout
slug: master_client_timeout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_client_timeout.htm
source: Advantage CHM
tags:
  - master
checksum: 2e2c8e67c6a289722c564938642790fdcd3f7fb1
---

# Master Client Timeout

Client Timeout

Client Timeout

Advantage Database Server

| Client Timeout  Advantage Database Server |  |  |  |  |

Default = 120

Note that this parameter is only used if the configuration parameter, [Use Semaphore Files](master_use_semaphore_files.md) is set to zero. The default is zero to indicate that the Client Timeout configuration parameter is to be used as opposed to the Semaphore Connection File Path configuration parameter. See [Semaphore Connection File Path](master_semaphore_connection_file_path.md) for more information.

When an Advantage application calls either an Advantage "connect" API (if available) or opens the first table, it establishes a connection between the application and the Advantage Database Server. The Advantage Database Server needs to ensure that the client application has not aborted its connection to the server. The connection is aborted when the application is abnormally halted. Examples would include a PC being rebooted, a PCs network connection being broken, the application having a GPF or when an application is halted from within a debugger.

The Advantage server determines if a client had died by keeping track of the last communication the server received from the client. If the server has not received a communication in a given time, then the client is disconnected. The timeout delay is 120 seconds by default. The Advantage Client Engine will start a thread that sends "keep alive" packets to the server at given intervals. These packets are only sent if necessary. If the client has had other communications within the interval, then the "keep alive" packet is not sent.

Note that this algorithm is generally an improvement over the Semaphore Connection Files algorithm. The directory specified in the Semaphore Connection Files option must be configured, so that all users have read access to the directory. This inherently leads to problems.

The Client Timeout algorithm has two drawbacks, however. Both issues affect the developer more so than end user. The first is that when an application is halted within the debugger, the keep alive packets are not sent to the server by the second thread, which is also halted. If the application is halted for more than the configured time, which is 120 seconds or 2 minutes by default, the server will abort that applications connection. The second problem is that when the developer aborts an application with a debugger, the connection is left open. The connection will remain open for the configured time. Semaphore connection files resulted in the files being closed quicker.
