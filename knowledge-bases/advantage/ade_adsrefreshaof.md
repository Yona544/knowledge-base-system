AdsRefreshAOF




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsRefreshAOF

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsRefreshAOF  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsRefreshAOF Advantage TDataSet Descendant ade\_Adsrefreshaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsRefreshAOF  Advantage TDataSet Descendant |  |  |  |  |

Rebuilds the filter.

Syntax

procedure AdsRefreshAOF;

Description

AdsRefreshAOF rebuilds the filter using the original values passed to [AdsSetAOF](ade_adssetaof.htm). The [Advantage Database Server](master_advantage_database_server.htm) maintains the accuracy of all AOFs associated with a given table when updates are performed. With [Advantage Local Server](master_advantage_local_server.htm), however, it is possible for another client to make updates to the table. In that case, it might be useful to call AdsRefreshAOF to force the filter to be rebuilt. It may also make sense to call this function if an index that could affect the optimization level of the AOF has been opened or created since the original AOF was created.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsSetAOF( 'LastName = "S" .AND. EMPID > 50' );

 

{. . .your code here. . .}

 

AdsTable1.AdsRefreshAOF;

 

See Also

[AdsSetAOF](ade_adssetaof.htm)

[AdsClearAOF](ade_adsclearaof.htm)

[AdsGetAOF](ade_adsgetaof.htm)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.htm)

[AdsEvalAOF](ade_adsevalaof.htm)