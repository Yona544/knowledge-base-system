AdsGetTableConnection




Advantage Database Server 12  

AdsGetTableConnection

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableConnection  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableConnection Advantage Client Engine ace\_Adsgettableconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableConnection  Advantage Client Engine |  |  |  |  |

Returns the connection handle associated with a table handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableConnection (ADSHANDLE hTbl,  ADSHANDLE \*phConnect); |

Parameters

|  |  |
| --- | --- |
| hTbl (I) | Handle of table or cursor |
| phConnect (O) | Returned connection handle |

Remarks

AdsGetTableConnection returns the connection handle associated with a given table handle. This function can be used to extract a table handle from a table opened by calling [AdsOpenTable](ace_adsopentable.htm) with a zero for the connection handle. Every table handle has an associated connection handle, no matter how the table handle was generated.

Example

None.

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsGetConnectionType](ace_adsgetconnectiontype.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)

[AdsOpenTable](ace_adsopentable.htm)