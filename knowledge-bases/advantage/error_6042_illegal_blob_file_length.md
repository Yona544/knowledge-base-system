6042 Illegal BLOB file length




Advantage Database Server 12  

6042 Illegal BLOB file length

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6042 Illegal BLOB file length  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6042 Illegal BLOB file length Advantage Error Guide error\_6042\_illegal\_blob\_file\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6042 Illegal BLOB file length  Advantage Error Guide |  |  |  |  |

Problem: The BLOB to be written in either the function AX\_BLOB2File() or AX\_File2BLOB() with the Advantage Clipper RDD was either too large or was of length 0. The size of the BLOB to be written must be between 1 byte and 16MB.

Solution: Verify the size of the BLOB to be written is between 1 byte and 16MB when using the Advantage Clipper RDD.