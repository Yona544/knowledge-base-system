AdsGetKeyCount




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsGetKeyCount

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsGetKeyCount  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsGetKeyCount Advantage TDataSet Descendant ade\_Adsgetkeycount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsGetKeyCount  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the number of keys in the active index.

Syntax

function AdsGetKeyCount : Longint;

Description

There may not be the same number of records referenced in an index as in the associated dataset if the index order is a conditional index or a custom index.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is either RESPECT\_SCOPES\_WHEN COUNTING or IGNORE\_SCOPES\_WHEN\_COUNTING, this function should return fairly quickly and provide good performance if the index is not large. If the index is large, this function could take some time to complete because the index keys are literally counted.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING, all records referenced by keys in the index that pass the filter and/or scope/range must be skipped through and counted. Thus, with large indexes where many records pass the filter and/or keys pass the scope/range, this function can be very slow.

Note This function works identically to [AdsGetRecordCount](ade_adsgetrecordcount.htm) when an index is active.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

lKeyCount := AdsTable1.AdsGetKeyCount;

{ lKeyCount equals 950 }

 

AdsTable1.SetRange( ['Adams'], ['Smith'] );

lKeyCount := AdsTable1.AdsGetKeyCount;

{ lKeyCount equals 950 }

AdsTable1.AdsTableOptions.AdsFilterOptions := RESPECT\_WHEN\_COUNTING;

lKeyCount := AdsTable1.AdsGetKeyCount;

{ lKeyCount equals 811 }

AdsTable1.CancelRange;

 

AdsTable1.AdsTableOptions.AdsFilterOptions := RESPECT\_WHEN\_COUNTING;

AdsTable1.Filter := 'LastName = "C\*"';

AdsTable1.Filtered := TRUE;

lKeyCount := AdsTable1.AdsGetKeyCount;

{ lKeyCount equals 72 }

See Also

[AdsGetRecordCount](ade_adsgetrecordcount.htm)