---
title: Ace Adssetaof
slug: ace_adssetaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 78d53ff84f80780da26776270a646a84b99f86f7
---

# Ace Adssetaof

AdsSetAOF

AdsSetAOF / AdsSetAOF100

Advantage Client Engine

| AdsSetAOF / AdsSetAOF100  Advantage Client Engine |  |  |  |  |

Create an Advantage Optimized Filter (AOF) for the given table

Syntax

| UNSIGNED32 | AdsSetAOF ( ADSHANDLE hTable,             UNSIGNED8 \*pucFilter,             UNSIGNED16 usOptions ); |
| UNSIGNED32 | AdsSetAOF100( ADSHANDLE hTable,               VOID       \*pvFilter,               UNSIGNED32 ulOptions ); |

Parameters

| hTable (I) | Handle of a table or cursor to set the filter on. |
| pucFilter (I) | Null terminated ANSI/OEM code page encoded filter expression. |
| pvFilter (I) | Null terminated Filter expression that is encoded based on the ulOptions. |
| usOptions (I) | Option to indicate how the filter should be resolved in the event that the expression cannot be fully optimized. This flag is also used to indicate how filter membership is affected by data changes. Options are ADS\_RESOLVE\_IMMEDIATE, ADS\_RESOLVE\_DYNAMIC, ADS\_DYNAMIC\_AOF, ADS\_KEYSET\_AOF, and ADS\_FIXED\_AOF. |
| ulOptions (I) | Option to indicate how the filter should be resolved and how the filter expression is encoded. In addition to the options allowed in the usOptions, the following options are supported:    ADS\_ENCODE\_UTF8: The string specified by pvFilter is encoded in UTF8. This option is mutually exclusive with the ADS\_ENCODE\_UTF16.    ADS\_ENCODE\_UTF16: The string specified by pvFilter is encoded in UTF-16LE. This option is mutually exclusive with the ADS\_ENCODE\_UTF8.    If neither of the encoding options is specified, the pvFilter should be encoded in ANSI/OEM code page. |

Remarks

AdsSetAOF and AdsSetAOF100 create an Advantage Optimized Filter on the given table using all currently open indexes. Filters created on tables opened with the ADS\_NTX option will not be optimized; only filters created on ADS\_CDX, ADS\_VFP or ADS\_ADT tables will be optimized. The ADS\_RESOLVE\_IMMEDIATE option causes the server to immediately remove all records from the result set that do not pass the filter if it cannot be fully optimized. This means it must evaluate the expression for every record that is potentially in the result set to determine membership conclusively. The ADS\_RESOLVE\_DYNAMIC option causes the server to determine membership as the data is read by the client (e.g., from a browse).

The benefit to using ADS\_RESOLVE\_IMMEDIATE is that a more "accurate" record count is returned and can be retrieved via AdsGetRecordCount. In addition, once the full resolution has been done, the server does not have to evaluate the expression on any subsequent record movements. The drawback to the immediate resolution is the extra time needed to perform the resolution. With dynamic resolution, records are removed from the filter as the client requests record movement. This means that the resolution time can be spread out through a browse of the data, and the elapsed time for the resolution will not be noticed. Also, a skip (browse) through the entire data set will remove all records from the filter that do not meet the condition. A second pass through the data, then, will not require those records to be evaluated. In general, it is better to use dynamic resolution for most applications.

The usOptions or ulOptions parameter is a multi-purpose option flag used to specify both the resolution type and the AOF type.

Resolution Types:

ADS\_RESOLVE\_IMMEDIATE

ADS\_RESOLVE\_DYNAMIC

AOF Types:

ADS\_DYNAMIC\_AOF

ADS\_KEYSET\_AOF

ADS\_FIXED\_AOF

The resolution portion of the options flag is required. If an AOF type is not specified, ADS\_DYNAMIC\_AOF will be assumed.

Different AOF types provide different levels of filter membership.

- Dynamic AOFs: Filter membership is affected by modifications all users make to record data. Dynamic filters are only supported when connected to the Advantage Database Server. If using the Advantage Local Server, dynamic filters will behave like keyset filters.

- Keyset-Driven AOFs: Filter membership is only affected by updates from the filter owner (the table instance that set the filter). Updates made by other users will not affect a records membership in the filter.

- Fixed AOFs: Filter membership does not change. If other users modify records they will always remain visible within this fixed filter, even if the changes have modified field values such that the record no longer passes the original filter expression.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example #1

[Click Here](ace_aof_and_encryption_examples.md#adssetaof_example)

Example #2

AdsSetAOF( hTable, "lastname > Anderson", ADS\_RESOLVE\_IMMEDIATE | ADS\_FIXED\_AOF );

See Also

[AdsClearAOF](ace_adsclearaof.md)

[AdsRefreshAOF](ace_adsrefreshaof.md)

[AdsGetAOF](ace_adsgetaof.md)

[AdsGetAOF100](ace_adsgetaof.md)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.md)

[AdsEvalAOF](ace_adsevalaof.md)

[AdsEvalAOF100](ace_adsevalaof.md)

[AdsSetFilter](ace_adssetfilter.md)
