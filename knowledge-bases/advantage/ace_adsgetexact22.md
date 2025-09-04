AdsGetExact22




Advantage Database Server 12  

AdsGetExact22

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetExact22  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetExact22 Advantage Client Engine ace\_Adsgetexact22 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetExact22  Advantage Client Engine |  |  |  |  |

Retrieves the "exact" setting

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetExact22 (ADSHANDLE hObj,  UNSIGNED16 \*pbExact); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of a table or connection. If this is 0, the result is the same as calling AdsGetExact. |
| pbExact (O) | Returns the current "exact" setting. |

Remarks

If a connection handle is specified in hObj, AdsGetExact22 returns the "exact" setting of the connection. The connection's "exact" setting is the default "exact" setting for tables that will be opened in the future on the specified connection. The connection's "exact" setting also affects string comparisons in index expressions in indexes created on tables opened on the connection.

If a table handle is specified in hObj, AdsGetExact22 returns the "exact" setting of the table. The "exact" setting of the table affects string comparisons in traditional record filters set via AdsSetFilter and string comparisons in Advantage Optimized Filters set via AdsSetAOF.

If 0 (zero) is specified in hObj, AdsGetExact22 is equivalent to AdsGetExact which returns the default "exact" settings used on new connections.

Note AdsGetExact22 expands the functionality available in AdsGetExact with the addition of a parameter for specifying a table or connection. Since a new parameter was added, a new API had to be created. The "22" indicates the Advantage Client Engine version (i.e., version 2.2) in which this new supplementary API was first available.

Example

[Click Here](ace_more_examples.htm#adsgetexact22_example)

See Also

[AdsSetExact22](ace_adssetexact22.htm)

[AdsSetFilter](ace_adssetfilter.htm)

[AdsSetAOF](ace_adssetaof.htm)

[AdsSetExact](ace_adssetexact.htm)