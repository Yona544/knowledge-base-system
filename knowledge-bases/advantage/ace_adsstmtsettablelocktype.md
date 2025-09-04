AdsStmtSetTableLockType




Advantage Database Server 12  

AdsStmtSetTableLockType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTableLockType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTableLockType Advantage Client Engine ace\_Adsstmtsettablelocktype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTableLockType  Advantage Client Engine |  |  |  |  |

Sets the locking type used by the statement handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTableLockType( ADSHANDLE hStatement,  UNSIGNED16 usLockType ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| usLockType (I) | Type of locking to use. Options are ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. If the application is to be used with non-Advantage applications, then ADS\_COMPATIBLE\_LOCKING should be used. If the table will be used only by Advantage applications, then ADS\_PROPRIETARY\_LOCKING should be used. See [Advantage Locking Modes](master_advantage_locking_modes.htm) for more information. When ADS\_COMPATIBLE\_LOCKING is chosen, Advantage uses the appropriate style based on the table type. |

Remarks

The default value for newly created statement handles is ADS\_PROPRIETARY\_LOCKING.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.htm) before calling this API.

Example

[Click Here](ace_more_examples.htm#adsstmtsettablelocktypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.htm)

[AdsStmtSetTableType](ace_adsstmtsettabletype.htm)