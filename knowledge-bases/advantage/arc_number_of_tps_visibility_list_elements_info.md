Number of TPS Visibility List Elements Info




Advantage Database Server 12  

Number of TPS Visibility List Elements Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Number of TPS Visibility List Elements Info |  |  | Feedback on: Advantage Database Server 12 - Number of TPS Visibility List Elements Info arc\_Number\_of\_tps\_visibility\_list\_elements\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Number of TPS Visibility List Elements Info |  |  |  |  |

While changes are being made to the database, the Advantage TPS hides those updates from other users until the data is committed. The uncommitted data is visible only to the application performing the transaction. Other applications view the data as it was before the transaction began. If the transaction is rolled back, the uncommitted data is never seen by any users other than the one who was performing the transaction. If the transaction is committed, the updated data becomes visible to all users at one time. The TPS Visibility List Elements are used to provide this "data hiding" during a transaction. The TPS Visibility List is specific to changes made to database files and their associated index files.