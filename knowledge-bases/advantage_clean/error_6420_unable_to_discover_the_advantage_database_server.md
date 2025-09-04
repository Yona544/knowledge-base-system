---
title: Error 6420 Unable To Discover The Advantage Database Server
slug: error_6420_unable_to_discover_the_advantage_database_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6420_unable_to_discover_the_advantage_database_server.htm
source: Advantage CHM
tags:
  - error
checksum: 979e8101f9f422890397b2bddc5b23ab3173e64b
---

# Error 6420 Unable To Discover The Advantage Database Server

6420 Unable to "discover" the Advantage Database Server

6420 Unable to "discover" the Advantage Database Server

Advantage Error Guide

| 6420 Unable to "discover" the Advantage Database Server  Advantage Error Guide |  |  |  |  |

Problem: The Advantage application was unable to connect to the Advantage Database Server.

Solution: Several problems can cause this error to occur. Some common solutions are listed below. Reference the Advantage Knowledge Base for more detailed descriptions and a more complete list of known error cases.

- Verify the Advantage Database Server is installed and running on the server where the database is located.

- If attempting to use the Advantage Local Server and not the Advantage Database Server, make sure the application's "server types" setting is set to use the Advantage Local Server.

- If using the Native SQL Utility in the Advantage Data Architect, and you desire to use the Advantage Local Server and not the Advantage Database Server, make sure the Advantage connection type is set to "Local (ALS)". This can be done via the Query Options dialog that is accessed by clicking the button that has the screwdriver, hammer, and wrench on it.

- If communicating to a server that only has IPX installed, make sure the Advantage client is enabled to send IPX packets.

- If running through a firewall, make sure the Advantage IP send and receive ports are properly configured and opened up through the firewall.

- If attempting to make a Transport Layer Security (TLS/SSL) connection, the 6420 error may be returned if the server is not enabled for [strong encryption](master_se_usage_overview.md). When attempting discovery for a TLS connection, the client looks specifically for the server port configured for TLS communications. If an error occurred when Advantage Database Server attempted to set up TLS at server startup, the port will not exist.  This can result in a 6420 error at the client. If you have configured the server for TLS communications, check the Advantage error log for errors (e.g., [7163](error_7163_ssl_library_error.md)) at the time the server was started. Verify that the [TLS\_KEY\_FILE](master_tls_key_file.md) configuration parameter is correct.
