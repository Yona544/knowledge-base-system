DIFFERENCE()




Advantage Database Server 12  

DIFFERENCE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DIFFERENCE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DIFFERENCE() Advantage Concepts master\_difference Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DIFFERENCE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that computes the difference of the SOUNDEX values of two strings.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DIFFERENCE( <cStr1>, <cStr2> ) à nResult

Parameters

|  |  |
| --- | --- |
| <cStr1>, <cStr2> | Character values. |

Return Value

A value measuring the SOUNDEX difference between <cStr1> and <cStr2>.

Remarks

DIFFERENCE() returns an integer value that indicates the difference between the values returned by the SOUNDEX() function for <cStr1> and <cStr2>. The value returned will be in the range 0 to 4. The value 4 indicates the closest match (it means that the soundex encoding of str1 and str2 are identical). The value 0 indicates the lowest possible phonetic match, with the values 1, 2, and 3 indicating increasing degrees of phonetic matching.

See Also

[SOUNDEX()](master_soundex.htm)