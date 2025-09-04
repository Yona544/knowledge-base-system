AdsGetSQLStatementHandle




Advantage Database Server 12  

AdsGetSQLStatementHandle

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetSQLStatementHandle  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetSQLStatementHandle Advantage Client Engine ace\_Adsgetsqlstatementhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetSQLStatementHandle  Advantage Client Engine |  |  |  |  |

Returns the statement handle associated with the cursor handle passed in.

Syntax

UNSIGNED32 AdsGetSQLStatementHandle( ADSHANDLE hCursor,

ADSHANDLE \*phStmt );

Parameters

|  |  |
| --- | --- |
| hCursor (I) | Cursor handle to retrieve the statement handle from. |
| phStmt (O) | Handle of the statement that ownes hCursor. |

Remarks

Use AdsGetSQLStatementHandle to get the statement handle a cursor was executed on.

See Also

[AdsGetTableHandle](ace_adsgettablehandle.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)