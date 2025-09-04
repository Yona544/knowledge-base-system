3101 Incomplete record filter expression




Advantage Database Server 12  

3101 Incomplete record filter expression

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 3101 Incomplete record filter expression  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 3101 Incomplete record filter expression Advantage Error Guide error\_3101\_incomplete\_record\_filter\_expression Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 3101 Incomplete record filter expression  Advantage Error Guide |  |  |  |  |

An error occurred in the Advantage Expression Engine parser. The error was in the record filter expression.

Problem 1: The expression is invalid. The expression may be invalid due to an extra right paren(s) plus possible other invalid text following that parenthesis. The expression may also be invalid to an extra, illegal comma placed within the expression plus possible other invalid text following that comma.

Solution 1: Change any filters that use an invalid expression and re-set the filter using a valid expression.

Problem 2: The parse finished but the expression was incomplete.

Solution 2: If Solution 1 above does not solve the problem and the error persists, contact Advantage [Technical Support](master_technical_support_u_s__and_canada.htm) and send in a small re-creation.