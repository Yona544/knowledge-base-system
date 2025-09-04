3001 Incomplete index key expression




Advantage Database Server 12  

3001 Incomplete index key expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3001 Incomplete index key expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3001 Incomplete index key expression Advantage Error Guide error\_3001\_incomplete\_index\_key\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3001 Incomplete index key expression  Advantage Error Guide |  |  |  |  |

An error occurred in the Advantage Expression Engine parser. The error was in the index key expression.

Problem 1: The expression is invalid. The expression may be invalid due to an extra right paren(s) plus possible other invalid text following that parenthesis. The expression may also be invalid to an extra, illegal comma placed within the expression plus possible other invalid text following that comma.

Solution 1: Delete any indexes that have an invalid expression and rebuild the index with a valid index expression.

Problem 2: The parse finished but the expression was incomplete.

Solution 2: If Solution 1 above does not solve the problem and this error persists, contact Advantage [Technical Support](master_technical_support_u_s__and_canada.htm) and send in a small re-creation.