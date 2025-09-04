Handle




Advantage Database Server 12  

TAdsStoredProc.Handle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.Handle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.Handle Advantage TDataSet Descendant ade\_Handle\_tadsstoredproc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.Handle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Advantage Client Engine (ACE) handle to the cursor (if one exists) returned from procedure execution.

Syntax

property Handle: ADSHANDLE;

Description

Handle contains the Advantage Client Engine handle to the cursor returned from procedure execution. If the handle value is <= 0 it is not a valid handle, and should not be used. This will occur if the procedure does not return any parameters, if the procedure does not return a result set, or if the procedure is not currently active. Use the Handle property if it is necessary to directly call Advantage Client Engine API's.