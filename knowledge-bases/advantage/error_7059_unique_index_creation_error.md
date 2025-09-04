7059 Unique index creation error




Advantage Database Server 12  

7059 Unique index creation error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7059 Unique index creation error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7059 Unique index creation error Advantage Error Guide error\_7059\_unique\_index\_creation\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7059 Unique index creation error  Advantage Error Guide |  |  |  |  |

Problem: An index with the UNIQUE property was not able to be created because data in the table produced non-unique key values.

Solution: Make sure that the table data used to create the unique index is unique. When the record(s) was found that would cause a non-unique key to be place in the index, an error was logged in the Advantage error log (ADS\_ERR.ADT or ADS\_ERR\_.DBF). That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Use the Advantage error log to determine which records are in violation of the uniqueness property.