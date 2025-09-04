---
title: Ace Adsbuildrawkey
slug: ace_adsbuildrawkey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsbuildrawkey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 45c56302c40edc7264cb7abed96a199917be766d
---

# Ace Adsbuildrawkey

AdsBuildRawKey

AdsBuildRawKey / AdsBuildRawKey100

Advantage Client Engine

| AdsBuildRawKey / AdsBuildRawKey100  Advantage Client Engine |  |  |  |  |

Creates a raw key that can be used with the ADS\_RAWKEY data type in calls to [AdsSeek](ace_adsseek.md), [AdsSeekLast](ace_adsseeklast.md), [AdsLookupKey](ace_adslookupkey.md), and [AdsSetScope](ace_adssetscope.md).

Syntax

| UNSIGNED32 | AdsBuildRawKey ( ADSHANDLE hIndex,                  UNSIGNED8 \*pucKey,                  UNSIGNED16 \*pusKeyLen); |
| UNSIGNED32 | AdsBuildRawKey100 ( ADSHANDLE hIndex,                     UNSIGNED8  \*pucKey,                     UNSIGNED16 \*pusKeyLen,                     UNSIGNED32 ulOptions ); |

Parameters

| hIndex (I) | Handle of index order. |
| pucKey (O) | Return key in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |
| ulOptions (I) | Options to determine returned key. The available options are:    ADS\_GET\_DEFAULT\_KEY\_LENGTH return the partial key length based on partial data in the last set segment in the index. This option is same as calling AdsBuildRawKey.    ADS\_GET\_PARTIAL\_FULL\_KEY\_LENGTH return the partial key length as if the last set segment is padded to the full length. This option is useful only when the index expression uses binary concatenation operator, ";" exclusively. If there are other operators in the index expression, then it is not possible to determine the the partial full key length and the result will be the same as AdsBuildRawKey.    ADS\_GET\_FULL\_KEY\_LENGTH return the key length as if all segments of the index are set.    ADS\_GET\_PRIMARY\_WEIGHT\_LENGTH This option is only meaningful if the only set segment is a Unicode column and it is the first segment in the index. For other data types, this option is same as ADS\_GET\_DEFAULT\_KEY\_LENGTH. For Unicode column, the returned key length is the length of the primary weight portion of the key. It is useful for seeking for prefix on Unicode character columns. |

Remarks

AdsBuildRawKey and AdsBuildRawKey100 will build the raw seek key based on the "AdsSet" calls that have been made since the call to [AdsInitRawKey](ace_adsinitrawkey.md) for this index handle.

The key length passed in to AdsBuildRawKey should be the maximum length for the key possible. This can be obtained through a call to [AdsGetKeyLength](ace_adsgetkeylength.md). AE\_INSUFFICIENT\_BUFFER (5005) error may be returned if the buffer size is less than the maximum key length.

The following sequence of calls might be used to build a raw seek key for an index built on "lastname+firstname+mi" or "lastname;firstname;mi":

ulRet = AdsInitRawKey( hIndex );

ulRet = AdsSetString( hIndex, "lastname", "Adams", 5 );

ulRet = AdsSetString( hIndex, "firstname", "John", 4 );

usKeyLen = sizeof( aucKey );

ulRet = AdsBuildRawKey( hIndex, aucKey, &usKeyLen );

ulRet = AdsSeek( hIndex, aucKey, usKeyLen, ADS\_RAWKEY, ADS\_HARDSEEK, &pbFound);

Note that any fields that are not set, will be "empty". The right-most field that is set determines the actual key length.

If in the above example both lastname and firstname fields are 20 characters long and the mi field is one character, and the index uses double byte dynamic collation, and the index expression is "lastname;firstname;mi", then the key created above using AdsBuildRawKey would return key length of 44 bytes. However, if AdsBuildRawKey100 is called using ADS\_GET\_PARTIAL\_FULL\_KEY\_LENGTH option, the returned key length will be 80 bytes. With the ADS\_GET\_FULL\_KEY\_LENGTH option, the returned key length will be 82 bytes.

Example

[Click Here](ace_examples.md#adsbuildrawkeyexample)

See Also

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsSeek](ace_adsseek.md)

[AdsSeekLast](ace_adsseeklast.md)

[AdsSetScope](ace_adssetscope.md)

[AdsLookupKey](ace_adslookupkey.md)

[AdsSetDate](ace_adssetdate.md)

[AdsSetDouble](ace_adssetdouble.md)

[AdsSetEmpty](ace_adssetempty.md)

[AdsSetField](ace_adssetfield.md)

[AdsSetFieldW](ace_adssetfield.md)

[AdsSetJulian](ace_adssetjulian.md)

[AdsSetLogical](ace_adssetlogical.md)

[AdsSetLong](ace_adssetlong.md)

[AdsSetMilliseconds](ace_adssetmilliseconds.md)

[AdsSetRecord](ace_adssetrecord.md)

[AdsSetShort](ace_adssetshort.md)

[AdsSetString](ace_adssetstring.md)

[AdsSetStringW](ace_adssetstring.md)

[AdsSetTime](ace_adssettime.md)
