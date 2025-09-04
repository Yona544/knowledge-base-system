---
title: Master Scoredistinct
slug: master_scoredistinct
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_scoredistinct.htm
source: Advantage CHM
tags:
  - master
checksum: 5db008efcdcd4e7b84f8dd49654e34b7075f7817
---

# Master Scoredistinct

SCOREDISTINCT()

SCOREDISTINCT()

Advantage Concepts

| SCOREDISTINCT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the score of a [CONTAINS()](master_contains.md) result.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

SCOREDISTINCT( <n> ) à nScore

SCOREDISTINCT( <field> | \*, <cCondition> )

Parameters

| <n> | If this version of SCOREDISTINCT is used, <n> refers to the nth instance of CONTAINS() in an SQL statement. |
| <field> | \* | If this version of SCOREDISTINCT is used, a field is specified or an asterisk (\*) to indicate that all FTS-indexed fields will be searched. |
| <cCondition> | A valid [FTS search condition](master_full_text_search_conditions.md). |

Return Value

An integer score

Remarks

The SCOREDISTINCT() function can be used in either of two forms. If it is used in conjunction with one or more CONTAINS() calls in an SQL statement, it is possible to just specify the instance number of a CONTAINS() call, and it will use the same parameters as that referenced CONTAINS.  It is also valid to just specify the full search condition in the SCOREDISTINCT() call.

SCOREDISTINCT() returns the count of the words in the search condition that appear one or more times in the field for a given record. For example, if the search condition contains three words, this function will return a value from 0 to 3. This is normally expected to be used in conjunction with the CONTAINS() scalar function (e.g., in ORDER BY clauses), but it can used in statements that do not use the CONTAINS() function.

See Also

[Full Text Search](master_full_text_search.md)

[Full Text Search Examples](master_full_text_search_scalar_functions.md)

[CONTAINS()](master_contains.md)

[SCORE()](master_score.md)
