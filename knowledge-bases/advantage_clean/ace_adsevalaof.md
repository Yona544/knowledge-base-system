---
title: Ace Adsevalaof
slug: ace_adsevalaof
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsevalaof.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4002e1e616284fc7dc815434f775023d86da2abb
---

# Ace Adsevalaof

AdsEvalAOF

AdsEvalAOF / AdsEvalEOF100

Advantage Client Engine

| AdsEvalAOF / AdsEvalEOF100  Advantage Client Engine |  |  |  |  |

Evaluate a filter expression to determine its optimization level

Syntax

| UNSIGNED32 | AdsEvalAOF ( ADSHANDLE hTable,              UNSIGNED8 \*pucFilter,              UNSIGNED16 \*pusOptLevel ); |
| UNSIGNED32 | AdsEvalAOF100( ADSHANDLE hTable,                VOID       \*pvFilter,                UNSIGNED32 ulOptions,                UNSIGNED16 \*pusOptLevel ); |

Parameters

| hTable (I) | Table or cursor for which the AOF is being considered. |
| pucFilter (I) | ANSI/OEM encoded filter expression to evaluate to determine optimization level. |
| pvFilter (I) | Filter expression that is encoded based on the ulOptions parameter. |
| ulOptions (I) | This is a bit field for defining the options for the filter. The options are:    ADS\_ENCODE\_UTF8: The string specified by pvFilter is encoded in UTF8. This option is mutually exclusive with the ADS\_ENCODE\_UTF16.    ADS\_ENCODE\_UTF16: The string specified by pvFilter is encoded in UTF-16LE. This option is mutually exclusive with the ADS\_ENCODE\_UTF8.    If neither encoding option is specified, the pvFilter is expected to be encoded in ANSI/OEM code page. |
| pusOptLevel (O) | Return optimization level of the given expression. Values are ADS\_OPTIMIZED\_FULL, ADS\_OPTIMIZED\_PART, ADS\_OPTIMIZED\_NONE. |

Remarks

AdsEvalAOF and AdsEvalAOF100 can be used to determine the optimization level of a potential filter expression. It performs the same parsing as AdsSetAOF or AdsSetAOF100 but does not actually build the filter.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.md).

Example

[Click Here](ace_aof_and_encryption_examples.md#adsevalaof_example)

See Also

[AdsSetAOF](ace_adssetaof.md)

[AdsSetAOF100](ace_adssetaof.md)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.md)

[AdsGetAOFOptLevel100](ace_adsgetaofoptlevel.md)
