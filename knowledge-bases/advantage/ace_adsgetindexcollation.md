AdsGetIndexCollation




Advantage Database Server 12  

AdsGetIndexCollation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexCollation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexCollation Advantage Client Engine ace\_Adsgetindexcollation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language that the index was created or opened with.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexCollation ( ADSHANDLE hIndex,  UNSIGNED8 \*pucCollation,  UNSIGNED16 \*pusLen ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of an index order. |
| pucCollation (O) | Return the collation language in this buffer. See [dynamic collation support](master_collation_support.htm). |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetIndexCollation returns the collation language the index was created or opened with. When an index is opened or created, it inherits the collation language used by the table it belongs to.

Example

usLen = sizeof( aucCollation );

ulRetCode = AdsGetIndexCollation( hIndex, aucCollation, &usLen );

See Also

[AdsGetTableCollation](ace_adsgettablecollation.htm)

[AdsSetCollation](ace_adssetcollation.htm)

[AdsGetCollation](ace_adsgetcollation.htm)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.htm)