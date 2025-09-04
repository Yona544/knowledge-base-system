---
title: Oledb Provider Specific Session Properties
slug: oledb_provider_specific_session_properties
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_provider_specific_session_properties.htm
source: Advantage CHM
tags:
  - oledb
checksum: 09b24a8071f7f571e5b03df6a1a4b9612dc373f2
---

# Oledb Provider Specific Session Properties

Provider-Specific Session Properties

Provider-Specific Session Properties

Advantage OLE DB Provider (for ADO)

| Provider-Specific Session Properties  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property set DBPROPSET\_ADSSESSIONINFO includes the following property.

| Property ID | Description |
| ADSPROP\_ENFORCE\_AUTOINC | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the read/only status of auto-increment values in tables opened on this session. By default, auto-increment values are generated and maintained by Advantage. If the read/only status of auto-increment fields is disabled with this property, it is possible to write any integer value to an auto-increment field, and Advantage will perform no verification of the uniqueness of auto-increment values. The default value is TRUE. |
| ADSPROP\_ENFORCE\_UNIQUE\_INDEX | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the enforcement of unique indexes on tables opened on this session. The default value is TRUE. |
| ADSPROP\_ENFORCE\_RI | Type: VT\_BOOL  Typical R/W: Read-Write  Description: This property provides the capability to disable (and re-enable) the enforcement of referential integrity rules on tables opened on this session. To set this property, the connection opened by this session must be to an Advantage data dictionary. The default value is TRUE. |
