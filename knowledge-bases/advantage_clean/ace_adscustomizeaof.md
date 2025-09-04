---
title: Ace Adscustomizeaof
slug: ace_adscustomizeaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscustomizeaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 890ec369553c9c23e234cadba2667441aabaebf6
---

# Ace Adscustomizeaof

AdsCustomizeAOF

AdsCustomizeAOF

Advantage Client Engine

| AdsCustomizeAOF  Advantage Client Engine |  |  |  |  |

Add records to or remove records from an existing Advantage Optimized Filter (AOF).

Syntax

| UNSIGNED32 | AdsCustomizeAOF (ADSHANDLE hTable,  UNSIGNED32 ulNumRecs,  UNSIGNED32 \*pulRecords,  UNSIGNED16 usOption); |

Parameters

| hTable (I) | Handle of table or cursor with existing AOF to customize. |
| ulNumRecs (I) | Number of records to customize. The maximum number of records that can be customized in a single call is 16,383. |
| pulRecords (I) | Array of record numbers to add to or remove from the AOF. |
| usOption (I) | Determines whether the specified records are added to or removed from the AOF. The valid options are ADS\_AOF\_ADD\_RECORD, ADS\_AOF\_REMOVE\_RECORD, or ADS\_AOF\_TOGGLE\_RECORD. |

Remarks

AdsCustomizeAOF provides the capability to add records to or remove records from an Advantage Optimized Filter (AOF). This can be useful for creating filtered record sets that cannot be defined through the use of a filter expression. Calls to AdsCustomizeAOF must be made after an application has created a filter with a call to AdsSetAOF. To create a completely empty record set (to which records can be added with calls to AdsCustomizeAOF), use ".F." as the filter expression given to AdsSetAOF. To create a completely full record set (from which records can be removed), use ".T." as the filter expression.

If an application must use a filter expression that is not fully optimized as the starting point for customization, the ADS\_RESOLVE\_IMMEDIATE option should be used with the call to AdsSetAOF. Otherwise, the dynamic filter resolution that occurs on the server will automatically remove records that have been added through the AdsCustomizeAOF calls. It is probably best to use fully optimized AOFs as the starting point for customization. The filter expressions ".T." and ".F." both result in fully optimized AOFs regardless of available indexes.

Once an application customizes an AOF, the server will not update the bitmap in response to record updates. For example, suppose an AOF such as "married = .T." is set. If the AOF has not been customized, then the server will remove a record from the AOF bitmap if the record is updated with the 'married' field set to .F. This is done in order to keep the AOF bitmap consistent with the record data. If, however, the AOF has been customized, then the server will not change the bitmap when the record is updated. Note that if you do not use the ADS\_RESOLVE\_IMMEDIATE option when creating the AOF, Advantage Database Server will still dynamically resolve the AOF as it reads records even if the AOF has been customized.

Be aware that each call to AdsCustomizeAOF results in a server request because the Advantage Optimized Filters are handled on the server. The work performed on the server to resolve each request is minimal, but the network can be a bottleneck if large numbers of calls are made.

If an application needs different customized AOFs on a single table simultaneously, it is possible to open the table multiple times and create a different filter on each different table handle.

Note that a call to AdsRefreshAOF will rebuild the original filter and will remove customizations to the filter.

Example

[Click Here](ace_aof_and_encryption_examples.md#adscustomizeaof_example)

See Also

[AdsSetAOF](ace_adssetaof.md)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.md)

[AdsIsRecordInAOF](ace_adsisrecordinaof.md)
