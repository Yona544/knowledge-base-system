Index Scopes (Ranges)




Advantage Database Server 12  

Index Scopes (Ranges)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Scopes (Ranges)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Index Scopes (Ranges) Advantage Concepts master\_Index\_scopes\_ranges Advantage Concepts > Advantage ISAM Concepts > Index Scopes (Ranges) / Dear Support Staff, |  |
| Index Scopes (Ranges)  Advantage Concepts |  |  |  |  |

The Advantage TDataSet Descendant equivalent of the generic Advantage "Scope" concept is a called a "Range". The Advantage "top" scope value is equivalent to the TDataSet Descendant "start" range value. The Advantage "bottom" scope value is equivalent to the TDataSet Descendant "end" range value.

An index scope allows you to view a subset of records in an index. Top and bottom index [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) limits may be defined to retrieve only those records contained within the specified index scope range. The range acts as a temporary view of an index, allowing extremely fast retrieval of only those records meeting the index scope range value(s). The range values are determined based on the currently active or specified index.

A Top value and Bottom value are assigned to define the value range. The Top and Bottom values may be the same value. Once the Top and Bottom values are set, only those records within the range are visible.

Index scopes should be used when the currently active or specified index key expression contains the value(s) that are to be the limits of the view of the table. If the value(s) of the limits of the view are not contained in an index key expression, index scopes cannot be used. Instead, record filters or Advantage Optimized Filters must be used. For example, if the expression to be used to limit the view of the table is "state >= Idaho", and if the active or selected index key expression is not state, then a traditional record filter or Advantage Optimized Filter must be used rather than an index scope.

Note Index scope boundary checking is performed on the client and traditional record filters and Advantage Optimized Filters are handled on the server. However, the client versus server issue is not the relevant performance factor with index scopes versus filters. The way index scope functionality is implemented makes it a superior method to view a subset of records compared to a traditional record filter or an Advantage Optimized Filter.

To understand the differences between index scopes and traditional record filters, a comparison is outlined below. In this comparison, let the currently active or selected index key expression be "name". For the cases when an index scope is described, let the top scope value be Jones and the bottom scope value be Phillips. For the cases when a record filter is described, let the filter expression be "name >= Jones .AND. name <= Phillips." Both the index scope and record filter include the same number of records within their boundaries. The following is what actually occurs for specific operations.

[Go Top (First, MoveFirst) when a Scope is Set](master_go_top_index.htm)

[Go Bottom (Last, MoveLast) when a Scope is Set](master_go_bottom_index.htm)

[Seek (FindKey, FindNearest, GotoKey, GotoNearest) when a Scope is Set](master_seek_index.htm)

[Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set](master_skip_index.htm)

[Go To (GotoBookmark, Bookmark) when a Scope is Set](master_go_to_index.htm)