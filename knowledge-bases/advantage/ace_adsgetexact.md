AdsGetExact




Advantage Database Server 12  

AdsGetExact

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetExact  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetExact Advantage Client Engine ace\_Adsgetexact Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetExact  Advantage Client Engine |  |  |  |  |

Retrieves the "exact" setting

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetExact (UNSIGNED16 \*pbExact); |

Parameters

|  |  |
| --- | --- |
| pbExact (O) | Return the current "exact" setting. |

Remarks

AdsGetExact returns the global "exact" setting for the current application. The global "exact" setting is the default "exact" setting for any new connections. The "exact" setting affects how string comparisons are performed with the relational operators =, >, <, >=, and <=.

Example

[Click Here](ace_examples.htm#adsgetexactexample)

See Also

[AdsSetExact](ace_adssetexact.htm)

[AdsSetFilter](ace_adssetfilter.htm)

[AdsSetAOF](ace_adssetaof.htm)

[AdsGetExact22](ace_adsgetexact22.htm)