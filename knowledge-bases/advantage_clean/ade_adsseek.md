---
title: Ade Adsseek
slug: ade_adsseek
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsseek.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c325ccbc925a44238c4b1f4147027073ad529a85
---

# Ade Adsseek

AdsSeek

TAdsTable.AdsSeek

Advantage TDataSet Descendant

| TAdsTable.AdsSeek  Advantage TDataSet Descendant |  |  |  |  |

Performs an indexed search on the given table using the given index order. Scopes and filters are respected.

Syntax

type TAdsSeekTypes = ( stSOFT, stHARD );

 

function AdsSeek( strKey : String; eSeekTypes : TAdsSeekTypes ) : Boolean;

Parameter

| strKey | Search key. |
| eSeekTypes | Indicates if hard or soft seek is performed. Options are stSOFT or stHARD. Use of soft seek allows a record to be found with the next higher key value if the given key does not exist. |

CAUTION The AdsSeek method is not any slower nor any less efficient than the native Delphi equivalent FindKey and FindNearest methods. But in nearly every single situation, the native Delphi methods FindKey and FindNearest are easier to use. It is recommended that the Advantage extended method AdsSeek only be used when absolutely necessary. See your Delphi documentation for more information about the FindKey and FindNearest Delphi methods.

Description

AdsSeek provides the fastest way for the Advantage Database Server to locate a record. The strKey parameter is used by the Advantage Client Engine to build a seekable index key for the server to seek through the indicated index for a matching key. If the strKey string is shorter than the keys within the index, only the portion of the key that is the exact length of strKey is checked. For example, if strKey="Sm" it would find the first key in the index starting with "Sm" such as "Smithers".

To seek for records using indexes built on date, time, or timestamp fields, the date and time values must be formatted as text. The date should be formatted according to [DateFormat](ade_dateformat.md). For example, to seek on a date index, an application might pass "2/25/1997" as the seek key. To seek on a timestamp index, the seek key could be "2/25/1997 3:25pm".

By sending stSOFT for the eSeekType parameter, the Advantage Client Engine will perform a "soft" seek, which means that if the desired key is not found in the index, the table will be positioned at the first key logically greater than the seek key. On an stHARD, if the desired key is not found, the table is positioned at EOF.

On a seek that is successful, the value returned from the function will be True. If the seek fails, the value returned from the function will be False. On a "soft" seek, the value returned from the function will be True when the specified key is found. If the specified key is not found on a "soft" seek, the value returned from the function will be False.

Example

{ one field index on a string value }

AdsTable1.FindKey( [Smith] );

{ one field index on an integer value }

AdsTable1.FindKey( [ 14 ] );

{ 4 field index on a string value, an integer value, a boolean value, and a date }

AdsTable1.FindKey( [Smith, 15, TRUE, 10/21/80 ] );

See Also

[AdsClearScope](ade_adsclearscope.md)

[AdsGetScope](ade_adsgetscope.md)

[AdsSetScope](ade_adssetscope.md)

[AdsSkip](ade_adsskip.md)

[AdsLookupKey](ade_adslookupkey.md)
