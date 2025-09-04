error 7159 Cannot determine the code page for the default ANSI/OEM character set




Advantage Database Server 12  

7159 Cannot determine the code page for the default ANSI/OEM character set

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7159 Cannot determine the code page for the default ANSI/OEM character set  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7159 Cannot determine the code page for the default ANSI/OEM character set Advantage Error Guide Error\_7159\_Cannot\_determine\_th Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7159 Cannot determine the code page for the default ANSI/OEM character set  Advantage Error Guide |  |  |  |  |

The likely cause for this error is that an older version (pre 10.0 release) of the adscollate.adt is loaded by the server. When Advantage database server is loaded, it will try to determine the code pages of the servers default ANSI/OEM character sets. This is done using look up in the adscollate.adt. If the look up failed to find the corresponding code pages for the character sets, this error will be returned when a conversion between Unicode and code page characters is needed on a table opened with the default ANSI/OEM character type.