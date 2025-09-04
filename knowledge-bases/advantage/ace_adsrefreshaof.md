AdsRefreshAOF




Advantage Database Server 12  

AdsRefreshAOF

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRefreshAOF  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRefreshAOF Advantage Client Engine ace\_Adsrefreshaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRefreshAOF  Advantage Client Engine |  |  |  |  |

Updates the filter

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRefreshAOF ( ADSHANDLE hTable ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor that has an AOF to be refreshed. |

Remarks

AdsRefreshAOF rebuilds the filter using the original values passed to [AdsSetAOF](ace_adssetaof.htm). The [Advantage Database Server](master_advantage_database_server.htm) maintains the accuracy of all AOFs associated with a given table when updates are performed. With [Advantage Local Server](master_advantage_local_server.htm), however, it is possible for another client to make updates to the table. In that case, it might be useful to call AdsRefreshAOF to force the filter to be rebuilt. It may also make sense to call this function if an index that could affect the optimization level of the AOF has been opened or created since the original AOF was created.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsrefreshaof_example)

See Also

[AdsSetAOF](ace_adssetaof.htm)

[AdsClearAOF](ace_adsclearaof.htm)

[AdsGetAOF](ace_adsgetaof.htm)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.htm)

[AdsEvalAOF](ace_adsevalaof.htm)