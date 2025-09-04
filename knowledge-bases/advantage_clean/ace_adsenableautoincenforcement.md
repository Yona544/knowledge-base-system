---
title: Ace Adsenableautoincenforcement
slug: ace_adsenableautoincenforcement
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsenableautoincenforcement.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 24b280c4af6e7d164c4257f304de96c32a495ff3
---

# Ace Adsenableautoincenforcement

AdsEnableAutoIncEnforcement

AdsEnableAutoIncEnforcement

Advantage Client Engine

| AdsEnableAutoIncEnforcement  Advantage Client Engine |  |  |  |  |

Enables the enforcement of the read/only status of auto-increment values.

Syntax

UNSIGNED32 AdsEnableAutoIncEnforcement( ADSHANDLE hConnect );

Parameters

| hConnect (I) | Valid connection handle. |

Remarks

AdsEnableAutoIncEnforcement restores the default behavior of auto-increment fields on the given connection. By default, auto-increment values are generated and maintained by Advantage. This API is used to re-enable the enforcement of auto-increment values after a call to AdsDisableAutoIncEnforcement.

See Also

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.md)

[AdsDisableUniqueEnforcement](ace_adsdisableuniqueenforcement.md)

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.md)

[AdsDisableRI](ace_adsdisableri.md)

[AdsEnableRI](ace_adsenableri.md)
