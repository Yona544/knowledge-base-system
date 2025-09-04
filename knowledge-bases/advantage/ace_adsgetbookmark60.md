AdsGetBookmark60




Advantage Database Server 12  

AdsGetBookmark60

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetBookmark60  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetBookmark60 Advantage Client Engine ace\_Adsgetbookmark60 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetBookmark60  Advantage Client Engine |  |  |  |  |

Retrieves a bookmark for use in a later call to AdsGotoBookmark60 or AdsCompareBookmarks.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetBookmark60 (ADSHANDLE hObj,  UNSIGNED8 \*pucBookmark,  UNSIGNED32 \*pulLength); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of a table, cursor, or index. |
| pucBookmark (O) | Pointer to pre-allocated memory to place the bookmark in. |
| pulLength (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetBookmark60 returns a bookmark into user-allocated space. Allocate pucBookmark using the bookmark length retrieved from a call to the [AdsGetBookmarkLength](ace_adsgetbookmarklength.htm) API. Bookmark length is dependent on the key size of the index in question (if the hObj parameter is an index handle, or a cursor handle based on an SQL statement that utilizes an ORDER BY).

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

 

ulRetVal = AdsGetBookmark60( hIndex, pucBookmark1, &ulBookmarkLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Skip 3 records and get a bookmark. \*/

AdsSkip( hIndex, 3 );

 

ulRetVal = AdsGetBookmark60( hIndex, pucBookmark2, &ulBookmarkLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Compare the bookmarks. \*/

ulRetVal = AdsCompareBookmarks( pucBookmark1, pucBookmark2, &lResult );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

See Also

[AdsGetBookmarkLength](ace_adsgetbookmarklength.htm)

[AdsCompareBookmarks](ace_adscomparebookmarks.htm)

[AdsGotoBookmark60](ace_adsgotobookmark60.htm)