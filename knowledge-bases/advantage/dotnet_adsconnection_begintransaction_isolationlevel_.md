AdsConnection.BeginTransaction( IsolationLevel )




Advantage Database Server 12  

AdsConnection.BeginTransaction( IsolationLevel )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.BeginTransaction( IsolationLevel )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.BeginTransaction( IsolationLevel ) Advantage .NET Data Provider dotnet\_Adsconnection\_begintransaction\_isolationlevel\_ Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.BeginTransaction( IsolationLevel ) / Dear Support Staff, |  |
| AdsConnection.BeginTransaction( IsolationLevel )  Advantage .NET Data Provider |  |  |  |  |

Begins a database transaction with the specified isolation level.

public AdsTransaction BeginTransaction( IsolationLevel iso );

Remarks

This returns an [AdsTransaction](dotnet_adstransaction.htm) object representing the new transaction. Currently, the isolation level must be IsolationLevel.ReadCommitted. Advantage currently does not support other isolation levels. This method will throw a NotSupportedException if a different isolation level is specified.

Distributed transactions are not supported. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started. Note that Advantage Local Server does not support transactions. If the ServerType property ([AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)) is LOCAL, no transaction will actually be started, although an AdsTransaction object will still be returned. Transactions can be nested by calling BeginTransaction inside of an existing transaction.

Example

see [AdsConnection.BeginTransaction()](dotnet_adsconnection_begintransaction_.htm)

See Also

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.htm)

[AdsTransaction](dotnet_adstransaction.htm)