Go Bottom (Last, MoveLast)




Advantage Database Server 12  

Go Bottom (Last, MoveLast)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Go Bottom (Last, MoveLast)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Go Bottom (Last, MoveLast) Advantage Concepts master\_Go\_bottom\_movement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Go Bottom (Last, MoveLast)  Advantage Concepts |  |  |  |  |

Go Bottom will position to the last record in the table if no index files are open, no index order is active, or no index order was specified in the Go Bottom operation. If an index order is active or is specified, then Go Bottom will position to the last logical record in the index order. For example, if the index order is on "name", a Go Bottom will position to the record containing the last "Z" in the table. This operation can be quite time consuming if it causes an SQL static cursor to be dynamically populated. See [Populating Static Cursors](master_populating_static_cursors.htm) for details.