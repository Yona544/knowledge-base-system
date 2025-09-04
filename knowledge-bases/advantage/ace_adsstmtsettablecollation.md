AdsStmtSetTableCollation




Advantage Database Server 12  

AdsStmtSetTableCollation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTableCollation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTableCollation Advantage Client Engine ace\_Adsstmtsettablecollation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTableCollation  Advantage Client Engine |  |  |  |  |

Sets the collation language used by the statement handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTableCollation ( ADSHANDLE hStatement,  UNSIGNED8 \*pucCollation ); |

Parameters

|  |  |
| --- | --- |
| hStatement (I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| pucCollation (I) | The collation language to set on the statement handle. See [dynamic collation support](master_collation_support.htm). |

Remarks

AdsStmtSetTableCollation sets the collation language used by a statement handle when creating or opening ADS\_ADT or ADS\_VFP tables. For all other table types, the statement collation language setting has no effect.

Example

ulRetCode = AdsConnect60( "D:\\data", ADS\_REMOTE\_SERVER, NULL, NULL, 0, &hConnect )

ulRetCode = AdsCreateSQLStatement( hConnect, &hStmt );

ulRetCode = AdsStmtSetTableCollation( hStmt, "GERMAN\_VFP\_CI\_AS\_1252" );

See Also

[AdsSetCollation](ace_adssetcollation.htm)

[AdsGetCollation](ace_adsgetcollation.htm)

[AdsGetTableCollation](ace_adsgettablecollation.htm)

[AdsGetIndexCollation](ace_adsgetindexcollation.htm)

[AdsStmtSetTableCharType](ace_adsstmtsettablechartype.htm)