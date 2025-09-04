AdsAtEOF




Advantage Database Server 12  

AdsAtEOF

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsAtEOF  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsAtEOF Advantage Client Engine ace\_Adsateof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsAtEOF  Advantage Client Engine |  |  |  |  |

Determines if the current position is at the end of the table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsAtEOF (ADSHANDLE hTable,  UNSIGNED16 \*pbEof); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pbEof (O) | Set to True if at EOF. |

Remarks

The EOF flag (End Of File) indicates that the table is positioned at the bottom of the table on a virtual record. When EOF is set to True, the current record number is the number of records in the table plus 1 (one). Data cannot be retrieved because the table is not positioned on a physical record.

The EOF flag is set after skipping forward past the last record in the table, after failed seeks, and when there are no visible records in the table. If positioned at EOF, skipping back 1 (one) will position at the last record in the table or index order, or other movement functions can be used.

Example

[Click Here](ace_examples.htm#adsateofexample)

See Also

[AdsAtBOF](ace_adsatbof.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSkip](ace_adsskip.htm)