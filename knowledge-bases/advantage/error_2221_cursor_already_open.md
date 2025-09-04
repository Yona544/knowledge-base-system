2221 Cursor already open




Advantage Database Server 12  

2221 Cursor already open

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2221 Cursor already open  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 2221 Cursor already open Advantage Error Guide error\_2221\_cursor\_already\_open Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 2221 Cursor already open  Advantage Error Guide |  |  |  |  |

Problem: An SQL script statement is attempting to open a cursor that is already opened.

Solution: Check the error message for the location of the error in the script. Make sure the OPEN statement at that location is not attempting to open a cursor that has been opened by a statement executed prior to this statement.