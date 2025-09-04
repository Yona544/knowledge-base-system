CREATETIMESTAMP()




Advantage Database Server 12  

CREATETIMESTAMP()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATETIMESTAMP()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CREATETIMESTAMP() Advantage Concepts master\_createtimestamp Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATETIMESTAMP()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function to create a timestamp literal from the given integer parameter values.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CREATETIMESTAMP( <nYear>, <nMonth>, <nDay>, <nHour>, <nMinute>, <nSecond>, <nMillisecond> ) à timestamp

Parameters

|  |  |
| --- | --- |
| <nValue> | The components of the timestamp can be expression values with constants or based on field values. |

Return Value

A timestamp value

See Also

[STOTS()](master_stots.htm)

[EXTRACT()](master_extract.htm)