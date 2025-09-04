AdsSkip




Advantage Database Server 12  

TAdsTable.AdsSkip

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSkip  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSkip Advantage TDataSet Descendant ade\_Adsskip Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSkip  Advantage TDataSet Descendant |  |  |  |  |

Skips the given number of records (backwards if lRecs is negative).

Syntax

procedure AdsSkip( lNumRecs : Longint );

Parameter

|  |  |
| --- | --- |
| lNumRecs | Number of records to skip (can be negative). |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Next or Prior. See your Delphi documentation for more information about this native Delphi method.

Description

If the handle is that of a table, then the movement is based on physical record ordering. If it is the handle of an index order, the movement uses that index order. Scopes and filters are respected. A positive number means the skip will occur toward the bottom of the table in natural order if a table handle is passed, and in logical index order if an index order handle is passed. A negative number means the skip will approach the top of the table in logical or natural order. AdsSkip obeys all current filters, and when passing an index handle, top and bottom scopes.

Skipping one record may skip over many physical records because the Advantage server filters records that do not meet current filters conditions.

Skipping forward beyond the last visible record results in the record number being set to the number of records in the table +1, and the EOF flag is set to True. Skipping negative past the first logical record sets BOF to True and sets the current record number to zero.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.Next;

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsGotoBottom](ade_adsgotobottom.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)

[AdsGotoTop](ade_adsgototop.htm)