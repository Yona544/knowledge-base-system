AdsEvalAOF




Advantage Database Server 12  

TAdsTable.AdsEvalAOF

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsEvalAOF  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsEvalAOF Advantage TDataSet Descendant ade\_Adsevalaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsEvalAOF  Advantage TDataSet Descendant |  |  |  |  |

Evaluate a filter expression to determine its optimization level.

Syntax

type TAdsAOFOptimizeLevel = ( olFULL, olPART, olNONE );

 

function AdsEvalAOF ( strFilter : String ): TAdsEvalAOF;

Parameter

|  |  |
| --- | --- |
| strFilter | Filter expression to evaluate to determine optimization level. |

Description

AdsEvalAOF can be used to determine the optimization level of a potential filter expression. It performs the same parsing as [AdsSetAOF](ade_adssetaof.htm) but does not actually build the filter.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

 

eLevel := AdsTable1.AdsEvalAOF( 'LastName = "S" .AND. EMPID > 50' );

{ eLevel equals olPart because EMPID is not indexed }

 

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

eLevel := AdsTable1.AdsGetAOFOptLevel( strNonOptimizied );

{ eLevel equals olPart because EMPID is not indexed }

{ strNonOptimized equals EMPID>50 }

See Also

[AdsSetAOF](ade_adssetaof.htm)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.htm)