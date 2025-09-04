AdsGetEpoch




Advantage Database Server 12  

AdsGetEpoch

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetEpoch  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetEpoch Advantage Client Engine ace\_Adsgetepoch Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetEpoch  Advantage Client Engine |  |  |  |  |

Retrieves the current epoch setting

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetEpoch (UNSIGNED16 \*pusEpoch); |

Parameters

|  |  |
| --- | --- |
| pusEpoch (O) | Contains the retrieved current epoch setting. |

Remarks

AdsGetEpoch will retrieve the current value of the default epoch setting for two-digit years. The epoch setting is the same for all connected Advantage servers. See [AdsSetEpoch](ace_adssetepoch.htm) for information on the epoch setting.

AdsGetEpoch is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsgetepochexample)

See Also

[AdsSetEpoch](ace_adssetepoch.htm)

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsGetDateFormat](ace_adsgetdateformat.htm)