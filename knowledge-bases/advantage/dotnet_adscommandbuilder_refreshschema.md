AdsCommandBuilder.RefreshSchema




Advantage Database Server 12  

AdsCommandBuilder.RefreshSchema

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.RefreshSchema  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.RefreshSchema Advantage .NET Data Provider dotnet\_Adscommandbuilder\_refreshschema Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Methods > AdsCommandBuilder.RefreshSchema / Dear Support Staff, |  |
| AdsCommandBuilder.RefreshSchema  Advantage .NET Data Provider |  |  |  |  |

Refreshes the database schema information used to generate INSERT, UPDATE, or DELETE statements.

public void RefreshSchema();

Remarks

An application should call RefreshSchema whenever the SelectCommand value of the [AdsDataAdapter](dotnet_adsdataadapter.htm) associated with the AdsCommandBuilder changes. The SelectCommand is not associated directly with the AdsCommandBuilder, so it has no way of automatically detecting when it is changed.