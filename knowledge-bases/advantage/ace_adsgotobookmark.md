AdsGotoBookmark




Advantage Database Server 12  

AdsGotoBookmark

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGotoBookmark  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGotoBookmark Advantage Client Engine ace\_Adsgotobookmark Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGotoBookmark  Advantage Client Engine |  |  |  |  |

Positions the given table to the given bookmark

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGotoBookmark (ADSHANDLE hTable,  ADSHANDLE hBookmark); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| hBookmark (I) | Bookmark from a call to AdsGetBookmark. |

Remarks

This function is equivalent to [AdsGotoRecord](ace_adsgotorecord.htm). Currently, hBookmark as returned from AdsGetBookmark is the record number.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adsgotobookmarkexample)

See Also

[AdsGetBookmark](ace_adsgetbookmark.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)