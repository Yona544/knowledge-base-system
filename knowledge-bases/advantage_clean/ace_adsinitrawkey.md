---
title: Ace Adsinitrawkey
slug: ace_adsinitrawkey
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsinitrawkey.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 92b6a5f9ea14a65c156ecb5c257a13a79b2a381e
---

# Ace Adsinitrawkey

AdsInitRawKey

AdsInitRawKey

Advantage Client Engine

| AdsInitRawKey  Advantage Client Engine |  |  |  |  |

Initializes the creation of a raw key that can be used with the ADS\_RAWKEY data type in calls to [AdsSeek](ace_adsseek.md), [AdsSeekLast](ace_adsseeklast.md), [AdsLookupKey](ace_adslookupkey.md), and [AdsSetScope](ace_adssetscope.md).

Syntax

| UNSIGNED32 | AdsInitRawKey(ADSHANDLE hIndex); |

Parameters

| hIndex (I) | Handle of index order. |

Remarks

After calling AdsInitRawKey, make calls to the "AdsSet" APIs to set field values for the key with an hIndex handle instead of the usual hTable handle. After the desired fields have been set, call [AdsBuildRawKey](ace_adsbuildrawkey.md). For example, the following sequence of calls might be used to build a raw seek key for an index built on "lastname+firstname":

ulRet = AdsInitRawKey( hIndex );

ulRet = AdsSetString( hIndex, "lastname", "Adams", 5 );

ulRet = AdsSetString( hIndex, "firstname", "John", 4 );

usKeyLen = sizeof( aucKey );

ulRet = AdsBuildRawKey( hIndex, aucKey, &usKeyLen );

ulRet = AdsSeek( hIndex, aucKey, usKeyLen, ADS\_RAWKEY, ADS\_HARDSEEK, &pbFound);

Note that any fields that are not set, will be "empty". The right-most field that is set determines the actual key length. If in the above example both lastname and firstname fields are 20 characters long, then the key created above would be 24 characters long. If an index is "f1;f2;f3" and only fields f1 and f3 were set, then the final key will include "blanks" for f2.

Example

[Click Here](ace_examples.md#adsinitrawkeyexample)

See Also

[AdsBuildRawKey](ace_adsbuildrawkey.md)

[AdsSeek](ace_adsseek.md)

[AdsSeekLast](ace_adsseeklast.md)

[AdsSetScope](ace_adssetscope.md)

[AdsLookupKey](ace_adslookupkey.md)

[AdsSetDate](ace_adssetdate.md)

[AdsSetDouble](ace_adssetdouble.md)

[AdsSetEmpty](ace_adssetempty.md)

[AdsSetField](ace_adssetfield.md)

[AdsSetJulian](ace_adssetjulian.md)

[AdsSetLogical](ace_adssetlogical.md)

[AdsSetLong](ace_adssetlong.md)

[AdsSetMilliseconds](ace_adssetmilliseconds.md)

[AdsSetRecord](ace_adssetrecord.md)

[AdsSetShort](ace_adssetshort.md)

[AdsSetString](ace_adssetstring.md)

[AdsSetTime](ace_adssettime.md)
