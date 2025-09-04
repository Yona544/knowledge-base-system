AdsStmtSetTableCharType




Advantage Database Server 12  

AdsStmtSetTableCharType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTableCharType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTableCharType Advantage Client Engine ace\_Adsstmtsettablechartype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTableCharType  Advantage Client Engine |  |  |  |  |

Sets the type of character data used in rowsets

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTableCharType( ADSHANDLE hStatement,  UNSIGNED16 usCharType ) |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| usCharType (I) | Type of character data used in returned rowsets. Options are ADS\_ANSI and ADS\_OEM, or one of the [dynamic collations](master_collation_support.htm) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be used in the rowset. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified. |

Remarks

The default value for newly created statement handles is ADS\_ANSI.

If the statement handle was created on a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)), this setting is ignored when accessing the [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). The usCharType is obeyed on the free tables.

If the statement handle was created on a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)), the usCharType setting is always obeyed.

Note There cannot be an open cursor associated with the statement when this API is called. If an open cursor exists close it using [AdsCloseTable](ace_adsclosetable.htm) before calling this API.

Example

[Click Here](ace_more_examples.htm#adsstmtsettablechartypeexample)

See Also

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.htm)

[AdsStmtSetTableLockType](ace_adsstmtsettablelocktype.htm)

[AdsStmtSetTableReadOnly](ace_adsstmtsettablereadonly.htm)

[AdsStmtSetTableRights](ace_adsstmtsettablerights.htm)

[AdsStmtSetTableType](ace_adsstmtsettabletype.htm)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.htm)