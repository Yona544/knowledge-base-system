SCORE()




Advantage Database Server 12  

SCORE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SCORE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SCORE() Advantage Concepts master\_score Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SCORE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the score of a [CONTAINS()](master_contains.htm) result.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

SCORE( <n> ) à nScore

SCORE( <field> | \*, <cCondition> )

Parameters

|  |  |
| --- | --- |
| <n> | If this version of SCORE is used, <n> refers to the nth instance of CONTAINS() in an SQL statement. |
| <field> | \* | If this version of SCORE is used, a field is specified or an asterisk (\*) to indicate that all FTS-indexed fields will be searched. |
| <cCondition> | A valid [FTS search condition](master_full_text_search_conditions.htm). |

Return Value

An integer score

Remarks

The SCORE() function can be used in either of two forms. If it is used in conjunction with one or more CONTAINS() calls in an SQL statement, it is possible to just specify the instance number of a CONTAINS() call, and it will use the same parameters as that referenced CONTAINS.  It is also valid to just specify the full search condition in the SCORE() call.

SCORE() returns an integer value representing the score of the search condition for a given record. The score is the total count of the words from the search condition that are in the field. This is normally expected to be used in conjunction with the CONTAINS() scalar function (e.g., in ORDER BY clauses), but it can used in statements that do not use the CONTAINS() function.

See Also

[Full Text Search](master_full_text_search.htm)

[Full Text Search Examples](master_full_text_search_scalar_functions.htm)

[CONTAINS()](master_contains.htm)

[SCOREDISTINCT()](master_scoredistinct.htm)