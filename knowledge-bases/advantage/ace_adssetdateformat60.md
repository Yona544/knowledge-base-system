AdsSetDateFormat60




Advantage Database Server 12  

AdsSetDateFormat60

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetDateFormat60  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetDateFormat60 Advantage Client Engine ace\_Adssetdateformat60 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetDateFormat60  Advantage Client Engine |  |  |  |  |

Specifies the date format for dates represented as character strings for a given connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetDateFormat60( ADSHANDLE hConn, UNSIGNED8 \*pucFormat ); |

Parameters

|  |  |
| --- | --- |
| hConn (I) | Handle of connection to set the date format on. If this is 0, it is the same as calling [AdsSetDateFormat](ace_adssetdateformat.htm). |
| pucFormat (I) | Specifies the date format to be set. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MMDDYYYY"). The default value is "MM/DD/YYYY". |

Remarks

AdsSetDateFormat60 can be used to set the date format for a specific connection. This setting affects how the Advantage Client Engine interprets date strings passed to the Advantage Client Engine from the calling application. It also defines how the Advantage Client Engine formats dates passed back from the Advantage Client Engine to the calling application. AdsSetDateFormat60 can be used to specify separators in the date format. For example, "DD/MM/YYYY" and "YYYY-MM-DD" are both valid date formats.

See Also

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsGetDateFormat60](ace_adsgetdateformat60.htm)

[AdsSetEpoch](ace_adssetepoch.htm)

[AdsGetDate](ace_adsgetdate.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSetScope](ace_adssetscope.htm)

[AdsSetDate](ace_adssetdate.htm)