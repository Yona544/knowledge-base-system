AdsLocate




Advantage Database Server 12  

TAdsTable.AdsLocate

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsLocate  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsLocate Advantage TDataSet Descendant ade\_Adslocate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsLocate  Advantage TDataSet Descendant |  |  |  |  |

Performs a sequential search for a record that matches the given expression.

Syntax

function AdsLocate( strExpression : String; bForward : Boolean ) : Boolean;

Parameters

|  |  |
| --- | --- |
| strExpression | Expression that defines desired records. |
| bForward | If True, then search forward. If False, search backward. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Locate. See your Delphi documentation for more information about this native Delphi method.

Description

AdsLocate performs an exhaustive search of the table for records that meet the given expression. The expression given must evaluate to True or False. AdsLocate and AdsContinue do respect any filters set on the table, so for best performance it is best to set a filter before calling this function. If the bForward parameter is True, the search is performed from the top of the table. Subsequent calls to AdsContinue search in the same direction as the AdsLocate call.

If there is an existing index order it is much more efficient to perform an indexed seek using AdsSeek than to perform an AdsLocate. If there is not an existing index order, it would be faster to call AdsSetFilter and use AdsSkip to step through the records because the server would then perform the filtering.

Note Do not confuse an Advantage AdsTable.AdsLocate with a Delphi Locate. A Delphi Locate determines the best possible way to search for a piece of data and performs the search in that manner. An AdsTable.AdsLocate always does a sequential search and is very inefficient and slow. A Delphi Locate is usually very efficient and fast.

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

[AdsContinue](ade_adscontinue.htm)

[AdsSeek](ade_adsseek.htm)

[AdsLookupKey](ade_adslookupkey.htm)