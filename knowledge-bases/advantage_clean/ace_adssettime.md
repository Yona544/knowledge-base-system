---
title: Ace Adssettime
slug: ace_adssettime
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssettime.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f71a7f33ab074063d315a4316b8319344e0a45c6
---

# Ace Adssettime

AdsSetTime

AdsSetTime

Advantage Client Engine

| AdsSetTime  Advantage Client Engine |  |  |  |  |

Stores given time value in the given time or timestamp field

Syntax

| UNSIGNED32 | AdsSetTime (ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucValue,  UNSIGNED16 usLen); |

Parameters

| hObj (I) | Handle of table, cursor, statement, or index order. |
| pucFldName (I) | Name of field to set. |
| pucValue (I) | Time value as a string. |
| usLen (I) | Length of data. |

Remarks

AdsSetTime can be used to set the time value in a time field, ModTime field, or in the time portion of a timestamp field. The time given can be in 12-hour time or 24-hour time format. Valid examples include "12:30 am", "1:45:22 PM", "3:00", and "16:55". In addition, milliseconds can be included if desired. For example "1:30:15.444" represents 5,415,444 milliseconds since midnight. Note that if no "am" or "pm" is included with the time, then it is assumed to be 24-hour time. This means that the value "12:00" is assumed to represent noon (as opposed to midnight).

If the handle passed is an index order handle, the logical record buffer of the index order is modified instead of the table data. The logical record buffer of the index order can be used to build a raw index key in conjunction with calls to [AdsInitRawKey](ace_adsinitrawkey.md) and [AdsBuildRawKey](ace_adsbuildrawkey.md).

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and are one-based. For example, in the statement "INSERT INTO test (lastname, firstname) values (:lname, :fname)" the lname parameter can be referenced either as "lname" or as parameter 1. Likewise, the fname parameter can be referenced either as "fname" or as parameter 2.

If using AdsSetTime to set parameters in an SQL statement the time format is HH:MM:SS or HH:MM:SS.MMM on a 24-hour clock cycle.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE time\_field = :TimeParam" );

AdsSetTime( hStatement, "TimeParam", "13:30:00", strlen( "13:30:00" ) );

AdsExecuteSQL( hStatement, &hCursor);

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE time\_field = :TimeParam" );

AdsSetTime( hStatement, ADSFIELD(1), "13:30:00", strlen( "13:30:00" ) );

AdsExecuteSQL( hStatement, &hCursor);

Example 3

[Additional Example](ace_more_examples.md#adssettimeexample)

See Also

[AdsSetField](ace_adssetfield.md)

[AdsGetTime](ace_adsgettime.md)

[AdsSetMilliseconds](ace_adssetmilliseconds.md)

[AdsInitRawKey](ace_adsinitrawkey.md)

[AdsBuildRawKey](ace_adsbuildrawkey.md)

[AdsPrepareSQL](ace_adspreparesql.md)
