AdsSetExact




Advantage Database Server 12  

AdsSetExact

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetExact  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetExact Advantage Client Engine ace\_Adssetexact Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetExact  Advantage Client Engine |  |  |  |  |

Affects how string comparisons are performed with certain relational operators

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetExact( UNSIGNED16 bIgnoreSpaces ); |

Parameters

|  |  |
| --- | --- |
| bIgnoreSpaces (I) | A non-zero value causes string comparisons with certain relational operators to ignore trailing spaces. The default is False. |

Remarks

The AdsSetExact setting affects how string comparisons are performed with the relational operators =, >, <, >=, and <=. The exact equal, ==, operator is not affected by this setting. In general, if the AdsSetExact setting is True, trailing spaces are ignored during the comparison. The AdsSetExact setting is not that simple, however. It is somewhat complex and affects the various relational operators differently. See [Expression Engine Operators](master_expression_engine_operators.htm) for detailed information on how the AdsSetExact setting affects relational operators.

AdsSetExact will affect string comparisons for all currently opened tables and all tables opened in the future for all connections. Changing the exact setting via AdsSetExact has an immediate effect on all string comparisons in existing traditional record filters set via AdsSetFilter, but has no effect on existing Advantage Optimized Filters set via AdsSetAOF until AdsRefreshAOF is called. Changing the set exact setting via AdsSetExact also affects all string comparisons in index expressions.

Note AdsSetExact does not affect [AdsSeek](ace_adsseek.htm).

 

Note AdsSetExact affects all tables on all connections. See [AdsSetExact22](ace_adssetexact22.htm) for information on how to set "exact" on the individual table or connection.

Example

[Click Here](ace_examples.htm#adssetexactexample)

See Also

[AdsSetExact22](ace_adssetexact22.htm)

[AdsGetExact22](ace_adsgetexact22.htm)

[AdsGetExact](ace_adsgetexact.htm)

[AdsSetFilter](ace_adssetfilter.htm)

[AdsSetAOF](ace_adssetaof.htm)