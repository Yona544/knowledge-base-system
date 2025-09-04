AdsExtendedReader.RecallAllRecords




Advantage Database Server 12  

AdsExtendedReader.RecallAllRecords

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.RecallAllRecords  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.RecallAllRecords Advantage .NET Data Provider dotnet\_Adsextendedreader\_recallallrecords Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.RecallAllRecords / Dear Support Staff, |  |
| AdsExtendedReader.RecallAllRecords  Advantage .NET Data Provider |  |  |  |  |

Recalls all deleted records in a table.

public void RecallAllRecords();

Remarks

RecallAllRecords loops through each record in the given table and recalls all deleted records. RecallAllRecords uses slightly lower level functions and thus can recall more records (for ADTs) than RecallRecord. This operation requires exclusive access to the table, specified in the ConnectionString (Shared=FALSE). To ensure the integrity of the table header and all associated indexes, RecallAllRecords performs a pack of the table after recalling all deleted records. For this reason, all associated indexes of this table must be opened to remain logically correct. See PackTable for more information.

Note RecallAllRecords can only recall records still in the re-use list (for ADTs). Once a record buffer is re-used, it can never be recalled.

See Also

[RecallRecord](dotnet_adsextendedreader_recallrecord.htm)

[DeleteRecord](dotnet_adsextendedreader_deleterecord.htm)

[PackTable](dotnet_adsextendedreader_packtable.htm)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)