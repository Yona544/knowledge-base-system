RAND()




Advantage Database Server 12  

RAND()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RAND()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - RAND() Advantage Concepts master\_rand Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| RAND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a pseudo-random number.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

RAND( [<nSeed>] ) à SyntaxRetPH

Parameters

|  |  |
| --- | --- |
| <nSeed> | Optional integer seed value for the random number generator. |

Return Value

Pseudo-random number between 0 and 1.

Remarks

Returns a pseudo-random floating point value between 0 and 1 using <nSeed> as an optional seed value. If zero is specified as the seed value, the current time in milliseconds is used as the seed. Seeding RAND() is not required and RAND() should only be seeded once for the life of the connection. Seeding RAND() multiple times on the same connection can result in poor random number generation.