AdsDataAdapter Constructor( AdsCommand )




Advantage Database Server 12  

AdsDataAdapter Constructor( AdsCommand )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter Constructor( AdsCommand )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter Constructor( AdsCommand ) Advantage .NET Data Provider dotnet\_Adsdataadapter\_constructor\_adscommand\_ Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Constructors > AdsDataAdapter Constructor( AdsCommand ) / Dear Support Staff, |  |
| AdsDataAdapter Constructor( AdsCommand )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given command object.

public AdsDataAdapter( AdsCommand command );

Remarks

The provided [AdsCommand](dotnet_adscommand.htm) object is stored as the [SelectCommand](dotnet_adsdataadapter_selectcommand.htm) property. The command is not cloned; the AdsDataAdapter simply keeps a reference to the command object.