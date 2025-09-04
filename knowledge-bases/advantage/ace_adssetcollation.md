AdsSetCollation




Advantage Database Server 12  

AdsSetCollation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetCollation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetCollation Advantage Client Engine ace\_Adssetcollation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetCollation  Advantage Client Engine |  |  |  |  |

Sets the collation language on a connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetCollation( ADSHANDLE hConnect,  UNSIGNED8 \*pucCollation ); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | A connection handle. |
| pucCollation (I) | The collation language to be set. See [dynamic collation support](master_collation_support.htm). |

Remarks

AdsSetCollation sets the collation language for a specific connection handle. The collation language of a connection is used when ACE APIs which take a collation language (AdsOpenTable90, AdsCreateTable90, AdsDDAddTable90, and AdsRestructureTable90) are called without a collation language. It is also used with SQL statement handles which have not had a collation language set on them using AdsStmtSetTableCollation.

Note Collation languages passed to ACE APIs are only valid with ADS\_ADT or ADS\_VFP tables. The AdsSetCollation API will not affect ADS\_NTX and ADS\_CDX tables.

Example

ulRetCode = AdsSetCollation( hConnect, "GERMAN\_VFP\_CI\_AS\_1252" );

See Also

[AdsGetCollation](ace_adsgetcollation.htm)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.htm)

[AdsGetTableCollation](ace_adsgettablecollation.htm)

[AdsGetIndexCollation](ace_adsgetindexcollation.htm)

[Dynamic Collation Support](master_collation_support.htm).