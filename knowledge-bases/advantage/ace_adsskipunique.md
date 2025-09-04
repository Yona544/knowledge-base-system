AdsSkipUnique




Advantage Database Server 12  

AdsSkipUnique

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSkipUnique  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSkipUnique Advantage Client Engine ace\_Adsskipunique Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSkipUnique  Advantage Client Engine |  |  |  |  |

Skips through an index only stopping on unique keys.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSKipUnique ( ADSHANDLE hIndex,                 SIGNED32 lRecs ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| lRecs (I) | Number of records to skip (can be negative). |

Remarks

Skips the given number of records (backward if lRecs is negative) only stopping on unqiue keys in the index. Scopes and filters are respected. A positive number means the skip will occur in logical index order to next unique key value. A negative number means the skip will approach the top of the table in logical order. AdsSkipUnique obeys all current filters and top and bottom scopes are observed.

Skipping one record may skip over many physical records because the Advantage server will filter records that do not meet current filter conditions.

Skipping forward beyond the last visible record results in the record number being set to the number of records in the table +1, and the EOF flag is set to True. Skipping negative past the first logical record sets BOF to True and sets the current record number to zero.

Skipping zero records will flush pending changes to disk but will not move in the index.

Example

ulRetCode = AdsSkipUnique( hIndex2, 1 );

See Also

[AdsSkip](ace_adsskip.htm)

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsAtBOF](ace_adsatbof.htm)

[AdsAtEOF](ace_adsateof.htm)