Connection Handles




Advantage Database Server 12  

Connection Handles

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connection Handles  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Connection Handles Advantage Client Engine ace\_Connection\_handles Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Connection Handles  Advantage Client Engine |  |  |  |  |

The idea of controllable connections to Advantage servers has not been available before. This capability exposes new functionality for Advantage. A connection handle is a reference to a single communication link with the Advantage server. These Advantage connections can be controlled explicitly, but it is also possible to let the Advantage Client Engine control connections. To allow the Advantage Client Engine to control server connections, specify a zero for the connection parameter on calls to [AdsOpenTable](ace_adsopentable.htm), [AdsCreateTable](ace_adscreatetable.htm) and the transaction functions ([AdsBeginTransaction](ace_adsbegintransaction.htm), [AdsCommitTransaction](ace_adscommittransaction.htm), [AdsRollbackTransaction](ace_adsrollbacktransaction.htm), and [AdsInTransaction](ace_adsintransaction.htm)).

To control Advantage server connections explicitly, use the functions [AdsConnect](ace_adsconnect.htm), [AdsDisconnect](ace_adsdisconnect.htm), and [AdsFindConnection](ace_adsfindconnection.htm). The availability of these functions allows an application to obtain multiple connections to the same Advantage server. Because Advantage Server transactions are performed by connection, it is now possible for an application to control multiple independent transactions at one time.

Note Although multiple transactions are now possible from one client on an Advantage Server, record visibility through the separate table handles on the separate connections is exactly as if the transactions were taking place from different client machines. Therefore, if a record in one transaction is updated, the other transaction will not see the change until it is committed.

[AdsApplicationExit](ace_adsapplicationexit.htm) will close all implicit and all explicit connections. In addition, [AdsDisconnect](ace_adsdisconnect.htm) can be used to close connections explicitly.