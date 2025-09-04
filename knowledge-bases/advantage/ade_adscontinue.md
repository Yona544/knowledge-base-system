AdsContinue




Advantage Database Server 12  

TAdsTable.AdsContinue

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsContinue  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsContinue Advantage TDataSet Descendant ade\_Adscontinue Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsContinue  Advantage TDataSet Descendant |  |  |  |  |

Continues the locate command based on a previous call to AdsLocate.

Syntax

function AdsContinue : Boolean;

Description

AdsContinue continues searching for records that pass the condition specified in AdsLocate in the direction set by the AdsLocate function. If Result returns False, the table is positioned at EOF or BOF, depending on the direction of the AdsLocate.

AdsContinue performs a skip before evaluating the current record against the condition set in AdsLocate. It is unnecessary to explicitly call AdsSkip between an AdsLocate and an AdsContinue call or between successive AdsContinue calls.

Note Since each record is read from the server for comparison against the filter, it would be faster to use AdsSetFilter because the server would then perform the filtering.

Example

procedure TForm1.LocateRowClick(Sender: TObject);

begin

{ find the first row where LastName equals Smith }

AdsTable1.AdsLocate( 'LastName = "Smith"', TRUE );

end;

 

procedure TForm1.LocateNextRowClick(Sender: TObject);

begin

{ find the next row where LastName equals Smith }

AdsTable1.AdsContinue;

end;

See Also

[AdsLocate](ade_adslocate.htm)