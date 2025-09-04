AdsGetFilter




Advantage Database Server 12  

AdsGetFilter

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetFilter  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetFilter Advantage Client Engine ace\_Adsgetfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetFilter  Advantage Client Engine |  |  |  |  |

Returns the current filter expression for the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetFilter (ADSHANDLE hTable,  UNSIGNED8 \*pucFilter,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFilter (O) | Return the expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

AdsGetFilter will return the current filter expression for the specified table. Note that the case of the expression returned is not guaranteed to be identical to the filter expression that was given in the AdsSetFilter.

Example

[Click Here](ace_examples.htm#adsgetfilterexample)

See Also

[AdsSetFilter](ace_adssetfilter.htm)

[AdsClearFilter](ace_adsclearfilter.htm)