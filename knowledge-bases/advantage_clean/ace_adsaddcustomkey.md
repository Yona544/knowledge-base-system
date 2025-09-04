---
title: Ace Adsaddcustomkey
slug: ace_adsaddcustomkey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsaddcustomkey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ef44b5292b6d1455617e50d08fce3a5f4beabf48
---

# Ace Adsaddcustomkey

AdsAddCustomKey

AdsAddCustomKey

Advantage Client Engine

| AdsAddCustomKey  Advantage Client Engine |  |  |  |  |

Adds a key built on the current record to the custom index order.

Syntax

| UNSIGNED32 | AdsAddCustomKey (ADSHANDLE hIndex); |

Parameters

| hIndex (I) | Handle of index order that was created with the ADS\_CUSTOM option. |

Remarks

Custom indexes are empty when created and require keys to be explicitly added and removed. AdsAddCustomKey will add a key based on the current record to the custom index order. This key will be updated if the values in the record change.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

Note When the index is shared, adding a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be added even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

[Click Here](ace_examples.md#adsaddcustomkeyexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsIsIndexCustom](ace_adsisindexcustom.md)

[AdsDeleteCustomKey](ace_adsdeletecustomkey.md)

[AdsAtEOF](ace_adsateof.md)
