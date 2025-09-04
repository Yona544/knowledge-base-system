AdsGetTime




Advantage Database Server 12  

AdsGetTime

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTime  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTime Advantage Client Engine ace\_Adsgettime Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTime  Advantage Client Engine |  |  |  |  |

Retrieves the time value from the given time or timestamp field

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTime (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  UNSIGNED8 \*pucBuf,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| pucBuf (O) | Return field in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetTime returns the time value formatted in 12-hour time with hours, minutes, seconds and an AM/PM indicator as appropriate from either a time field, ModTime field, or the time portion of a timestamp field. If, for example, the time field contains 5415000 milliseconds (since midnight), the string value returned will be "01:30:15 AM". If the exact number of milliseconds is required, use [AdsGetMilliseconds](ace_adsgetmilliseconds.htm).

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_more_examples.htm#adsgettimeexample)

See Also

[AdsSetTime](ace_adssettime.htm)

[AdsGetField](ace_adsgetfield.htm)

[AdsGetMilliseconds](ace_adsgetmilliseconds.htm)