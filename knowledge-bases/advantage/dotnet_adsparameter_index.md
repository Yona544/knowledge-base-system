AdsParameter.Index




Advantage Database Server 12  

AdsParameter.Index

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.Index  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.Index Advantage .NET Data Provider dotnet\_Adsparameter\_index Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.Index / Dear Support Staff, |  |
| AdsParameter.Index  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the one-based parameter index number of unnamed parameters.

public int Index { get; set; }

Remarks

When using unnamed parameters (represented by a question mark) in an SQL statement, the AdsParameter.Index property should be set to the one-based ordinal of the parameter as it appears in the SQL statement.