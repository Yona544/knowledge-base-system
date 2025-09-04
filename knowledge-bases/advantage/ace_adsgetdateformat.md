AdsGetDateFormat




Advantage Database Server 12  

AdsGetDateFormat

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDateFormat  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDateFormat Advantage Client Engine ace\_Adsgetdateformat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDateFormat  Advantage Client Engine |  |  |  |  |

Retrieves the current date format

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDateFormat (UNSIGNED8 \*pucFormat,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| pucFormat (O) | Contains the returned date format string. |
| pusLen (I/O) | Length of the buffer on input, amount of data stored on output. |

Remarks

AdsGetDateFormat returns the current date format or the date format defined by AdsSetDateFormat.

AdsGetDateFormat is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adsgetdateformatexample)

See Also

[AdsGetDate](ace_adsgetdate.htm)

[AdsGetDateFormat60](ace_adsgetdateformat60.htm)

[AdsGetEpoch](ace_adsgetepoch.htm)

[AdsSetDate](ace_adssetdate.htm)

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsSetDateFormat60](ace_adssetdateformat60.htm)

[AdsSetEpoch](ace_adssetepoch.htm)