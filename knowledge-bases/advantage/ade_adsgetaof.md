AdsGetAOF




Advantage Database Server 12  

TAdsTable.AdsGetAOF

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetAOF  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetAOF Advantage TDataSet Descendant ade\_Adsgetaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetAOF  Advantage TDataSet Descendant |  |  |  |  |

Retrieve the AOF expression that was used in the call to AdsSetAOF.

Syntax

function AdsGetAOF : String

Description

AdsGetAOF returns the AOF expression string that was used in the call to AdsSetAOF

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

 

eLevel := AdsTable1.AdsEvalAOF( 'LastName = "S" .AND. EMPID > 50' );

{ eLevel equals olPart because EMPID is not indexed }

 

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

strAOF := AdsTable1.AdsGetAOF;

eLevel := AdsTable1.AdsGetAOFOptLevel( strNonOptimizied );

{ eLevel equals olPart because EMPID is not indexed }

{ strNonOptimized equals EMPID>50 }

 

{. . . your code here . . .}

 

AdsTable1.AdsRefreshAOF;

 

See Also

[AdsSetAOF](ade_adssetaof.htm)

[AdsRefreshAOF](ade_adsrefreshaof.htm)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.htm)