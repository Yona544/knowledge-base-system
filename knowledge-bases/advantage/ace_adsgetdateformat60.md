AdsGetDateFormat60




Advantage Database Server 12  

AdsGetDateFormat60

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetDateFormat60  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetDateFormat60 Advantage Client Engine ace\_Adsgetdateformat60 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetDateFormat60  Advantage Client Engine |  |  |  |  |

Retrieves the current date format for a given connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetDateFormat60( ADSHANDLE hConn,  UNSIGNED8 \*pucFormat,  UNSIGNED16 \*pusLen ); |

Parameters

|  |  |
| --- | --- |
| hConn (I) | Connection to retrieve the date format from. If this is 0, it is the same as calling AdsGetDateFormat. |
| pucFormat (O) | Contains the returned date format string. |
| pusLen (I/O) | Length of the buffer on input, amount of data stored on output. |

Remarks

AdsGetDateFormat60 returns the current date format for the given connection.

See Also

[AdsGetDateFormat](ace_adsgetdateformat.htm)

[AdsSetDateFormat60](ace_adssetdateformat60.htm)