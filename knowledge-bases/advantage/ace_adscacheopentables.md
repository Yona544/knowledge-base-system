AdsCacheOpenTables




Advantage Database Server 12  

AdsCacheOpenTables

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCacheOpenTables  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCacheOpenTables Advantage Client Engine ace\_Adscacheopentables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCacheOpenTables  Advantage Client Engine |  |  |  |  |

Provides caching of open tables

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCacheOpenTables (UNSIGNED16 usOpen); |

Parameters

|  |  |
| --- | --- |
| usOpen (I) | Number of tables to cache. |

Remarks

AdsCacheOpenTables allows table closes to be cached in order for subsequent opens to occur faster. A call to [AdsCloseTable](ace_adsclosetable.htm) with the table cache greater than zero results in the table appearing closed to an application, but still open on the Advantage server. A subsequent [AdsOpenTable](ace_adsopentable.htm) call will return very quickly because the server already has the table open. However, if the access rights for an [AdsOpenTable](ace_adsopentable.htm) on a cached table are different than those with which it was originally opened, the Advantage Client Engine will close the table and reopen it with the changed access rights.

Call this function if an application performs multiple opens and closes on the same table. If an application opens tables and leaves them open, AdsCacheOpenTables provides no additional value.

AdsCacheOpenTables is a global setting that affects the behavior of the entire application. The default number of open tables that are cached is 0.

Example

[Click Here](ace_examples.htm#adscacheopentablesexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCloseTable](ace_adsclosetable.htm)

[AdsCloseCachedTables](ace_adsclosecachedtables.htm)