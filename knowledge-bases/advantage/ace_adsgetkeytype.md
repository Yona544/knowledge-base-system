AdsGetKeyType




Advantage Database Server 12  

AdsGetKeyType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetKeyType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetKeyType Advantage Client Engine ace\_Adsgetkeytype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetKeyType  Advantage Client Engine |  |  |  |  |

Returns the Advantage Client Engine data type of the evaluated index keys.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetKeyType (ADSHANDLE hIndex,  UNSIGNED16 \*pusType); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of an index order. |
| pusType (O) | Returns the data type of keys in this index order. |

Remarks

Returns the data type of the key as evaluated by the Advantage Client Engine. Possible key types are ADS\_STRING, ADS\_NUMERIC, ADS\_DATE, ADS\_LOGICAL, and ADS\_RAW. ADS\_RAW is returned for any index that uses the binary concatenation operator (;) and for indexes created on time, timestamp, and raw fields.

Example

None.

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetIndexExpr](ace_adsgetindexexpr.htm)

[AdsGetKeyLength](ace_adsgetkeylength.htm)