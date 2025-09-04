CONTAINS()




Advantage Database Server 12  

CONTAINS()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CONTAINS()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CONTAINS() Advantage Concepts master\_Contains Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CONTAINS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that evaluates a full text search (FTS) expression search condition.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CONTAINS(<field> | \*, <cSearchCondition> ) -> lSearchResult

Parameters

|  |  |
| --- | --- |
| <field> | \* | The field to apply the search condition to. The asterisk (\*) can be used to specify that all fields with full text search (FTS) indexes are to be searched. This parameter can be a character value or the result of some expression that returns a character value, but the search will not be optimized. For best performance, this parameter should be the asterisk or a field that has a full text search index built on it. |
| <cSearchCondition> | A valid [FTS search condition](master_full_text_search_conditions.htm). |

Return Value

CONTAINS returns true (.T.) for records that meet the specified search condition.

Remarks

The CONTAINS() scalar function is the interface to the Advantage full text search engine. For a complete description, see [Full Text Search](master_full_text_search.htm).

This function can be used from the Advantage CA-Clipper AXDBFCDX RDD when using server-side Advantage Optimized Filters (AX\_SetServerAOF). This will evaluate the full text search condition at the server and return records that pass the condition. Full text search conditions are not evaluated at the client, so it is not possible to use CONTAINS() in client-side filters. In addition, building an index using a CONTAINS() expression may provide unexpected results and is not recommended because index keys are sometimes evaluated at the client and will not produce consistent results.

Examples

Search all fields with FTS indexes for records that contain both the word 'john' and 'smith':

 

CONTAINS( \*, 'john smith' )

Search a specific field for records where that field has a word beginning with 'Guggen' or 'Metro':

 

CONTAINS( directions, 'Guggen\* OR Metro\*' )

See Also

[Full Text Search](master_full_text_search.htm)

[Full Text Search Examples](master_full_text_search_scalar_functions.htm)

[SCORE()](master_score.htm)

[SCOREDISTINCT()](master_scoredistinct.htm)