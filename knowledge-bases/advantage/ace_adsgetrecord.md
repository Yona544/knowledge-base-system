AdsGetRecord




Advantage Database Server 12  

AdsGetRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetRecord Advantage Client Engine ace\_Adsgetrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetRecord  Advantage Client Engine |  |  |  |  |

Returns the current record as a single raw data buffer.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetRecord (ADSHANDLE hTable,  UNSIGNED8 \*pucRec,  UNSIGNED32 \*pulLen); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucRec (O) | Return record contents in this buffer. |
| pulLen (I/O) | Length of given buffer on input, length of returned data on output. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_CURRENT\_RECORD | Data cannot be retrieved from EOF or BOF |

Remarks

Use of AdsGetRecord is strongly discouraged, especially if there are memo fields or extended data types present in the table. It is much safer to use [AdsGetField](ace_adsgetfield.htm) and related functions to read information from a record.

Example

[Click Here](ace_examples.htm#adsgetrecordexample)

See Also

[AdsSetRecord](ace_adssetrecord.htm)

[AdsGetField](ace_adsgetfield.htm)