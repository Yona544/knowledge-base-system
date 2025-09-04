AdsGetMilliseconds




Advantage Database Server 12  

AdsGetMilliseconds

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetMilliseconds  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetMilliseconds Advantage Client Engine ace\_Adsgetmilliseconds Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetMilliseconds  Advantage Client Engine |  |  |  |  |

Retrieves the time value from the given time or timestamp field as the number of milliseconds since midnight

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetMilliseconds (ADSHANDLE hTable,  UNSIGNED8 \*pucFldName,  SIGNED32 \*plTime); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFldName (I) | Name of field to retrieve. |
| plTime (O) | Return the value. |

Remarks

AdsGetMilliseconds returns the number of milliseconds since midnight that is stored in a time field, ModTime field, or in the time portion of a timestamp field.

The pucFldName parameter can be passed as the field name itself or as the one-based integer field position. To pass an integer field position for the pucFldName parameter, use the ADSFIELD macro that is defined in ACE.H. For example, to specify the first field in the table, pass ADSFIELD(1) for the pucFldName parameter; to specify the second field in the table, pass ADSFIELD(2) for the pucFldName parameter; etc.

Example

[Click Here](ace_more_examples.htm#adsgetmillisecondsexample)

See Also

[AdsGetField](ace_adsgetfield.htm)

[AdsGetTime](ace_adsgettime.htm)

[AdsSetMilliseconds](ace_adssetmilliseconds.htm)