AdsResetConnection




Advantage Database Server 12  

AdsResetConnection

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsResetConnection  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsResetConnection Advantage Client Engine ace\_Adsresetconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsResetConnection  Advantage Client Engine |  |  |  |  |

Resets a given connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsResetConnection (ADSHANDLE hConnect); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle to reset. |

Remarks

AdsResetConnection resets a connection, (i.e., it closes all tables, indexes, SQL statements, unloads all stored procedure modules, and rolls back any uncommitted transactions.)