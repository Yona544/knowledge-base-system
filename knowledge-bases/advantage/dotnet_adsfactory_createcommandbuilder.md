AdsFactory.CreateCommandBuilder




Advantage Database Server 12  

AdsFactory.CreateCommandBuilder

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFactory.CreateCommandBuilder  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsFactory.CreateCommandBuilder Advantage .NET Data Provider dotnet\_Adsfactory\_createcommandbuilder Advantage .NET Data Provider > AdsFactory Class > AdsFactory Methods > AdsFactory.CreateCommandBuilder / Dear Support Staff, |  |
| AdsFactory.CreateCommandBuilder  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsCommandBuilder object as a strongly typed DbCommandBuilder instance.

public DbCommandBuilder CreateCommandBuilder();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbCommandBuilder adsCmdBldr = adsFact.CreateCommandBuilder();

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.htm)