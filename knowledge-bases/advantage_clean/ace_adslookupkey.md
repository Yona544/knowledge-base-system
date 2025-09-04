---
title: Ace Adslookupkey
slug: ace_adslookupkey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adslookupkey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 15c79dd4680275c9744c4bef216327306ea9e54e
---

# Ace Adslookupkey

AdsLookupKey

AdsLookupKey

Advantage Client Engine

| AdsLookupKey  Advantage Client Engine |  |  |  |  |

Performs an indexed search on the given table using the given index order to determine if a key exists in the index. Scopes and filters are ignored.

Syntax

| UNSIGNED32 | AdsLookupKey (ADSHANDLE hIndex,  UNSIGNED8 \*pucKey,  UNSIGNED16 usKeyLen,  UNSIGNED16 usDataType,  UNSIGNED16 \*pbFound); |

Parameters

| hIndex (I) | Handle of index order. |
| pucKey (I) | Search key (not necessarily a null terminated string). |
| usKeyLen (I) | Length of search key. |
| usDataType (I) | Indicates type of data given in pucKey. ADS\_RAWKEY indicates the key is given exactly as needed for the lookup. No conversion is performed. ADS\_STRINGKEY indicates the data is in a character string (numeric date, and ANSI/OEM conversions performed as necessary. ADS\_DOUBLEKEY indicates that the data is a pointer to an 8-byte floating-point value. ADS\_WSTRINGKEY indicates that the data is a pointer to a UTF16 encoded string and the usKeyLen is the number of bytes (not the number of characters) in the string. |
| pbFound (O) | Return True if the key found. |

Remarks

AdsLookupKey determines if a key exists in the index order. It does not perform any record movement. This function may be used to determine if a key value can be added to a unique index. See [AdsCreateIndex](ace_adscreateindex.md) for information about unique indexes.

Example

[Click Here](ace_more_examples.md#adslookupkeyexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsSeek](ace_adsseek.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)
