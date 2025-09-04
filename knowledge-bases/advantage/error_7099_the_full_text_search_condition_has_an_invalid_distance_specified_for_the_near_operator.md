7099 The full text search condition has an invalid distance specified for the NEAR operator




Advantage Database Server 12  

7099 The full text search condition has an invalid distance specified for the NEAR operator

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7099 The full text search condition has an invalid distance specified for the NEAR operator  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7099 The full text search condition has an invalid distance specified for the NEAR operator Advantage Error Guide error\_7099\_the\_full\_text\_search\_condition\_has\_an\_invalid\_distance\_specified\_for\_the\_near\_operator Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7099 The full text search condition has an invalid distance specified for the NEAR operator  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has an invalid distance parameter specified for the NEAR operator.

Solution: Verify that the NEAR parameter value is numeric. The NEAR operator can have an optional distance value specified in parentheses. The distance value must be a numeric value. For example, the following search condition is not valid because the parser expects the distance operator to be given:

dog near (cat and mouse)

The following search conditions are valid:

dog near() (cat and mouse)

dog near(5) cat

dog near cat