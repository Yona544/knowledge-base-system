---
title: Ace Adsgetjulian
slug: ace_adsgetjulian
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetjulian.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 93e39c0f807fe7773da655fbfc6b7682940a7fb7
---

# Ace Adsgetjulian

AdsGetJulian

AdsGetJulian

Advantage Client Engine

| AdsGetJulian  Advantage Client Engine |  |  |  |  |

Retrieves the Julian date representation from the given field.

Syntax

| UNSIGNED32 | AdsGetJulian (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  SIGNED32 \*plDate); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| plDate (O) | Return the date represented as a Julian value. |

Special Return Codes

| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

AdsGetJulian can be used to retrieve the Julian date representation of a date from date, short date, ModTime fields, and timestamp fields. A Julian date is a signed long integer representation of the number of days since January 1, 4713 B.C.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetjulianexample)

See Also

[AdsSetJulian](ace_adssetjulian.md)

[AdsGetDate](ace_adsgetdate.md)
