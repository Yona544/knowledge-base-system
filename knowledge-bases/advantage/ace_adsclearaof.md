AdsClearAOF




Advantage Database Server 12  

AdsClearAOF

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearAOF  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearAOF Advantage Client Engine ace\_Adsclearaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearAOF  Advantage Client Engine |  |  |  |  |

Deactivates the AOF and releases all resources associated with it

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearAOF ( ADSHANDLE hTable ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor with an AOF to clear. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

The AdsClearAOF function deactivates the AOF and releases all resources associated with it on both the client and the server. Also note that when a table is closed, any AOF associated with it is automatically cleared as well.

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsclearaof_example)

See Also

[AdsSetAOF](ace_adssetaof.htm)