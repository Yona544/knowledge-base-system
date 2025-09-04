6040 Error opening file containing the BLOB




Advantage Database Server 12  

6040 Error opening file containing the BLOB

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6040 Error opening file containing the BLOB  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6040 Error opening file containing the BLOB Advantage Error Guide error\_6040\_error\_opening\_file\_containing\_the\_blob Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6040 Error opening file containing the BLOB  Advantage Error Guide |  |  |  |  |

Problem: An error occurred opening the specified file containing the BLOB to be written to the specified memo field in the function AX\_File2BLOB().

Solution: Make sure the specified file containing the BLOB exists. Verify the path specified with the file name exists and is accurate. Also, verify no other users currently have the specified file open. Make sure the user has sufficient access rights to open the specified file.