AdsSkip




Advantage Database Server 12  

AdsSkip

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSkip  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSkip Advantage Client Engine ace\_Adsskip Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSkip  Advantage Client Engine |  |  |  |  |

Skips the given number of records

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSkip (ADSHANDLE hObj, SIGNED32 lRecs); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table, cursor, or index order. |
| lRecs (I) | Number of records to skip (can be negative). |

Remarks

Skips the given number of records (backward if lRecs is negative). If the handle is that of a table or cursor, then the movement is based on physical record ordering. If it is the handle of an index order, the movement uses that index order. Scopes and filters are respected. A positive number means the skip will occur toward the bottom of the table in natural order if a table or cursor handle is passed, and in logical index order if an index order handle is passed. A negative number means the skip will approach the top of the table in logical or natural order. AdsSkip obeys all current filters. When passing an index handle, top and bottom scopes are observed.

Skipping one record may skip over many physical records because the Advantage server will filter records that do not meet current filter conditions.

Skipping forward beyond the last visible record results in the record number being set to the number of records in the table +1, and the EOF flag is set to True. Skipping negative past the first logical record sets BOF to True and sets the current record number to zero.

Skipping zero records will flush pending changes to disk but will not move in the table or index.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adsskipexample)

See Also

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsAtBOF](ace_adsatbof.htm)

[AdsAtEOF](ace_adsateof.htm)