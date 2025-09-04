AdsApplicationExit




Advantage Database Server 12  

AdsApplicationExit

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsApplicationExit  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsApplicationExit Advantage Client Engine ace\_Adsapplicationexit Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsApplicationExit  Advantage Client Engine |  |  |  |  |

Closes all tables and cleans up all open Advantage connections

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsApplicationExit (); |

Parameters

None.

Remarks

AdsApplicationExit is used to ensure the Advantage Client Engine is unloaded completely and cleanly, and that all open indexes, tables, and connections are closed. Calling this function will roll back any open transactions.

Call AdsApplicationExit when exiting an application and all function calls into the Advantage Client Engine are complete.

Example

[Click Here](ace_examples.htm#adsapplicationexitexample)

See Also

[AdsThreadExit](ace_adsthreadexit.htm)