AdsIsFound




Advantage Database Server 12  

AdsIsFound

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsFound  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsFound Advantage Client Engine ace\_Adsisfound Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsFound  Advantage Client Engine |  |  |  |  |

Returns True if the last seek or locate function call was successful

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsFound (ADSHANDLE hTable,  UNSIGNED16 \*pbFound); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pbFound (O) | Return True if record found. |

Remarks

The found flag will not remain set after other movement in a table. Therefore, it is only guaranteed to be valid immediately following a call to AdsSeek, AdsLocate, or AdsContinue.

Example

[Click Here](ace_examples.htm#adsisfoundexample)

See Also

[AdsSeek](ace_adsseek.htm)

[AdsLocate](ace_adslocate.htm)

[AdsContinue](ace_adscontinue.htm)