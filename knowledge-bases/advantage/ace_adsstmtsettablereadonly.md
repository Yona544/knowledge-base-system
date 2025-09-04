AdsStmtSetTableReadOnly




Advantage Database Server 12  

AdsStmtSetTableReadOnly

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTableReadOnly  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTableReadOnly Advantage Client Engine ace\_Adsstmtsettablereadonly Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTableReadOnly  Advantage Client Engine |  |  |  |  |

Modifies the read-only flag associated with the statement handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTableReadOnly( ADSHANDLE hStatement,  UNSIGNED16 usReadOnly ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| usReadOnly (I) | Mode to open the file. Options are ADS\_CURSOR\_READONLY and ADS\_CURSOR\_READWRITE. If ADS\_CURSOR\_READONLY is used then any future cursors resulting from an [AdsExecuteSQL](ace_adsexecutesql.htm) statement will be read-only. If the value of ADS\_CURSOR\_READWRITE is used, then the resulting cursor may be used to update the rowset if a key-set cursor is possible. |

Remarks

The default value for newly created statement handles is ADS\_CURSOR\_READWRITE.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.htm) before calling this API.

Example

[Click Here](ace_more_examples.htm#adsstmtsettablereadonlyexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.htm)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.htm)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.htm)

[AdsStmtSetTableType](ace_adsstmtsettabletype.htm)