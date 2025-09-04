AdsGetNumOpenTables




Advantage Database Server 12  

AdsGetNumOpenTables

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumOpenTables  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumOpenTables Advantage Client Engine ace\_Adsgetnumopentables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumOpenTables  Advantage Client Engine |  |  |  |  |

Retrieves the total number of open tables and cursors in this application

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetNumOpenTables (UNSIGNED16 \*pusNum); |

Parameters

|  |  |
| --- | --- |
| pusNum (O) | Returns number of open tables and cursors. |

Remarks

AdsGetNumOpenTables will return the total number of open tables and cursors in the application.

Example

[Click Here](ace_examples.htm#adsgetnumopentablesexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetAllTables](ace_adsgetalltables.htm)