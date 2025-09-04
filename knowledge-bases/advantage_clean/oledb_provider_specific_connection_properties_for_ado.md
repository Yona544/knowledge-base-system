---
title: Oledb Provider Specific Connection Properties For Ado
slug: oledb_provider_specific_connection_properties_for_ado
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_provider_specific_connection_properties_for_ado.htm
source: Advantage CHM
tags:
  - oledb
checksum: b8f319072bdfbcce1941587b95e81935ab6f1e22
---

# Oledb Provider Specific Connection Properties For Ado

Provider-Specific Connection Properties for ADO

Provider-Specific Connection Properties for ADO

Advantage OLE DB Provider (for ADO)

| Provider-Specific Connection Properties for ADO  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property sets DBPROPSET\_ADSDATASOURCEINFO and DBPROPSET\_ADSSESSIONINFO can be accessed from ADO Connection objects once a connection to Advantage has occurred. For details and valid values for each property, see [Provider-Specific Data Source Information Properties](oledb_provider_specific_data_source_information_properties.md) and Provider-Specific Session Properties. The following is the mapping between the "friendly" property name and the property ID.

| Property ID | Property Name |
| ADSPROP\_CONNECTION\_HANDLE | ACE Connection Handle |
| ADSPROP\_ENFORCE\_AUTOINC | Enforce AutoInc |
| ADSPROP\_ENFORCE\_UNIQUE\_INDEX | Enforce Unique Index |
| ADSPROP\_ENFORCE\_RI | Enforce RI |

After a connection has been made to the Advantage OLE DB provider, the value for these properties can be retrieved from the Connection properties collection. For example:

Dim cn As ADODB.Connection

Set cn = New ADODB.Connection

cn.Provider = "Advantage.OLEDB.1"

cn.Properties.Item("Data Source") = "\\server\volume\path"

cn.Open

lHandle = cn.Properties.Item("ACE Connection handle")

lResult = AdsInTransaction( lHandle, bInTrans ) This returns whether the application is currently in a transaction

 

'Allow writing of any data to auto-increment fields

cn.Properties.Item("Enforce AutoInc") = False
