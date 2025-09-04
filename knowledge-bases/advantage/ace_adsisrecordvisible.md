AdsIsRecordVisible




Advantage Database Server 12  

AdsIsRecordVisible

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsRecordVisible  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsRecordVisible Advantage Client Engine ace\_Adsisrecordvisible Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsRecordVisible  Advantage Client Engine |  |  |  |  |

Determines if the current record is visible.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsRecordVisible (ADSHANDLE hObj, UNSIGNED16  \*pbVisible); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| pbVisible (O) | Return True if the current record is visible, False if not. |

Special Return Codes

AE\_NO\_CURRENT\_RECORD Data cannot be retrieved from EOF or BOF

Remarks

AdsIsRecordVisible tests the current record against all record filtering mechanisms. AdsIsRecordVisible will evaluate the current records deleted status, verify the record passes the filter expression (if a filter is set), and verify the record passes the AOF expression (if an AOF is set). If the record passes all of these conditions the return value in the pbVisible parameter will be True. If the record fails to pass any of the conditions the return value in the pbVisible parameter will be False. If the hObj parameter is an index order handle AdsIsRecordVisible will in addition to testing against the above filters also verify the record meets all scope and conditional index specifications.

Note The CONTAINS() function (see [Full Text Search](master_full_text_search_index_options_fts.htm) is not evaluated by this API. It is evaluated as True when evaluated by this API at the client. The cost of performing the text search at the client would be prohibitive. The primary effect of this is that the Advantage TDataSet Descendent will not change the visibility of records when edits are made that would change the result of a CONTAINS() call. The filter or query must be re-executed before the changes will take effect.

Example

AdsIsRecordVisible( hTable, &bVisible );

if ( bVisible )

{

/\* process this record \*/

}

See Also

[AdsIsRecordDeleted](ace_adsisrecorddeleted.htm)

[AdsShowDeleted](ace_adsshowdeleted.htm)