AdsGetLastTableUpdate




Advantage Database Server 12  

AdsGetLastTableUpdate

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetLastTableUpdate  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetLastTableUpdate Advantage Client Engine ace\_Adsgetlasttableupdate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetLastTableUpdate  Advantage Client Engine |  |  |  |  |

Returns the date the table was last updated.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetLastTableUpdate (ADSHANDLE hTable,  UNSIGNED8 \*pucDate,  UNSIGNED16\*pusDateLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor. |
| pucDate (O) | Day the table was last updated. |
| pusDateLen (I/O) | On input, the length of the pucDate buffer. On output, the length of the returned data. |

Remarks

The date returned is the day the table was last written to, and formatted according to the current date format.

Example

None.

See Also

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsGetEpoch](ace_adsgetepoch.htm)

[AdsOpenTable](ace_adsopentable.htm)