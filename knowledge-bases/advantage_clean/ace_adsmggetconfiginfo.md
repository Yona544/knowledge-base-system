---
title: Ace Adsmggetconfiginfo
slug: ace_adsmggetconfiginfo
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmggetconfiginfo.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 45c8bb2bb5b06cf5ad939aa6aec89350ffb5e1b9
---

# Ace Adsmggetconfiginfo

AdsMgGetConfigInfo

AdsMgGetConfigInfo

Advantage Client Engine

| AdsMgGetConfigInfo  Advantage Client Engine |  |  |  |  |

Returns Advantage Database Server configuration information

Syntax

| UNSIGNED32 | AdsMgGetConfigInfo ( ADSHANDLE hMgmtConnect,  ADS\_MGMT\_CONFIG\_PARAMS \*pstConfigValues,  UNSIGNED16 \*pusConfigValuesStructSize,  ADS\_MGMT\_CONFIG\_MEMORY \*pstConfigMemory,  UNSIGNED16 \*pusConfigMemoryStructSize ); |

Parameters

| hMgmtConnect (I) | Management API connection handle of server to get configuration information. |
| pstConfigValues (O) | Returned configuration parameter value structure. |
| pusConfigValueStructSize (I/O) | Size (in bytes) of pstConfigValues structure on input. On output, size (in bytes) of data returned. |
| pstConfigMemory (O) | Returned configuration parameter memory structure. |
| pusConfigMemoryStructSize (I/O) | Size (in bytes) of pstConfigMemory structure on input. On output, size (in bytes) of data returned. |

Remarks

When the Advantage Database Server is started/loaded, several values are available to be configured to fine tune the use of the Advantage Database Server. Many of these configurable parameters affect how much server memory is used when the Advantage Database Server is started/loaded. The remaining configurable parameters affect other non-memory Advantage features. AdsMgGetConfigInfo returns two structures. The first, pstConfigValues, contains the current settings of all Advantage Database Server configuration parameters. The second, pstConfigMemory, contains the memory taken up by the applicable configuration parameters. Each pstConfigMemory structure data member contains the total memory (in bytes) taken up for each setting. To determine how much memory is required per setting, divide the memory size by the number configured.

Since it is possible that the size of the ADS\_MGMT\_CONFIG\_PARAMS and/or ADS\_MGMT\_CONFIG\_MEMORY structures will increase in future releases of Advantage, it is highly recommended that on input the pusConfigValueStructSize and pusConfigMemoryStructSize parameters are literally initialized with sizeof( ADS\_MGMT\_CONFIG\_PARAMS ) and sizeof( ADS\_MGMT\_CONFIG\_MEMORY ), respectively, rather than being initialized with literal values.

Note With the Advantage Local Server, AdsMgGetConfigInfo will only return information for the instance of Advantage Local Server currently loaded into memory.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmggetconfiginfo_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[ADS\_MGMT\_CONFIG\_PARAMS](ace_ads_mgmt_config_params.md)

[ADS\_MGMT\_CONFIG\_MEMORY](ace_ads_mgmt_config_memory.md)
