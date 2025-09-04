LastError




Advantage Database Server 12  

TAdsSettings.LastError

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsSettings.LastError  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsSettings.LastError Advantage TDataSet Descendant ade\_Lasterror Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsSettings.LastError  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.htm)

Holds the last error that was encountered with the Advantage Database Server.

Syntax

property LastError: LongInt;

Description

The error code in this property will be the same as the one returned by the last Advantage Database Server reported error. If no error occurred on the last Advantage Database Server call, 0 (zero) is returned.