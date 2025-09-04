AdsExtendedReader.PartialMatch




Advantage Database Server 12  

AdsExtendedReader.PartialMatch

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.PartialMatch  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.PartialMatch Advantage .NET Data Provider dotnet\_Adsextendedreader\_partialmatch Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.PartialMatch / Dear Support Staff, |  |
| AdsExtendedReader.PartialMatch  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the Partial Match property used by SetRange, Seek and Filter.

public bool PartialMatch{ get; set; }

Remarks

This property controls the behavior of SetRange, Seek, and Filter. The default value is true.

For Filter, if partial match is true, string comparisons with certain relational operators will ignore trailing spaces. See the Relational Operators section of [Expression Engine Operators](master_expression_engine_operators.htm) for details.

For Seek, PartialMatch allows partial matching of a scope or seek value. For example, a Seek on a last name index with a seek value of "Smit" would fail to find "Smith" if PartialMatch is false, but succeed if PartialMatch is true.

Similarly for SetRange, a bottom scope of "S" would exclude "Smith" if PartialMatch is false, but will include all lastnames beginning with "S" if PartialMatch is true.

See Also

[SetRange](dotnet_adsextendedreader_setrange.htm)

[Seek](dotnet_adsextendedreader_seek.htm)

[Filter](dotnet_adsextendedreader_filter.htm)