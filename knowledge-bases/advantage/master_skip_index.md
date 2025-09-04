Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set




Advantage Database Server 12  

Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set Advantage Concepts master\_Skip\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) when a Scope is Set  Advantage Concepts |  |  |  |  |

Performance of Skips is similar to Seeks. If the Skip occurs within the index scope or record filter boundaries, index scope and record filter performance is identical. If the Skip occurs outside of the index scope or record filter boundaries, index scopes are again much faster than record filters. See the [Seek](master_seek_index.htm) section for a full explanation of how Skips work like Seeks when outside the index scope or record filter boundaries.

See Also

[Index Scopes (Ranges)](master_index_scopes_ranges.htm)