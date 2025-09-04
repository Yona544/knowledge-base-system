AdsClearSQLAbortFunc




Advantage Database Server 12  

AdsClearSQLAbortFunc

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearSQLAbortFunc  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearSQLAbortFunc Advantage Client Engine ace\_Adsclearsqlabortfunc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearSQLAbortFunc  Advantage Client Engine |  |  |  |  |

Clears the SQL abort callback function registered using AdsRegisterSQLAbortFunc.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm) and [AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm) instead, as they work better with threads and have more complete functionality.

Syntax

UNSIGNED32 AdsClearSQLAbortFunc();

Parameters

None.

Remarks

AdsClearSQLAbortFunc will cause the Advantage Client Engine to stop calling the registered callback function. The SQL abort callback function is used to abort an SQL query.

See Also

[AdsRegisterSQLAbortFunc](ace_adsregistersqlabortfunc.htm)