5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT




Advantage Database Server 12  

5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT Advantage Error Guide error\_5169\_ae\_info\_copy\_made\_by\_client Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5169 AE\_INFO\_COPY\_MADE\_BY\_CLIENT  Advantage Error Guide |  |  |  |  |

This is an informational error code that can be retrieved by using AdsGetLastError after a call to AdsCopyTable or AdsCopyTableContents. Should this error be retrieved after a call to either of these APIs it does NOT signify that the copy failed. Instead it means that the server could not carry out the copy and the operation had to be scaled back to the client in order to complete. The error string passed to AdsGetLastError will contain specifics as to why the operation had to scale back to the client when AdsGetLastError returns.