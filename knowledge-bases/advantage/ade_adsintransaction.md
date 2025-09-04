AdsInTransaction




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsInTransaction

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsInTransaction  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsInTransaction Advantage TDataSet Descendant ade\_Adsintransaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsInTransaction  Advantage TDataSet Descendant |  |  |  |  |

Tests if the dataset is within a transaction.

Syntax

function AdsInTransaction: boolean;

Description

AdsInTransaction will return True if this dataset is currently within a transaction and False otherwise.

Example

{ start a transaction for all records associated with AdsConnection1 }

AdsConnection1.BeginTransaction;

 

{ is this table in a transaction, It should be if it is associated to AdsConnection1 }

bInTransaction := AdsTable1.AdsInTransaction;

See Also

None.