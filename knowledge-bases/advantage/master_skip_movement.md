Skip (Next, Prior, MoveBy, MoveNext, MovePrevious)




Advantage Database Server 12  

Skip (Next, Prior, MoveBy, MoveNext, MovePrevious)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Skip (Next, Prior, MoveBy, MoveNext, MovePrevious)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Skip (Next, Prior, MoveBy, MoveNext, MovePrevious) Advantage Concepts master\_Skip\_movement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Skip (Next, Prior, MoveBy, MoveNext, MovePrevious)  Advantage Concepts |  |  |  |  |

Skip will cause a re-positioning to N records from the current record position, where N is the number of records specified in the Skip operation. The number of records to skip can be either a positive or a negative number. If no index files are open, no index order is active, or no index order was specified in the Skip operation, the movement will occur in "natural" record number order. If an index order is active or is specified, then Skip will move in the logical index order. For example, if the index order is on "name", and you are currently positioned on the "Jones" record, a Skip 1 operation will re-position to the next "Jones" record in the table as determined by the active or specified index order.