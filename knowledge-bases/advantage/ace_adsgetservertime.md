AdsGetServerTime




Advantage Database Server 12  

AdsGetServerTime

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetServerTime  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetServerTime Advantage Client Engine ace\_Adsgetservertime Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetServerTime  Advantage Client Engine |  |  |  |  |

Retrieves the current time and date from the server via the Advantage Database Server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetServerTime ( ADSHANDLE hConnect,  UNSIGNED8 \*pucDateBuf,  UNSIGNED16 \*pusDateBufLen,  SIGNED32 \*plTime,  UNSIGNED8 \*pucTimeBuf,  UNSIGNED16 \*pusTimeBufLen ); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of connection to server. |
| pucDateBuf (O) | Return the date on the server in this buffer. |
| pusDateBufLen (I/O) | Length of given date buffer on input, length of returned date data on output. |
| plTime (O) | Return the time value in milliseconds since midnight. |
| pucTimeBuf (O) | Return the time string on the server in the HH:MM:SS AM/PM format in this buffer. |
| pusTimeBufLen (I/O) | Length of given time buffer on input, length of returned time string on output. |

Remarks

AdsGetServerTime returns the current date and time from the server. The time is returned in two formats, as the number of milliseconds since midnight and as a time value formatted in 12-hour time with hours, minutes, seconds and an AM/PM indicator. The date is returned according to the date format set in [AdsSetDateFormat](ace_adssetdateformat.htm). AdsGetServerTime is useful if the Advantage client application is running at a site that is in a different time zone than where the data is located and is being accessed by the Advantage Database Server. When Advantage is used in a WAN environment or is being used with the Advantage Internet Server, the Advantage client and Advantage server will often be located in different time zones. This API allows time, date, and timestamp fields to be populated with a consistent date and time, that is, the date and time of the server location.

See Also

[AdsSetDateFormat](ace_adssetdateformat.htm)