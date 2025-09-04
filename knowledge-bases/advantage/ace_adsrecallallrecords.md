AdsRecallAllRecords




Advantage Database Server 12  

AdsRecallAllRecords

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRecallAllRecords  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRecallAllRecords Advantage Client Engine ace\_Adsrecallallrecords Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRecallAllRecords  Advantage Client Engine |  |  |  |  |

Recalls all deleted records in a table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRecallAllRecords (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |

Remarks

AdsRecallAllRecords loops through each record in the given table and recalls all deleted records. This API uses slightly lower level functions and thus can recall more records (for ADTs) than [AdsRecallRecord](ace_adsrecallrecord.htm). This operation requires exclusive access to the table, specified during the open. To ensure the integrity of the table header and all associated indexes, AdsRecallAllRecords performs a pack of the table after recalling all deleted records. For this reason, all associated indexes of this table must be opened to remain logically correct. See [AdsPackTable](ace_adspacktable.htm) for more information.

Note AdsRecallAllRecords can only recall records still in the re-use list (for ADTs). Once a record buffer is re-used, it can never be recalled.

See Also

[AdsRecall Record](ace_adsrecallrecord.htm)

[AdsDeleteRecord](ace_adsdeleterecord.htm)