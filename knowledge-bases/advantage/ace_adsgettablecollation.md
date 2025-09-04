AdsGetTableCollation




Advantage Database Server 12  

AdsGetTableCollation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableCollation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableCollation Advantage Client Engine ace\_Adsgettablecollation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language that the table was opened or created with.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableCollation ( ADSHANDLE hConnect,                        UNSIGNED8 \*pucCollation,                        UNSIGNED16 \*pusLen ); |

Parameters

|  |  |
| --- | --- |
| hTbl (I) | Handle of table or cursor. |
| pucCollation (O) | Return the collation language in this buffer. See [dynamic collation support](master_collation_support.htm). |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetTableCollation gets the collation language that the table was opened or created with. If no collation language was specified when the table was opened or created, AdsGetTableCollation returns an empty string.

Example

ulRetCode = AdsOpenTable90( 0, "D:\\data\\customers.dbf", "customers", ADS\_VFP,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_IGNORERIGHTS, ADS\_DEFAULT, "GERMAN\_VFP\_CI\_AS\_1252", &hTable );

usLen = sizeof( aucCollation );

ulRetCode = AdsGetTableCollation( hTable, aucCollation, &usLen );

See Also

[AdsGetIndexCollation](ace_adsgetindexcollation.htm)

[AdsSetCollation](ace_adssetcollation.htm)

[AdsGetCollation](ace_adsgetcollation.htm)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.htm)