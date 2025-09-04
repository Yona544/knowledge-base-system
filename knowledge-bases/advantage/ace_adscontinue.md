AdsContinue




Advantage Database Server 12  

AdsContinue

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsContinue  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsContinue Advantage Client Engine ace\_Adscontinue Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsContinue  Advantage Client Engine |  |  |  |  |

Continues the locate command based on a previous call to [AdsLocate](ace_adslocate.htm)

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsContinue (ADSHANDLE hTable,  UNSIGNED16 \*pbFound); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pbFound (O) | Return True if record found. |

Remarks

AdsContinue continues searching for records that pass the condition specified in [AdsLocate](ace_adslocate.htm) in the direction set by the AdsLocate function. If pbFound returns False, the table is positioned at EOF or BOF, depending on the direction of the AdsLocate.

AdsContinue performs a skip before evaluating the current record against the condition set in AdsLocate. It is unnecessary to explicitly call [AdsSkip](ace_adsskip.htm) between an AdsLocate and an AdsContinue call or between successive AdsContinue calls.

Note Since each record is read from the server for comparison against the filter, it would be faster to use [AdsSetFilter](ace_adssetfilter.htm) because the server would then perform the filtering.

Example

[Click Here](ace_examples.htm#adscontinueexample)

See Also

[AdsLocate](ace_adslocate.htm)

[AdsIsFound](ace_adsisfound.htm)