---
title: Oledb Command Parameters
slug: oledb_command_parameters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_command_parameters.htm
source: Advantage CHM
tags:
  - oledb
checksum: 26116a6db5beefcd5caa2f564127cb16804bfa55
---

# Oledb Command Parameters

Command Parameters

Command Parameters

Advantage OLE DB Provider (for ADO)

| Command Parameters  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Parameters are marked in command text with the ODBC-specified question mark character. For example, the following ODBC SQL statement is marked for a single input parameter:

 

SELECT \* FROM production WHERE product\_id = ?

 

To improve performance by reducing network traffic, the Advantage OLE DB Provider does not automatically derive parameter information. This means that the Advantage OLE DB Provider does not automatically perform the following actions:

•   Verify the correctness of the data type specified with ICommandWithParameters::SetParameterInfo.

- Map from the DBTYPE specified in the accessor binding information to the correct the Advantage Database Server data type for the parameter.

Applications will receive possible errors or loss of precision with either of these methods if they specify data types that are not compatible with the Advantage Database Server data type of the parameter.

To ensure this does not happen, the application should do the following:

- If hard-coding ICommandWithParameters::SetParameterInfo, ensure that pwszDataSourceType matches the Advantage Database Server data type for the parameter.

- If hard-coding an accessor, ensure that the DBTYPE value being bound to the parameter is of the same type as the Advantage Database Server data type for the parameter.

The Advantage OLE DB Provider only supports input parameters in SQL statement commands. Output parameters are not supported.
