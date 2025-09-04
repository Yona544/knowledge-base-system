---
title: Ace Adssetmilliseconds
slug: ace_adssetmilliseconds
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetmilliseconds.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3e4f8d4995203459f0d3dd876f9753e149aae8b8
---

# Ace Adssetmilliseconds

AdsSetMilliseconds

AdsSetMilliseconds

Advantage Client Engine

| AdsSetMilliseconds  Advantage Client Engine |  |  |  |  |

Stores the given value representing milliseconds since midnight in the given time or timestamp field

Syntax

| UNSIGNED32 | AdsSetMilliseconds (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  SIGNED32 lTime); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| lTime (I) | Value to store in the time or timestamp field. |

Remarks

AdsSetMilliseconds can be used to set the number of milliseconds since midnight in a time field, ModTime field, or in the time portion of a timestamp field.

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.md) and [AdsBuildRawKey](ace_adsbuildrawkey.md).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE time\_field > :TimeParam" );

AdsSetMilliseconds( hStatement, "TimeParam", 340000 );

AdsExecuteSQL( hStatement, &hCursor);

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE time\_field > :TimeParam" );

AdsSetMilliseconds( hStatement, ADSFIELD(1), 340000 );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_more_examples.md#adssetmillisecondsexample)

See Also

[AdsGetMilliseconds](ace_adsgetmilliseconds.md)

[AdsSetField](ace_adssetfield.md)

[AdsSetTime](ace_adssettime.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)

[AdsPrepareSQL](ace_adspreparesql.md)
