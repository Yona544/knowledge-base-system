AdsCommandBuilder.QuotePrefix




Advantage Database Server 12  

AdsCommandBuilder.QuotePrefix

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.QuotePrefix  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.QuotePrefix Advantage .NET Data Provider dotnet\_Adscommandbuilder\_quoteprefix Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Properties > AdsCommandBuilder.QuotePrefix / Dear Support Staff, |  |
| AdsCommandBuilder.QuotePrefix  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the beginning character to use when for delimiting Advantage object names (e.g., tables and columns).

public string QuotePrefix {get; set;}

Remarks

Advantage table names and column names can contain special characters such as spaces. If so, they must be delimited by either double quotes or by square brackets in order to be recognized correctly by the SQL parser. By default the QuotePrefix property is a left square bracket ([). It should not be necessary to set this property.

See Also

[AdsCommandBuilder.QuoteSuffix](dotnet_adscommandbuilder_quotesuffix.htm)