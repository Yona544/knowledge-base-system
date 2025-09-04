Full Text Search and Dynamic Cursors




Advantage Database Server 12  

Full Text Search and Dynamic Cursors

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search and Dynamic Cursors  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search and Dynamic Cursors Advantage Concepts master\_Full\_text\_search\_and\_dynamic\_cursors Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search and Dynamic Cursors  Advantage Concepts |  |  |  |  |

By default, Advantage creates dynamic cursors. When one client makes an update to a table, other clients cursors (result sets) are updated as appropriate based on the record changes. See [Use Dynamic Cursors](master_use_dynamic_cursors.htm) for more information. When the CONTAINS() scalar function is used, however, Advantage will not dynamically update cursor memberships. The cost of evaluating the conditions on memo and BLOB fields would be prohibitively expensive.