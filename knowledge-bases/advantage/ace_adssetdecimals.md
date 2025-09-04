AdsSetDecimals




Advantage Database Server 12  

AdsSetDecimals

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDecimals  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDecimals Advantage Client Engine ace\_Adssetdecimals Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDecimals  Advantage Client Engine |  |  |  |  |

Controls the resulting number of decimal places in a division, modulus, or exponentiation operation in an index or filter expression evaluated in the expression engine

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDecimals (UNSIGNED16 usDecimals); |

Parameters

|  |  |
| --- | --- |
| usDecimals (I) | Number of decimals. The default is 2. |

Remarks

AdsSetDecimals determines the number of decimal places saved in the results of numeric functions and calculations.

AdsSetDecimals is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adssetdecimalsexample)

See Also

[AdsGetDecimals](ace_adsgetdecimals.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsSetFilter](ace_adssetfilter.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)