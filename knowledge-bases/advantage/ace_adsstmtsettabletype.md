AdsStmtSetTableType




Advantage Database Server 12  

AdsStmtSetTableType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTableType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTableType Advantage Client Engine ace\_Adsstmtsettabletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTableType  Advantage Client Engine |  |  |  |  |

Sets the table type used by the statement handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTableType( ADSHANDLE hStatement,  UNSIGNED16 usTableType ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| usTableType (I) | Type of table. Options are ADS\_CDX, ADS\_VFP, and ADS\_ADT. ADS\_NTX is a valid option on a statement handle created on a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |

Remarks

The default value for newly created statement handles is ADS\_ADT.

If the statement handle was created on a database connection, the usTableType will affect the table created using the CREATE TABLE statement. It also determines the table type of [free table(s)](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) that are used in the query.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.htm) before calling this API.

Example

[Click Here](ace_more_examples.htm#adsstmtsettabletypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.htm)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.htm)