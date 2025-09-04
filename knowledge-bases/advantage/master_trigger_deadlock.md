Trigger Deadlock




Advantage Database Server 12  

Trigger Deadlock

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Trigger Deadlock  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Trigger Deadlock Advantage Concepts master\_Trigger\_deadlock Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Trigger Deadlock  Advantage Concepts |  |  |  |  |

Depending on how your triggers are defined, it is possible to encounter a deadlock situation. Consider a database with two tables (tableA and tableB) and two triggers (trigA and trigB). TrigA fires on tableA, and updates records in tableB. TrigB fires on tableB, and updates records in tableA.

Now if user1 updates tableA, and user2 updates tableB, it is possible for deadlock to occur, as the first user's trigger might need resources locked by user2, and user2's trigger might need resources locked by user1.

Advantage does not currently have any deadlock detection and/or recovery capabilities. It is the developer's responsibility to avoid trigger deadlock.