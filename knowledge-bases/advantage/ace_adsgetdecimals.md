AdsGetDecimals




Advantage Database Server 12  

AdsGetDecimals

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDecimals  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDecimals Advantage Client Engine ace\_Adsgetdecimals Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDecimals  Advantage Client Engine |  |  |  |  |

Retrieves the decimals setting

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDecimals (UNSIGNED16 \*pusDecimals); |

Parameters

|  |  |
| --- | --- |
| pusDecimals (O) | Returns the current decimals setting. |

Remarks

AdsGetDecimals will return the current decimals setting. The value returned is either the default or the latest value set through the [AdsSetDecimals](ace_adssetdecimals.htm) function.

AdsGetDecimals is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsgetdecimalsexample)

See Also

[AdsSetDecimals](ace_adssetdecimals.htm)

[AdsCreateIndex](ace_adscreateindex.htm)