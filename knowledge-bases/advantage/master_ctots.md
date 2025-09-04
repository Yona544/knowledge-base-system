CTOTS()




Advantage Database Server 12  

CTOTS()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CTOTS()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CTOTS() Advantage Concepts master\_Ctots Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CTOTS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a Timestamp value from a character expression.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CTOTS( <cTimestamp> ) à tTimestamp

Parameters

|  |  |
| --- | --- |
| <cTimestamp> | Specifies the character expression from which a timestamp value is returned. The proper format for the date component of <cTimestamp> is determined by the current setting of the function to set the date format. |

Return Value

CTOTS() returns a timestamp value. If <cTimestamp> is not a valid timestamp, CTOTS() returns an empty timestamp (0).

Remarks

CTOTS() is a character conversion function that converts a character string to a time. CTOTS() is used whenever you need a literal DateTime value. Some examples include:

|  |  |
| --- | --- |
| · | Comparing the result of a timestamp expression to a literal timestamp string. |

|  |  |
| --- | --- |
| · | Defining a filter that compares a literal timestamp string with a timestamp field. For example, if a table has a timestamp field named timestamp, then the filter "CtoTS( 9/30/1996 10:30am) > timestamp" could be used to find all records where the timestamp field has a date and time earlier than the given value. |

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

Examples

CTOTS( "02/16/95 2:00:00pm" )

CTOTS( "02/16/95 2:00pm" )

CTOTS( "02/16/95 14:00:00.55" )

CTOTS( "02/16/95" )

 

If only a date portion is specified in <cTimeStamp>, a default time of midnight (12:00:00 A.M.) is added to <cTimeStamp>.

See Also

[CTOT()](master_ctot.htm)

[CTOD()](master_ctod.htm)

[DTOS()](master_dtos.htm)

[STOD()](master_stod.htm)

[STOTS()](master_stots.htm)

[TSTOD()](master_tstod.htm)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.htm)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsSetEpoch](ace_adssetepoch.htm)