Modifying Subscription Information




Advantage Database Server 12  

Modifying Subscription Information

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Modifying Subscription Information  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Modifying Subscription Information Advantage Concepts master\_Modifying\_subscription\_information Advantage Concepts > Advantage Functionality > Replication > Modifying Subscription Information / Dear Support Staff, |  |
| Modifying Subscription Information  Advantage Concepts |  |  |  |  |

When modifying subscription and publication information for replication, the information will normally be refreshed at the server at the same time. However, if the subscription is in use, it is possible that cached information on the server cannot be refreshed. Therefore, for consistent results, it is best not to modify and create subscriptions while tables are actively being edited.

Note If a table is added to a subscription while that table is open, it will not start being replicated until all instances are closed and re-opened.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)