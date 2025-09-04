AdsGetCollation




Advantage Database Server 12  

AdsGetCollation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetCollation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetCollation Advantage Client Engine ace\_Adsgetcollation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetCollation  Advantage Client Engine |  |  |  |  |

Gets the collation language setting of a connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetCollation( ADSHANDLE hConnect,  UNSIGNED8 \*pucCollation,  UNSIGNED16 \*pusLen ); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | A connection handle. |
| pucCollation (O) | The collation language of the connection, or an empty string. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetCollation returns the collation language set on a connection. Initially, a connection has no collation set on it and AdsGetCollation will return an empty string. [AdsSetCollation](ace_adssetcollation.htm) can be used to set the collation language. See [AdsSetCollation](ace_adssetcollation.htm) for a description of when the collation language of a connection is used.

Example

usLen = sizeof( aucCollation );

ulRetCode = AdsGetCollation( hConnect, aucCollation, &usLen );

See Also

[AdsSetCollation](ace_adssetcollation.htm)

[AdsStmtSetTableCollation](ace_adsstmtsettablecollation.htm)

[AdsGetTableCollation](ace_adsgettablecollation.htm)

[AdsGetIndexCollation](ace_adsgetindexcollation.htm)

[Dynamic Collation Support](master_collation_support.htm).