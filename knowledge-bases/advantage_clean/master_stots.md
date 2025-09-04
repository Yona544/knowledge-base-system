---
title: Master Stots
slug: master_stots
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_stots.htm
source: Advantage CHM
tags:
  - master
checksum: d587d4263aa40a880807f078f731a8d369b29cfa
---

# Master Stots

STOTS()

STOTS()

Advantage Concepts

| STOTS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a character string formatted as 'YYYYMMDD HH:MM:SS.mmm' to a timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

STOTS(<cTimestamp>) -> Timestamp

Parameters

| <cTimestamp> | A character string consisting of a date and a time. The year consists of numbers representing the year, month, and day in the format YYYYMMDD, and the time is in the form HH:MM:SS.mmm. |

Return Values

STOTS() returns a timestamp value. If <cTimestamp> is not a valid timestamp, CTOTS() returns an empty timestamp.

Remarks

STOTS() is a character conversion function that converts a character string to a timestamp. STOTS() can be used whenever you need a literal DateTime value. It differs from CTOTS() in that the date format is fixed and does not depend on the current date format setting. Some examples of its use include:

- Comparing the result of a timestamp expression to a literal timestamp string.

- Defining a filter that compares a literal timestamp string with a timestamp field. For example, if a table has a timestamp field named 'timestamp', then the filter "STOTS( '19960913 14:30:45') > timestamp" could be used to find all records where the timestamp field has a date and time earlier than the given value.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

Examples

STOTS( '19950216 2:00:00pm' )

 

STOTS( '19950216 2:00pm' )

 

STOTS( '19950216 14:00:00.55' )

 

STOTS( '19950216' )

See Also

[CTOD()](master_ctod.md)

[CTOT()](master_ctot.md)

[CTOTS()](master_ctots.md)

[DATE()](master_date.md)

[DTOC()](master_dtoc.md)

[DTOS()](master_dtos.md)

[TTOC()](master_ttoc.md)

[TSTOD()](master_tstod.md)
