---
title: Oledb Selecting Advantage Server Types Via The Servertype Property
slug: oledb_selecting_advantage_server_types_via_the_servertype_property
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_selecting_advantage_server_types_via_the_servertype_property.htm
source: Advantage CHM
tags:
  - oledb
checksum: 41dab7c0249f5e65b3d7e81aa21f1383ab0bccfd
---

# Oledb Selecting Advantage Server Types Via The Servertype Property

Selecting Advantage Server Types via the ServerType Property

Selecting Advantage Server Types via the ServerType Property

Advantage OLE DB Provider (for ADO)

| Selecting Advantage Server Types via the ServerType Property  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage ServerType property that can be specified in the ADO connection string, in the OLE DB Provider String property, or via the ADSPROP\_INIT\_SERVER\_TYPE property allows you to specify which Advantage server type(s) to use when obtaining an Advantage server connection.

Multiple Advantage server types exist. ADS\_REMOTE\_SERVER refers to the Advantage Database Server, ADS\_AIS\_SERVER refers to the Advantage Internet Server, and ADS\_LOCAL\_SERVER refers to the Advantage Local Server. The default Advantage server types setting is ADS\_REMOTE\_SERVER logically ORed with ADS\_AIS\_SERVER.. If multiple Advantage server types are logically ORed together, the application will attempt to connect to Advantage servers in the following order: ADS\_REMOTE\_SERVER first (if specified), ADS\_AIS\_SERVER next (if specified), and ADS\_LOCAL\_SERVER last (if specified). If either the ADS\_REMOTE\_SERVER connect or the ADS\_AIS\_SERVER connect is successful, the ADS\_LOCAL\_SERVER connect will never be attempted.
