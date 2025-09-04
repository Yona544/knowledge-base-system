7102 No full text search indexes found




Advantage Database Server 12  

7102 No full text search indexes found

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7102 No full text search indexes found  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7102 No full text search indexes found Advantage Error Guide error\_7102\_no\_full\_text\_search\_indexes\_found Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7102 No full text search indexes found  Advantage Error Guide |  |  |  |  |

Problem: Use of CONTAINS( \*, 'condition' ) requires at least one full text search index. The asterisk (\*) indicates that all fields that have full text search indexes are to be searched, but the table does not have any full text search indexes available or the user does not have read permissions to any of the columns that have full text search indexes.

Solution: Create at least one full text search index or specify a particular field to search in the CONTAINS condition. If using a data dictionary with permissions checking turned on, verify that the user has read permission to at least one column that has a full text search index. Note that specifying a specific field to search that does not have a full text search index forces a low level search of the data, which can be slow.