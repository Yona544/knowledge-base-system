Go Bottom (Last, MoveLast) when a Scope is Set




Advantage Database Server 12  

Go Bottom (Last, MoveLast) when a Scope is Set

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Go Bottom (Last, MoveLast) when a Scope is Set  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Go Bottom (Last, MoveLast) when a Scope is Set Advantage Concepts master\_Go\_bottom\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Go Bottom (Last, MoveLast) when a Scope is Set  Advantage Concepts |  |  |  |  |

With an index scope set, a Go Bottom causes a Seek for the index [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) Phillipt (note that it is Phillipt rather than Phillips). Then a negative Skip is performed to position the user on the last of any Phillips keys. Therefore, two operations occur. A Go Bottom with an index scope set is very fast.

With a record filter set, a Go Bottom first goes to the bottom of the index (the Zimmerman key, for instance). Then a series of sequential negative Skips occur in the index until a Phillips key is found. The number of negative Skips depends on the number of keys in the index between Zimmerman and Phillips. Thus, many operations occur. A Go Bottom with an index scope is extremely fast relative to a traditional record filter.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.htm)