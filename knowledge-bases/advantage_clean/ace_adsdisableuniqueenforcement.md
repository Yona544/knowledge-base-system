---
title: Ace Adsdisableuniqueenforcement
slug: ace_adsdisableuniqueenforcement
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdisableuniqueenforcement.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2234ca70730bbcd7457a199e9391aa9a2e3965e4
---

# Ace Adsdisableuniqueenforcement

AdsDisableUniqueEnforcement

AdsDisableUniqueEnforcement

Advantage Client Engine

| AdsDisableUniqueEnforcement  Advantage Client Engine |  |  |  |  |

Disables unique key enforcement for record insertions and updates.

Syntax

UNSIGNED32 AdsDisableUniqueEnforcement(ADSHANDLE hConnection);

Parameters

| hConnection (I) | Connection handle. |

Remarks

AdsDisableUniqueEnforcement can be used to temporarily disable the maintenance of unique key indexes on all tables associated with the connection.

Note Disabling unique key maintenance can lead to logical data corruption. This API should be used with extreme caution.

See Also

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.md)

[AdsDisableRI](ace_adsdisableri.md)

[AdsEnableRI](ace_adsenableri.md)

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.md)

[AdsEnableAutoIncEnforcement](ace_adsenableautoincenforcement.md)
