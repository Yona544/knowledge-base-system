system.subscriptions




Advantage Database Server 12  

system.subscriptions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.subscriptions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.subscriptions Advantage SQL Engine master\_System\_subscriptions Advantage SQL > System Views > Views > system.subscriptions / Dear Support Staff, |  |
| system.subscriptions  Advantage SQL Engine |  |  |  |  |

Contains one row for each subscription in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Subscription name. |
| Publication | Character | 200 | The publication this subscription is using. |
| Target | Character | 260 | The path of the target data dictionary. |
| Target\_UserName | Character | 200 | The username used by Advantage Database Server when connecting to the target data dictionary. |
| Replication\_Queue | Character | 260 | The table used to store pending replication updates. |
| Forward | Logical | 1 | Flag that indicates if replication updates are forwarded. |
| Enabled | Logical | 1 | Flag that indicates if the subscription is enabled. |
| Comment | Memo | Variable | The description of the subscription. |
| Options | Integer | 4 | The options used when creating the subscription. See [sp\_CreateSubscription](master_sp_createsubscription.htm). |
| User\_Defined\_Prop | Binary | Variable | The user defined property. |
| Paused | Logical | 1 | Flag that indicates if the subscription is paused. |
| TCP/IP | Logical | 1 | Flag that indicates if TCP/IP communication is enabled |
| UDP/IP | Logical | 1 | Flag that indicates if UDP/IP communication is enabled |
| IPX | Logical | 1 | Flag that indicates if IPX communication is enabled |