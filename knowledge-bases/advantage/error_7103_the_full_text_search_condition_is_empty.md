7103 The full text search condition is empty




Advantage Database Server 12  

7103 The full text search condition is empty

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7103 The full text search condition is empty  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7103 The full text search condition is empty Advantage Error Guide error\_7103\_the\_full\_text\_search\_condition\_is\_empty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7103 The full text search condition is empty  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition does not have any valid search words. It is possible, for example, to specify a search condition that contains only noise words. The full text search engine ignores noise words that are in the search condition. If the condition consists of nothing but noise words, or words that are shorter than the minimum word length, then the engine has nothing to search for.

Solution: Verify that the search condition consists of at least one non-noise word.