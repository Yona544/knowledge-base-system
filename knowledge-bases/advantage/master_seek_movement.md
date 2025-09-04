Seek (FindKey, FindNearest, GotoKey, GotoNearest)




Advantage Database Server 12  

Seek (FindKey, FindNearest, GotoKey, GotoNearest)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Seek (FindKey, FindNearest, GotoKey, GotoNearest)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Seek (FindKey, FindNearest, GotoKey, GotoNearest) Advantage Concepts master\_Seek\_movement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Seek (FindKey, FindNearest, GotoKey, GotoNearest)  Advantage Concepts |  |  |  |  |

Seek is a fast and efficient way to search for data in the active or specified index order. Seek will position to the record containing the data if it is found. For example, if the index order is on "name", a Seek for "Schmidt" will position to the record containing the first "Schmidt" name. When performing a Seek with the Advantage client/server engine (Advantage Database Server), the operation is very fast since all index page reads and the index traversal are performed at the server. There is no network traffic generated related to the index. The client sends only the Seek request with the key value to search for, and the server sends back the Seek status and resulting record.