---
title: Ace Adssetfilter
slug: ace_adssetfilter
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetfilter.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 413bba8e79e8f9ecd957b4d4476c875eb5d45e4d
---

# Ace Adssetfilter

AdsSetFilter

AdsSetFilter / AdsSetFilter100

Advantage Client Engine

| AdsSetFilter / AdsSetFilter100  Advantage Client Engine |  |  |  |  |

Sets a filter on the given table

Syntax

| UNSIGNED32 | AdsSetFilter ( ADSHANDLE hTable,                UNSIGNED8 \*pucFilter); |
| UNSIGNED32 | AdsSetFilter100( ADSHANDLE hTable,                  VOID        \*pvFilter                  UNSIGNED32  ulOptions ); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFilter (I) | Filter expression given as a null terminated ANSI/OEM code page encoded string. If there is an existing filter on the given table, it is replaced with the new filter. This affects subsequent record movements other than AdsGotoRecord. |
| pvFilter (I) | Filter expression given as a null terminated string that is encoded based on the ulOptions. |
| ulOptions (I) | This is a bit field for defining the options for the filter. The options are:    ADS\_ENCODE\_UTF8: The string specified by pvFilter is encoded in UTF8. This option is mutually exclusive with the ADS\_ENCODE\_UTF16 option.    ADS\_ENCODE\_UTF16: The string specified by pvFilter is encoded in UTF-16LE. This option is mutually exclusive with the ADS\_ENCODE\_UTF8 option. |

Remarks

Setting a filter through AdsSetFilter  or AdsSetFilter100 allows only the records that pass the filter expression to be visible. The filter expression must result in a boolean True or False. After setting a filter, the table may still be positioned on a record that does not pass the filter. To activate the filter, perform an [AdsGotoTop](ace_adsgototop.md) or some other movement function.

For AdsSetFilter100, if neither ADS\_ENCODE\_UTF8 nor ADS\_ENCODE\_UTF16 is specified in the ulOptions, the pvFilter should be encoded using ANSI/OEM code page of the table.

See [Advantage Expression Engine](master_advantage_expression_engine.md) for a list of functions supported by the Advantage Expression Engine.

AdsSetFilter and AdsSetFilter100 do not utilize the Advantage Optimized Filters functionality. It is recommended you use the [AdsSetAOF](ace_adssetaof.md) or [AdsSetAOF100](ace_adssetaof.md) function.

Example

[Click Here](ace_examples.md#adssetfilterexample)

See Also

[AdsGetFilter](ace_adsgetfilter.md)

[AdsClearFilter](ace_adsclearfilter.md)

[AdsSetAOF](ace_adssetaof.md)

[AdsSetAOF100](ace_adssetaof.md)
