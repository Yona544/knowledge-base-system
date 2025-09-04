AdsFactory.CreateCommand




Advantage Database Server 12  

AdsFactory.CreateCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFactory.CreateCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsFactory.CreateCommand Advantage .NET Data Provider dotnet\_Adsfactory\_createcommand Advantage .NET Data Provider > AdsFactory Class > AdsFactory Methods > AdsFactory.CreateCommand / Dear Support Staff, |  |
| AdsFactory.CreateCommand  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsCommand object as a strongly typed DbCommand instance.

public DbCommand CreateCommand();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbCommand adsCmd = adsFact.CreateCommand();

See Also

[AdsCommand](dotnet_adscommand.htm)