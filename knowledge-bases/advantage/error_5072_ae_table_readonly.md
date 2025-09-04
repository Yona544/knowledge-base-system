5072 AE\_TABLE\_READONLY




Advantage Database Server 12  

5072 AE\_TABLE\_READONLY

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5072 AE\_TABLE\_READONLY  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5072 AE\_TABLE\_READONLY Advantage Error Guide error\_5072\_ae\_table\_readonly Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5072 AE\_TABLE\_READONLY  Advantage Error Guide |  |  |  |  |

This action requires read-write access to the table. In versions prior to the 6.1 release, this error is only returned when an update is attempted on a table that is specifically opened for read-only access.

In version 6.1 or greater, if the read/write access to the table is requested at the table open time but the table cannot be opened with read/write access due to OS file access restriction or data dictionary table access restriction, the Advantage Client Engine will default to opening the table with read-only access. No error is returned during the table open in this situation but the 5072 error will be returned when attempting to update the table.