5211 AE\_UNICODE\_CONVERSION




Advantage Database Server 12  

5211 AE\_UNICODE\_CONVERSION

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5211 AE\_UNICODE\_CONVERSION  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5211 AE\_UNICODE\_CONVERSION Advantage Error Guide error\_5211\_AE\_UNICODE\_CONVERSION Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5211 AE\_UNICODE\_CONVERSION  Advantage Error Guide |  |  |  |  |

Problem: There was an error when attempting to convert a Unicode character string into ANSI/OEM code page string, or vice versa.

Solution: When this error occurs, retrieve the text error message that accompanies the error. Some causes of this problem are:

|  |  |
| --- | --- |
| · | When trying to store Unicode character data into non-Unicode column, some Unicode characters cannot be converted into the ANSI/OEM code page characters. |

|  |  |
| --- | --- |
| · | An invalid code page is specified when trying to convert Unicode character data into ANSI/OEM code page character. A possible cause for this situation is that an older version of the adscollate.adt is loaded by the server. |