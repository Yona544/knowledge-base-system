error 7158 The server cannot determine the default ANSI/OEM Unicode collation locale




Advantage Database Server 12  

7158 The server cannot determine the default ANSI/OEM Unicode collation locale

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7158 The server cannot determine the default ANSI/OEM Unicode collation locale  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7158 The server cannot determine the default ANSI/OEM Unicode collation locale Advantage Error Guide Error\_7158\_The\_server\_cannot\_d Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7158 The server cannot determine the default ANSI/OEM Unicode collation locale  Advantage Error Guide |  |  |  |  |

The likely cause for this error is that an older version (pre 10.0 release) of the adscollate.adt is loaded by the servers. When Advantage database server is loaded, it will try to determine the Unicode collation locales correspond to the servers default ANSI/OEM character sets. This is done using look up in the adscollate.adt. If the look up failed to find the corresponding Unicode collation locales, this error will be returned when the server try to sort or compare Unicode characters for tables opened with the default ANSI/OEM collation.