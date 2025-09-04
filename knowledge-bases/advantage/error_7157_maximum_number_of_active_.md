7157 Maximum number of active Unicode collators for a connection have been exceeded.




Advantage Database Server 12  

7157 Maximum number of active Unicode collators for a connection have been exceeded

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7157 Maximum number of active Unicode collators for a connection have been exceeded  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7157 Maximum number of active Unicode collators for a connection have been exceeded Advantage Error Guide error\_7157\_Maximum\_number\_of\_active\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7157 Maximum number of active Unicode collators for a connection have been exceeded  Advantage Error Guide |  |  |  |  |

Each connection in Advantage server is allowed to use 128 distinct Unicode collation locales. For example, if two index files with en\_US collation locale and three index files with de\_DE collation locale are opened on a connection, then the connection is using two distinct Unicode collation locale. The opened Unicode collators are cached on the connection until the connection is closed. If the connection already has 128 Unicode collators active, then it will not be able to use index files built with Unicode locale that is not the same as one of the already opened collators.