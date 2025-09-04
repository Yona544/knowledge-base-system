AdsSetEpoch




Advantage Database Server 12  

AdsSetEpoch

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetEpoch  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetEpoch Advantage Client Engine ace\_Adssetepoch Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetEpoch  Advantage Client Engine |  |  |  |  |

Sets the default epoch to determine how dates without century digits are interpreted

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetEpoch (UNSIGNED16 usEpoch); |

Parameters

|  |  |
| --- | --- |
| usEpoch (I) | Epoch setting |

Remarks

AdsSetEpoch determines how date strings are interpreted that contain only two-year digits. For example, if a date is given as "5/15/98", then the usEpoch value will be used to determine the full four-digit year. If a date is given as "5/15/1998", then the usEpoch setting is not used. AdsSetEpoch affects all currently connected Advantage servers, and will be sent to any Advantage servers with which new connections are established.

The usEpoch setting will be interpreted as the 100-year range for the two digit year. For example, if the usEpoch value is 1970, a two digit year of "96" will be interpreted as 1996, while a two digit year of "12" will be interpreted as 2012.

The default epoch value is 1900. Dates are physically stored in the table with the century information. Thus, changing the epoch setting does not affect dates in existing tables.

AdsSetEpoch is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.htm#adssetepochexample)

See Also

[AdsGetEpoch](ace_adsgetepoch.htm)

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsGetDateFormat](ace_adsgetdateformat.htm)

[AdsSetDate](ace_adssetdate.htm)