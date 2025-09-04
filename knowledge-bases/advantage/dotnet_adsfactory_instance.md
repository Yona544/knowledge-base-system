AdsFactory.Instance




Advantage Database Server 12  

AdsFactory.Instance

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFactory.Instance  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsFactory.Instance Advantage .NET Data Provider dotnet\_Adsfactory\_instance Advantage .NET Data Provider > AdsFactory Class > AdsFactory Fields > AdsFactory.Instance / Dear Support Staff, |  |
| AdsFactory.Instance  Advantage .NET Data Provider |  |  |  |  |

Gets an instance of the AdsFactory. This can be used to retrieve strongly typed data objects.

public static readonly AdsFactory Instance;

Remarks

An application has a single instance of AdsFactory. It can be retrieved via the Instance field of the AdsFactory class. It can also be retrieved by calling DbProviderFactories.GetFactory().

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnection adsConn = adsFact.CreateConnection();