AdsGetRecordLength




Advantage Database Server 12  

TAdsTable.AdsGetRecordLength

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetRecordLength  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetRecordLength Advantage TDataSet Descendant ade\_Adsgetrecordlength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetRecordLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the record size for the given table.

Syntax

function AdsGetRecordLength : Longint;

Description

The record size returned includes space for the deleted byte for DBF table records. For ADT records, this record size will include 5 extra bytes used internally by Advantage. This length may not reflect the actual amount of data accessible for this record if the table includes variable-length fields.

Example

AdsTable1.Active := TRUE;

lRecordCount := AdsTable1.AdsGetRecordLength;

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)