5040 AE\_NO\_WORKAREA




Advantage Database Server 12  

5040 AE\_NO\_WORKAREA

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5040 AE\_NO\_WORKAREA  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5040 AE\_NO\_WORKAREA Advantage Error Guide error\_5040\_ae\_no\_workarea Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5040 AE\_NO\_WORKAREA  Advantage Error Guide |  |  |  |  |

This error is no longer applicable since the 6.1 release of Advantage clients. Prior to the 6.1 release, this error is returned when the maximum number of tables has been opened for this connection. The maximum number of tables open at any one time per connection prior to the 6.1 release is 255.

Try closing a table before opening another, or create another connection and open the tables on that connection.