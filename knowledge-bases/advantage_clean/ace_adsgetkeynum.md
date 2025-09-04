---
title: Ace Adsgetkeynum
slug: ace_adsgetkeynum
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetkeynum.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0494e09782eae84d6a717abbc00670904e812495
---

# Ace Adsgetkeynum

AdsGetKeyNum

AdsGetKeyNum

Advantage Client Engine

| AdsGetKeyNum  Advantage Client Engine |  |  |  |  |

Retrieves the logical key number of the current record with respect to the given index order.

Syntax

| UNSIGNED32 | AdsGetKeyNum (ADSHANDLE hIndex,  UNSIGNED16 usFilterOption,  UNSIGNED32 \*pulKey); |

Parameters

| hIndex (I) | Handle of index order. |
| usFilterOption (I) | Indicates if filters and/or scopes are to be respected (if they are set). Options are ADS\_RESPECTFILTERS, ADS\_RESPECTSCOPES, and ADS\_IGNOREFILTERS. Using ADS\_RESPECTFILTERS respects filters and scopes. Using ADS\_RESPECTSCOPES respects scopes only. Using ADS\_IGNOREFILTERS will ignore filters and scopes. |
| pulKey (O) | Return the logical record number. This is set to 0 if there is no current record (e.g., at eof) or if the current record is outside of the scope or filter. |

Remarks

The first record in the index is logical record 1.

If usFilterOption contains ADS\_IGNOREFILTERS or ADS\_RESPECTSCOPES, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because index keys are literally counted until the current key is reached.

If usFilterOption contains ADS\_RESPECTFILTERS, the Advantage Client Engine must skip through all records referenced by keys in the index that pass the filter and/or scope and count them until the current key is reached. Thus, with large indexes where many records pass the filter and/or keys pass the scope, this function can be very slow.

Example

[Click Here](ace_examples.md#adsgetkeynumexample)

See Also

[AdsGetRecordNum](ace_adsgetrecordnum.md)
