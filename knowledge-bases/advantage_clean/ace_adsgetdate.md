---
title: Ace Adsgetdate
slug: ace_adsgetdate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetdate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0786bd307ba47774f8dc464dd67bd69aa51c0e80
---

# Ace Adsgetdate

AdsGetDate

AdsGetDate

Advantage Client Engine

| AdsGetDate  Advantage Client Engine |  |  |  |  |

Retrieves the date value from the given field formatted according to the format defined by AdsSetDateFormat.

Syntax

| UNSIGNED32 | AdsGetDate (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucBuf,  UNSIGNED16 \*pusLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pucBuf (O) | Return field in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetDate returns dates according to the date format set in [AdsSetDateFormat](ace_adssetdateformat.md). It can be used to retrieve dates from date fields, short date fields, ModTime fields, and the date portion of timestamp fields.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_examples.md#adsgetdateexample)

See Also

[AdsSetDate](ace_adssetdate.md)

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsSetField](ace_adssetfield.md)

[AdsGetJulian](ace_adsgetjulian.md)

[AdsGetTime](ace_adsgettime.md)
