AdsGotoBookmark60




Advantage Database Server 12  

AdsGotoBookmark60

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGotoBookmark60  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGotoBookmark60 Advantage Client Engine ace\_Adsgotobookmark60 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGotoBookmark60  Advantage Client Engine |  |  |  |  |

Positions the given table to the given bookmark.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGotoBookmark60 (ADSHANDLE hObj,  UNSIGNED8 \*pucBookmark); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table or cursor. |
| pucBookmark (I) | Bookmark from a call to AdsGetBookmark60. |

Remarks

Position the table/cursor to the bookmark previously retrieved from a call to [AdsGetBookmark60](ace_adsgetbookmark60.htm).

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

See Also

[AdsGetBookmark60](ace_adsgetbookmark60.htm)

[AdsGetBookmarkLength](ace_adsgetbookmarklength.htm)

[AdsCompareBookmarks](ace_adscomparebookmarks.htm)