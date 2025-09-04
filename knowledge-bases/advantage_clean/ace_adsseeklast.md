---
title: Ace Adsseeklast
slug: ace_adsseeklast
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsseeklast.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b63d272c28d4db04c3962ec998bc23e6245962d2
---

# Ace Adsseeklast

AdsSeekLast

AdsSeekLast

Advantage Client Engine

| AdsSeekLast  Advantage Client Engine |  |  |  |  |

Seeks for the last value in an index.

Syntax

| UNSIGNED32 | AdsSeekLast (ADSHANDLE hIndex,  UNSIGNED8 \*pucKey,  UNSIGNED16 usKeyLen,  UNSIGNED16 usDataType,  UNSIGNED16 \*pbFound) |

Parameters

| hIndex (I) | Handle of index order. |
| pucKey (I) | Search key (not necessarily a null terminated string). |
| usKeyLen (I) | Length of search key. |
| usDataType (I) | Indicates type of data given in pucKey. ADS\_RAWKEY indicates that the key is given exactly as needed for seek. No conversion is performed. ADS\_STRINGKEY indicates the data is in a character string (numeric date, and ANSI/OEM conversions performed as necessary. ADS\_DOUBLEKEY indicates that the data is a pointer to an 8-byte floating-point value. ADS\_WSTRINGKEY indicates that the data is a pointer to a UTF16 encoded string and the usKeyLen is the number of bytes (not the number of characters) in the string. |
| pbFound (O) | Return True if record found. |

Remarks

AdsSeekLast will perform a seek for the last key in the indicated index order that matches the passed in search key. If the key is not in the index, the function will position the table at EOF and set the found flag to False. A zero length search key is defined to match all index keys and will perform an AdsGotoBottom in the index order indicated by hIndex.

Example

[Click Here](ace_examples.md#adsseeklastexample)

See Also

[AdsSeek](ace_adsseek.md)

[AdsIsFound](ace_adsisfound.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)
