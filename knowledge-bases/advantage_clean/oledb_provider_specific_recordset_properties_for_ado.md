---
title: Oledb Provider Specific Recordset Properties For Ado
slug: oledb_provider_specific_recordset_properties_for_ado
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_provider_specific_recordset_properties_for_ado.htm
source: Advantage CHM
tags:
  - oledb
checksum: aa8108c80fd41995f5c23bac174ae1fda5622314
---

# Oledb Provider Specific Recordset Properties For Ado

Provider-Specific Recordset Properties for ADO

Provider-Specific Recordset Properties for ADO

Advantage OLE DB Provider (for ADO)

| Provider-Specific Recordset Properties for ADO  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The provider-specific property set DBPROPSET\_ADSROWSET can be accessed from ADO Recordset objects. For details and valid values for each property, see [Provider-Specific Rowset Properties](oledb_provider_specific_rowset_properties.md).

The following is the mapping between the "friendly" property name and the property ID.

| Property ID | Property Name |
| ADSPROP\_LAST\_AUTOINC | Last AutoInc |
| ADSPROP\_ROWSET\_HANDLE | ACE Recordset Handle |

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.

After a table has been opened directly or a cursor opened by executing an SQL SELECT statement, the value for these properties can be retrieved from the Recordset properties collection. For example:

 

cmd.CommandText = "INSERT INTO table (field1) VALUES ('value1')"

cmd.Execute

LastAutoInc = cmd.Properties.Item("Last AutoInc")

 

rs.Open "customers", , , , adCmdTableDirect

lHandle = rs.Properties.Item("ACE Recordset handle")

lResult = AdsLockRecord( lHandle, 69 ) This allows record 69 in the customers table to be locked directly
