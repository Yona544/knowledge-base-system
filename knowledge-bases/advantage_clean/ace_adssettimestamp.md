---
title: Ace Adssettimestamp
slug: ace_adssettimestamp
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssettimestamp.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5442faf1c6eb24dd24736a7960154e2b27429327
---

# Ace Adssettimestamp

AdsSetTimeStamp

AdsSetTimeStamp

Advantage Client Engine

| AdsSetTimeStamp  Advantage Client Engine |  |  |  |  |

Stores the given timestamp in the given field

Syntax

| UNSIGNED32 | AdsSetTimeStamp( ADSHANDLE hObj,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucBuf,  UNSIGNED32 ulLen ) |

Parameters

| hObj (I) | Handle of table or statement. |
| pucFldName (I) | Name of field to set. |
| pucBuf (I) | TimeStamp value as a string. |
| ulLen (I) | Length of data. |

Remarks

Dates, times, timestamps, and numerics are expected to be given as text strings. Dates are expected to be formatted the same as the current [AdsSetDateFormat](ace_adssetdateformat.md) setting. For example, to set a timestamp field, the value could be "7/28/1996 14:30:25". To set empty or null values in fields, use [AdsSetEmpty](ace_adssetempty.md). Setting the value of a field requires a data lock on the table, either a record lock or a file lock. If no lock is held on the current record or table, the Advantage Client Engine will attempt to get an implicit lock on the record. Implicit locks are released when the record is updated on the server.

When passed a statement handle, this API can be used to specify parameters in an SQL statement previously prepared with a call to [AdsPrepareSQL](ace_adspreparesql.md). For this usage, pass pucFieldName as either the name of the parameter (when using named parameters) or the number of the parameter (when using either named or unnamed parameters). Parameter numbers in SQL statements are assigned left to right and utilize a one-based counter. For example, in the statement "SELECT \* FROM test WHERE :lname = :value" the lname parameter could be referenced either as "lname" or as parameter 1. Using the same logic the value parameter could be referenced either as "value" or as parameter 2.

If using AdsSetTimeStamp to set parameters in an SQL statement, the format CCYY-MM-DD HH:MM:SS or CCYY-MM-DD HH:MM:SS.MMM on a 24-hour clock cycle can always be used. Alternatively, the date portion of the timestamp field can be specified using the current Advantage Client Engine date format (see [AdsSetDateFormat](ace_adssetdateformat.md)).

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example 1

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE arrival = :ArrivalParam" );

AdsSetTimeStamp( hStatement, "ArrivalParam", "1999-04-28 19:00:00", strlen("1999-04-28 19:00:00" ));

AdsExecuteSQL( hStatement, &hCursor);

When using unnamed parameters these parameters MUST be referenced using their parameter number.

Example 2

AdsPrepareSQL( hStatement,

"SELECT \* FROM test WHERE arrival = :ArrivalParam" );

AdsSetTimeStamp( hStatement, ADSFIELD(1), "1999-04-28 19:00:00", strlen("1999-04-28 19:00:00" ));

AdsExecuteSQL( hStatement, &hCursor);

See Also

[AdsSetField](ace_adssetfield.md)

[AdsSetTime](ace_adssettime.md)

[AdsSetDate](ace_adssetdate.md)

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsSetJulian](ace_adssetjulian.md)

[AdsSetMilliseconds](ace_adssetmilliseconds.md)
