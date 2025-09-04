AdsStmtConstrainUpdates




Advantage Database Server 12  

AdsStmtConstrainUpdates

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtConstrainUpdates  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtConstrainUpdates Advantage Client Engine ace\_Adsstmtconstrainupdates Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtConstrainUpdates  Advantage Client Engine |  |  |  |  |

Sets constraint behavior for the statement handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtConstrainUpdates ( ADSHANDLE hStatement,  UNSIGNED16 usConstrain ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| usConstrain (I) | Constraint value to set. Options are ADS\_CONSTRAIN and ADS\_NO\_CONSTRAIN. |

Remarks

The default value for newly created statement handles is ADS\_NO\_CONSTRAIN.

If AdsStmtConstrainUpdates is called with a value of ADS\_CONSTRAIN the behavior of future cursors on this statement will change. Any row that is modified with the AdsSet functions (see [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm)) will undergo a WHERE clause verification on the server. If the row does not meet the WHERE clause that created the cursor, then the update will fail and an error will be returned. If the new row does meet the select criteria, then the update will occur normally.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.htm) before calling this API.

Example

[Click Here](ace_more_examples.htm#adsstmtconstrainupdatesexample)

See Also

None.