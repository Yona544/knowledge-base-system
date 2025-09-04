POSITION()




Advantage Database Server 12  

POSITION()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| POSITION()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - POSITION() Advantage Concepts master\_position Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| POSITION()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that searches for one string in another.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

POSITION( <cSearch> IN <cTarget> ) à nPos

Parameters

|  |  |
| --- | --- |
| <cSearch> | The string to search for |
| <cTarget> | The string to be searched |

Return Value

POSITION() returns the position of the first instance of <cSearch> within <cTarget> as an integer numeric value. If <cSearch> is not found, POSITION() returns zero.

See Also

[AT()](master_at.htm)