AOF Relational Operators




Advantage Database Server 12  

AOF Relational Operators

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AOF Relational Operators  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - AOF Relational Operators Advantage Concepts master\_Aof\_relational\_operators Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AOF Relational Operators  Advantage Concepts |  |  |  |  |

Advantage Optimized Filters support the following relational operators. See [Expression Engine Operators](master_expression_engine_operators.htm) for details.

|  |  |
| --- | --- |
| Operator | Description |
| = | Equal to |
| == | Strict equality for string comparison |
| < | Less than |
| <= | Less than or equal to |
| > | Greater than |
| >= | Greater than or equal to |
| #, !=, <> | Not equal to |
| $ | String containment |

For the string containment operator ($) to be optimized, it must have the field name on the left side of the operator just as with the other operators. For example, the filter expression "x $ lastname", which will find all records that have the character x in the field "lastname", will not be optimized. The containment operator can be used to efficiently find all records that have one of a set of specific characters in a specific location. For example, if the index "SUBSTR(category, 3, 1)" existed, then the filter expression "SUBSTR(category, 3, 1) $ aAbB" would be fully optimized and would find all records that have either an A, a, B, or b in the third character of field "category". It can also be used for longer substrings, but it would generally be more efficient to use several simple expressions joined with the logical .OR. operator.