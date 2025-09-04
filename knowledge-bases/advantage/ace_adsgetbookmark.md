AdsGetBookmark




Advantage Database Server 12  

AdsGetBookmark

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetBookmark  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetBookmark Advantage Client Engine ace\_Adsgetbookmark Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetBookmark  Advantage Client Engine |  |  |  |  |

Retrieves a bookmark for a later call to AdsGotoBookmark

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetBookmark (ADSHANDLE hTable,  ADSHANDLE \*phBookmark); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| PhBookmark (O) | Return a handle that refers to the current record. |

Remarks

AdsGetBookmark returns the physical record number. It is the equivalent of [AdsGetRecordNum](ace_adsgetrecordnum.htm) called with ADS\_IGNOREFILTERS.

Example

[Click Here](ace_examples.htm#adsgetbookmarkexample)

See Also

[AdsGotoBookmark](ace_adsgotobookmark.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)