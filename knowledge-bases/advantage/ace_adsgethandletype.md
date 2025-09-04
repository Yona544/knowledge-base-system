AdsGetHandleType




Advantage Database Server 12  

AdsGetHandleType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetHandleType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetHandleType Advantage Client Engine ace\_Adsgethandletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetHandleType  Advantage Client Engine |  |  |  |  |

Returns the type of a given Advantage Client Engine handle.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetHandleType (ADSHANDLE hObj,  UNSIGNED16 \*pusType); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of an Advantage Client Engine object. |
| pusType ( O ) | Type of the Advantage Client Engine handle. |

Remarks

Possible types returned are ADS\_TABLE for table handles, ADS\_CONNECTION for connection handles, ADS\_INDEX\_ORDER for index order handles, ADS\_FTS\_INDEX\_ORDER for full text search index order handles, ADS\_CURSOR for cursor handles, ADS\_SQL\_STATEMENT for statement handles, ADS\_DATABASE\_CONNECTION for data dictionary connections, and ADS\_SYS\_ADMIN\_CONNECTION for system administrator (adssys) data dictionary connections.

Example

None.

See Also

[AdsFindConnection](ace_adsfindconnection.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.htm)