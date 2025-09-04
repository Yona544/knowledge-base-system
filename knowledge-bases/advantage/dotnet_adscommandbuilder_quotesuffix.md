AdsCommandBuilder.QuoteSuffix




Advantage Database Server 12  

AdsCommandBuilder.QuoteSuffix

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.QuoteSuffix  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.QuoteSuffix Advantage .NET Data Provider dotnet\_Adscommandbuilder\_quotesuffix Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Properties > AdsCommandBuilder.QuoteSuffix / Dear Support Staff, |  |
| AdsCommandBuilder.QuoteSuffix  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the ending character to use when for delimiting Advantage object names (e.g., tables and columns).

public string QuoteSuffix {get; set;}

Remarks

Advantage table names and column names can contain special characters such as spaces. If so, they must be delimited by either double quotes or by square brackets in order to be recognized correctly by the SQL parser. By default the QuoteSuffix property is a right square bracket (]). It should not be necessary to set this property.

See Also

[QuotePrefix](dotnet_adscommandbuilder_quoteprefix.htm)