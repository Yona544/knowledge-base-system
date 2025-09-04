---
title: Ace Adsmgresetcommstats
slug: ace_adsmgresetcommstats
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmgresetcommstats.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ba0478d1a5bd483157ebe34fd8202195fa24b278
---

# Ace Adsmgresetcommstats

AdsMgResetCommStats

AdsMgResetCommStats

Advantage Client Engine

| AdsMgResetCommStats  Advantage Client Engine |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero

Syntax

| UNSIGNED32 | AdsMgResetCommStats ( ADSHANDLE hMgmtConnect ); |

Parameters

| hMgmtConnect (I) | Management API connection handle of server to reset communication statistics. |

Remarks

AdsMgResetCommStats resets all Advantage Database Server communication statistics to zero. This function is useful when used in conjunction with AdsMgGetCommStats to determine how often corrupted packets are being discovered.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmgresetcommstats_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[AdsMgGetCommStats](ace_adsmggetcommstats.md)

[ADS\_MGMT\_COMM\_STATS](ace_ads_mgmt_comm_stats.md)
