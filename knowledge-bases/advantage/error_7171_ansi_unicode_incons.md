error\_7171\_ANSI\_UNICODE\_INCONSISTENT




Advantage Database Server 12  

7171 Inconsistent ANSI/Unicode FTS Word Count

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7171 Inconsistent ANSI/Unicode FTS Word Count  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7171 Inconsistent ANSI/Unicode FTS Word Count  Advantage Error Guide Error\_7171\_ANSI\_UNICODE\_INCONS Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7171 Inconsistent ANSI/Unicode FTS Word Count  Advantage Error Guide |  |  |  |  |

Problem: When using wild card in FTS filter expression, i.e. searching in multiple fields, the words to be searched must be the same for all ANSI and Unicode fields. 7171 error is returned when the number of words when parsed using Unicode collation is different from the number of words when parsed in ANSI collation. For example, the expression "Contains( \*, 'КНДР')" where КНДР is encoded in Unicode and is parsed as one word in Unicode. However, in ANSI collation, the same string literal may not be able to translate directly and cannot be parsed into an valid word. If the table contains both ANSI and Unicode fields, the 7171 error will returned.

Solution: Avoid searching both ANSI and Unicode fields for Unicode words that cannot be translated into ANSI encoding.