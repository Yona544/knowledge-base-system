---
title: Ace Adsdisableri
slug: ace_adsdisableri
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdisableri.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 77e9c059302cacb6fcc5b99cda12d2286e6b9fc9
---

# Ace Adsdisableri

AdsDisableRI

AdsDisableRI

Advantage Client Engine

| AdsDisableRI  Advantage Client Engine |  |  |  |  |

Disables referential integrity (RI) enforcement for record insertions and updates.

Syntax

UNSIGNED32 AdsDisableRI( ADSHANDLE hConnection );

Parameters

| hConnection (I) | Connection handle. |

Remarks

AdsDisableRI can be used to temporarily disable referential integrity constraints on the database.

Note Disabling referential integrity constraints can lead to logical data corruption. This API should be used with extreme caution.

See Also

[AdsEnableRI](ace_adsenableri.md)

[AdsDisableUniqueEnforcement](ace_adsdisableuniqueenforcement.md)

[AdsEnableUniqueEnforcement](ace_adsenableuniqueenforcement.md)

[AdsDisableAutoIncEnforcement](ace_adsdisableautoincenforcement.md)

[AdsEnableAutoIncEnforcement](ace_adsenableautoincenforcement.md)
