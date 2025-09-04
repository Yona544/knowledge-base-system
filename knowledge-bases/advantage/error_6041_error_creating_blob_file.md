6041 Error creating BLOB file




Advantage Database Server 12  

6041 Error creating BLOB file

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6041 Error creating BLOB file  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6041 Error creating BLOB file Advantage Error Guide error\_6041\_error\_creating\_blob\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6041 Error creating BLOB file  Advantage Error Guide |  |  |  |  |

Problem: An error occurred creating the specified file that is to contain the BLOB to be written from the specified memo field in the function AX\_BLOB2File().

Solution: Make sure the path specified with the file name exists and is accurate. If the file already exists, make sure no other users currently have the specified file open. Verify the user has sufficient access rights to create and open the specified file.