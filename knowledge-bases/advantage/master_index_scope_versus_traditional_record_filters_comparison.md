Index Scope Versus Traditional Record Filters Comparison




Advantage Database Server 12  

Index Scope versus Traditional Record Filters Comparison

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Scope versus Traditional Record Filters Comparison  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Index Scope versus Traditional Record Filters Comparison Advantage Database Server master\_Index\_scope\_versus\_traditional\_record\_filters\_comparison Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Index Scope versus Traditional Record Filters Comparison  Advantage Database Server |  |  |  |  |

In this comparison, let the currently active or selected index [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) expression be "name". For the cases when an index scope is described, let the top scope value be Jones and the bottom scope value be Phillips. For the cases when a record filter is described, let the filter expression be "name >= Jones .AND. name <= Phillips." Both the index scope and record filter include the same number of records within their boundaries. The following is what actually occurs for specific operations.

Go Top

With an index scope set, a Go Top operation causes a Seek for the index key Jones to occur, in a single operation. A Go Top with an index scope set is very fast.

With a record filter set, a Go Top first goes to the top of the index (the Abbot key, for instance). Then a series of sequential skips occur in the index until the first Jones key is found. The number of skips depends on the number of keys in the index between Abbot and Jones. Therefore, many operations may occur. A Go Top with an index scope is extremely fast relative to a traditional record filter.

Go Bottom

With an index scope set, a Go Bottom causes a Seek for the index key Phillipt (note that it is Phillipt rather than Phillips). Then a negative Skip is performed to position the user on the last of any Phillips keys. Therefore, two operations occur. A Go Bottom with an index scope set is very fast.

With a record filter set, a Go Bottom first goes to the bottom of the index (the Zimmerman key, for instance). Then a series of sequential negative Skips occur in the index until a Phillips key is found. The number of negative Skips depends on the number of keys in the index between Zimmerman and Phillips. Thus, many operations occur. A Go Bottom with an index scope is extremely fast relative to a traditional record filter.

Seek

If the key being Seeked is within the index scope or record filter boundaries (the Nelson key, for instance), then index scope and record filter performance is identical.

If the key being Seeked is before the top index scope or record filter boundary (the Brown key, for instance), index scopes are much faster than traditional record filters. With index scopes, a Seek to the top of the scope (the first Jones key) or an immediate repositioning to the end of file will occur, depending if Softseek is set. With traditional record filters, a series of skips will be performed (from the Brown key to the Jones key) before the Softseek setting is accounted for.

If the key being Seeked is after the bottom index scope or record filter boundary (the Smith key, for instance), then index scopes are once again faster than traditional record filters. With index scopes, an immediate repositioning to the end of file will occur. With record filters, a series of skips will be performed (starting at the Smith key) until the end of file is reached.

Skip

Performance of Skips is similar to Seeks. If the Skip occurs within the index scope or record filter boundaries, index scope and record filter performance is identical. If the Skip occurs outside of the index scope or record filter boundaries, index scopes are again much faster than record filters. See the Seek section above for a full explanation of how Skips work like Seeks when outside the index scope or record filter boundaries.

Go To

Regardless of which record you are positioning to, Go To performance is identical when using index scopes and record filters because Go To ignores both scopes and filters.