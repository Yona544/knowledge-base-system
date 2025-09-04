Go Top (First, MoveFirst) when a Scope is Set




Advantage Database Server 12  

Go Top (First, MoveFirst) when a Scope is Set

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Go Top (First, MoveFirst) when a Scope is Set  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Go Top (First, MoveFirst) when a Scope is Set Advantage Concepts master\_Go\_top\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Go Top (First, MoveFirst) when a Scope is Set  Advantage Concepts |  |  |  |  |

With an index scope set, a Go Top operation causes a Seek for the index [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) Jones to occur, in a single operation. A Go Top with an index scope set is very fast.

With a record filter set, a Go Top first goes to the top of the index (the Abbot key, for instance). Then a series of sequential skips occur in the index until the first Jones key is found. The number of skips depends on the number of keys in the index between Abbot and Jones. Therefore, many operations may occur. A Go Top with an index scope is extremely fast relative to a traditional record filter.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.htm)