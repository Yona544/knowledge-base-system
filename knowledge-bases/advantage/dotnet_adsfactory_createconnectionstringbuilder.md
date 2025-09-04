AdsFactory.CreateConnectionStringBuilder




Advantage Database Server 12  

AdsFactory.CreateConnectionStringBuilder

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFactory.CreateConnectionStringBuilder  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsFactory.CreateConnectionStringBuilder Advantage .NET Data Provider dotnet\_Adsfactory\_createconnectionstringbuilder Advantage .NET Data Provider > AdsFactory Class > AdsFactory Methods > AdsFactory.CreateConnectionStringBuilder / Dear Support Staff, |  |
| AdsFactory.CreateConnectionStringBuilder  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsConnectionStringBuilder object as a strongly typed DbConnectionStringBuilder instance.

public DbConnectionStringBuilder CreateConnectionStringBuilder();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnectionStringBuilder adsCSBldr =

adsFact.CreateConnectionStringBuilder();

See Also

[AdsConnectionStringBuilder](dotnet_adsconnectionstringbuilder_class.htm)