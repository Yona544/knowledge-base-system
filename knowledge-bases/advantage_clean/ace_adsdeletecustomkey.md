---
title: Ace Adsdeletecustomkey
slug: ace_adsdeletecustomkey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdeletecustomkey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2592fcdaa241d6771718210a59a31e3955ffb756
---

# Ace Adsdeletecustomkey

AdsDeleteCustomKey

AdsDeleteCustomKey

Advantage Client Engine

| AdsDeleteCustomKey  Advantage Client Engine |  |  |  |  |

Removes the key built from the current record from the custom index order.

Syntax

| UNSIGNED32 | AdsDeleteCustomKey (ADSHANDLE hIndex); |

Parameters

| hIndex (I) | Handle of index order that was created with the ADS\_CUSTOM option. |

Remarks

AdsDeleteCustomKey will remove the key corresponding to the current record from the custom index order. If a key for this record was not added to the index, AdsDeleteCustomKey will return AE\_SUCCESS.

Note When the index is shared, deleting a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be deleted even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

[Click Here](ace_examples.md#adsdeletecustomkeyexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsAddCustomKey](ace_adsaddcustomkey.md)

[AdsIsIndexCustom](ace_adsisindexcustom.md)

[AdsAtEOF](ace_adsateof.md)
