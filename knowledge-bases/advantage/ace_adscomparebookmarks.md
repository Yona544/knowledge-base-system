AdsCompareBookmarks




Advantage Database Server 12  

AdsCompareBookmarks

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCompareBookmarks  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCompareBookmarks Advantage Client Engine ace\_Adscomparebookmarks Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCompareBookmarks  Advantage Client Engine |  |  |  |  |

Compares two bookmarks.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCompareBookmarks (UNSIGNED8 \*pucBookmark1,  UNSIGNED8 \*pucBookmark2,  SIGNED32 \*plResult); |

Parameters

|  |  |
| --- | --- |
| pucBookmark1 (I) | Bookmark from a call to [AdsGetBookmark60](ace_adsgetbookmark60.htm). |
| pucBookmark2 (I) | Bookmark from a call to [AdsGetBookmark60](ace_adsgotobookmark60.htm). |
| plResult (O) | Result of the comparison. Can be one of the following values: ADS\_CMP\_LESS, ADS\_CMP\_EQUAL, ADS\_CMP\_GREATER. |

Remarks

Compares two bookmarks. If the bookmarks were retrieved from an index handle the key values associated with the bookmarks will be compared, o/w the comparison will be based on the record number. If the key values are compared and determined to be equivalent the record number will then be used for the comparison.

Examples

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

[AdsGetBookmarkLength](ace_adsgetbookmarklength.htm)

[AdsGetBookmark60](ace_adsgetbookmark60.htm)

[AdsGotoBookmark60](ace_adsgotobookmark60.htm)