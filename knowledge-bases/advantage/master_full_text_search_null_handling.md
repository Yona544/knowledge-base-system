Full Text Search Null Handling




Advantage Database Server 12  

Full Text Search Null Handling

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Null Handling  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Null Handling Advantage Concepts master\_Full\_text\_search\_null\_handling Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Null Handling  Advantage Concepts |  |  |  |  |

In general, a NULL value in an expression causes the expression to result in NULL. For example, the expression "lastname <> 'Smith'" returns NULL for records where lastname is NULL (and those record are not returned in an SQL result set with that condition).

The CONTAINS scalar function works similarly. CONTAINS(fieldname, search condition) returns NULL for records where the fieldname is NULL regardless of the condition.

The behavior of CONTAINS( \*, search condition ) is slightly different however. If any FTS-indexed field matches the search condition, the record passes the filter even if one of the fields contains a NULL value.