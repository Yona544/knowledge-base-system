AdsCloseSQLStatement




Advantage Database Server 12  

AdsCloseSQLStatement

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloseSQLStatement  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloseSQLStatement Advantage Client Engine ace\_Adsclosesqlstatement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloseSQLStatement  Advantage Client Engine |  |  |  |  |

Releases memory associated with a statement handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloseSQLStatement ( ADSHANDLE hStatement ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of statement to free. |

Remarks

All statement resources are released. If tables were opened during generation of the rowset, they will be closed.

If a cursor associated with this statement exists it is freed as well.

To close a cursor without releasing the statement handle, use [AdsCloseTable](ace_adsclosetable.htm) on the cursor handle.

Note The [AdsCacheOpenCursors](ace_adscacheopencursors.htm) setting must be set to zero in conjunction with the AdsCloseSQLStatement in order for the cursor and underlying table to be truly closed. Use these functions only when necessary or else possible performance loss may occur. To close all cached tables without modifying AdsCacheOpenCursors, see the [AdsCloseCachedTables](ace_adsclosecachedtables.htm) API.

Example

[Click Here](ace_more_examples.htm#adsclosesqlstatementexample)

See Also

[AdsCreateSQLStatement](ace_adscreatesqlstatement.htm)

[AdsCacheOpenCursors](ace_adscacheopencursors.htm)

[AdsCloseCachedTables](ace_adsclosecachedtables.htm)