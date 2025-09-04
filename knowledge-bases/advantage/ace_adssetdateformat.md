AdsSetDateFormat




Advantage Database Server 12  

AdsSetDateFormat

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDateFormat  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDateFormat Advantage Client Engine ace\_Adssetdateformat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDateFormat  Advantage Client Engine |  |  |  |  |

Specifies the date format for dates represented as character strings

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDateFormat (UNSIGNED8 \*pucFormat); |

Parameters

|  |  |
| --- | --- |
| pucFormat (I) | Specifies the date format to be set. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MMDDYYYY"). The default value is "MM/DD/YYYY". |

Remarks

AdsSetDateFormat analyzes the format specified by pucFormat and determines the placement as well as the correct number of digits for the day, month, and year.

AdsSetDateFormat is a global setting that affects the behavior of the entire application. This allows control of date formatting for applications being used internationally.

This setting affects how the Advantage Client Engine interprets all date strings passed to the Advantage Client Engine from the calling application. It also defines how the Advantage Client Engine formats all dates passed back from the Advantage Client Engine to the calling application. AdsSetDateFormat can also be used to specify separators in the date format. For example, "DD/MM/YYYY" and "DD-MM-YYYY" are both valid date formats.

Example

[Click Here](ace_examples.htm#adssetdateformatexample)

See Also

[AdsGetDateFormat](ace_adsgetdateformat.htm)

[AdsGetDate](ace_adsgetdate.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSetScope](ace_adssetscope.htm)

[AdsSetDate](ace_adssetdate.htm)

[AdsSetDateFormat60](ace_adssetdateformat60.htm)

[AdsSetEpoch](ace_adssetepoch.htm)