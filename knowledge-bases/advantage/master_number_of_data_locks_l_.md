Number of Data Locks (-L)




Advantage Database Server 12  

Number of Data Locks (-L)

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Number of Data Locks (-L)  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Number of Data Locks (-L) Advantage Database Server master\_Number\_of\_data\_locks\_l\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Number of Data Locks (-L)  Advantage Database Server |  |  |  |  |

Default = (40 x CONNECTIONS) data locks. Range = 1 - no upper limit.

This is the initial number of record locks, table locks, implicit header locks, and implicit index locks that can be in effect at one time. It may not be necessary to change this parameter. For a frame of reference, check the Advantage Management Utility for the Max Used number. Increase this parameter only if the Max Used Data Locks value is larger than the Configured value or more than zero Data Locks have been rejected.

The "Number of Data Locks" configuration setting on the Advantage Database Server is a "per-client" setting. That is, one data lock must be available per record, table, header, or index lock requested per Advantage client. For example, if 10 Advantage clients each have 15 records or files locked at one time, there must be at least 150 data locks configured on the Advantage Database Server.

If an Advantage application attempts to obtain a record, table, or index lock, and the configured number of data locks have already been used, the Advantage Database Server will attempt to allocate more resources to accommodate more data locks. If that allocation fails, the Advantage application which is attempting to get the lock will receive a 7007 error, Maximum number of locks exceeded, until a lock "element" becomes available. Data locks take very little memory. Setting this value to a very high number should not require much server RAM to be used.