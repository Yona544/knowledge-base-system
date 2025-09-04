CTOT()




Advantage Database Server 12  

CTOT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CTOT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CTOT() Advantage Concepts master\_Ctot Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CTOT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a Time value from a character expression.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CTOT(<cTime>) à tTime

Parameters

|  |  |
| --- | --- |
| <cTime> | A character string consisting of numbers representing the hour, minutes, seconds, and milliseconds separated by : characters (or any non-numeric character). The hours can be from 0-23, or from 1-12 with an "am" or "pm" specified in <cTime>. If the hour is from 1-11 with no "am" or "pm" specified in <cTime>, the time returned is am. If the hour is 12 and no "am" or "pm" indicator is specified, it is assumed to be 12pm. |

Return Value

CTOT() returns a time value. If <cTime> is not a valid time, CTOT() returns an empty time (0).

Remarks

CTOT() is a character conversion function that converts a character string to a time. CTOT() is used whenever you need a literal time value. Some examples include:

|  |  |
| --- | --- |
| · | Comparing the result of a time expression to a literal time string. |

|  |  |
| --- | --- |
| · | Defining a filter that compares a literal time string with a timestamp or time field. For example, if a table has a time field named time, then the filter "CtoT( 10:30am) > time" could be used to find all records where the time field has a value earlier than 10:30am. If CTOT() is used to compare a value with a timestamp field, then only the time portion of the field is used in the comparison; the date portion is ignored. |

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

Examples

CTOT( "" )    // returns an empty time

CTOT( "12:00:00am" )  // midnight - 12:00 am

CTOT( "12:00:00" )  // noon - 12:00 pm

CTOT( "1:21:12pm" ) // 1:21:12 pm

CTOT( "21:12" )   // 9:21 pm

CTOT( "2:00" )  // 2:00 am

CTOT( "1:25:15.234") // 234 milliseconds after 1:25:15 am

See Also

[CTOTS()](master_ctots.htm)

[CTOD()](master_ctod.htm)

[STOD()](master_stod.htm)

[STOTS()](master_stots.htm)