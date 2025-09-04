error 3x26 Unicode Coversion Error




Advantage Database Server 12  

3x26 Unicode Conversion Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3x26 Unicode Conversion Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3x26 Unicode Conversion Error Advantage Error Guide error\_3x26\_Unicode\_Coversion\_Error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3x26 Unicode Conversion Error  Advantage Error Guide |  |  |  |  |

3026, 3126, 3226, 3326, 3426, 3526

Problem: There was a problem converting ANSI/OEM character string in the expression to Unicode string, or vice versa.

Solution: Make sure that the correct adscollate.adt is installed. On non-Windows platform, verify that the Advantage ICU components (aicu.so and icudt40l.dat) are installed.