2146 Unable to perform sort for ORDER BY or DISTINCT




Advantage Database Server 12  

2146 Unable to perform sort for ORDER BY or DISTINCT

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2146 Unable to perform sort for ORDER BY or DISTINCT  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2146 Unable to perform sort for ORDER BY or DISTINCT Advantage Error Guide error\_2146\_unable\_to\_perform\_sort\_for\_order\_by\_or\_distinct Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2146 Unable to perform sort for ORDER BY or DISTINCT  Advantage Error Guide |  |  |  |  |

Problem: An error occurred while attempting to sort data for the SQL statement. The most likely cause is a problem with the file system (unable to create a temporary file, unable to write to the disk, etc.).

Solution: If using the Advantage Database Server, the temporary files used for sorting are created in the directory specified in the connect path. With Advantage Local Server, the system temp directory (e.g., the directory specified by the TEMP environment variable) is used for temporary files. Verify that the disk contains enough space for the sorting.