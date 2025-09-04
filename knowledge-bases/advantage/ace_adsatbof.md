AdsAtBOF




Advantage Database Server 12  

AdsAtBOF

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsAtBOF  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsAtBOF Advantage Client Engine ace\_Adsatbof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsAtBOF  Advantage Client Engine |  |  |  |  |

Determines if the current position is at the beginning of the table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsAtBOF (ADSHANDLE hTable,  UNSIGNED16 \*pbBOF); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pbBof (O) | Set to True if at BOF. |

Remarks

The BOF flag (Beginning Of File) indicates that the table is positioned at the top of the table on a virtual record. When BOF is True, the record number is zero (0). Data values cannot be retrieved because there is no physical record. The BOF flag is set after an [AdsSkip](ace_adsskip.htm) call with a negative number that skips back past the first record in the table, or if there are no records currently visible. When located at BOF and there are no visible records, skipping forward 1 (one) will position at the first logical record in the table, or another movement function can be used to position.

Example

[Click Here](ace_examples.htm#adsatbofexample)

See Also

[AdsAtEOF](ace_adsateof.htm)

[AdsSkip](ace_adsskip.htm)