AdsGetBookmarkLength




Advantage Database Server 12  

AdsGetBookmarkLength

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetBookmarkLength  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetBookmarkLength Advantage Client Engine ace\_Adsgetbookmarklength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetBookmarkLength  Advantage Client Engine |  |  |  |  |

Returns the length required to save a bookmark

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetBookmarkLength (ADSHANDLE hObj,  UNSIGNED32 \*pulLength); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of a table, cursor, or index. |
| pulLength (O) | Return the bookmark length. |

Remarks

AdsGetBookmarkLength returns the length required to save a bookmark with a call to [AdsGetBookmark60](ace_adsgetbookmark60.htm). The bookmark length is related to the index key size, and can vary depending on the index handle passed in. If passed a table handle AdsGetBookmarkLength will always return the same length. If passed a cursor handle AdsGetBookmarkLength can return a variable length depending on the ORDER BY clause of the SQL statement.

Allocate a buffer of \*pulLength bytes to be passed to the AdsGetBookmark60 API.

If using the AdsGetBookmark60 API to save, goto and compare bookmarks, AdsGetBookmarkLength should be called any time the ordering of a table/cursor is changed, to insure a correct bookmark length is maintained by the calling application.

Example

UNSIGNED32 ulRetVal;

UNSIGNED32 ulBookmarkLength;

UNSIGNED8 \*pucBookmark1, \*pucBookmark2;

SIGNED32 lResult;

 

/\* Get the bookmark size for this index. \*/

ulRetVal = AdsGetBookmarkLength( hIndex, &ulBookmarkLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Allocate two bookmarks. \*/

pucBookmark1 = (UNSIGNED8\*)malloc( ulBookmarkLength );

pucBookmark2 = (UNSIGNED8\*)malloc( ulBookmarkLength );

 

/\* Gotop and get a bookmark. \*/

AdsGotoTop( hIndex );

 

ulRetVal = AdsGetBookmark60( hIndex, pucBookmark1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Skip 3 records and get a bookmark. \*/

AdsSkip( hIndex, 3 );

 

ulRetVal = AdsGetBookmark60( hIndex, pucBookmark2 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Compare the bookmarks. \*/

ulRetVal = AdsCompareBookmarks( pucBookmark1, pucBookmark2, &lResult );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

See Also

[AdsGetBookmark60](ace_adsgetbookmark60.htm)

[AdsGotoBookmark60](ace_adsgotobookmark60.htm)

[AdsCompareBookmarks](ace_adscomparebookmarks.htm)