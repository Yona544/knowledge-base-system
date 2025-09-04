AdsCloneTable




Advantage Database Server 12  

AdsCloneTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloneTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloneTable Advantage Client Engine ace\_Adsclonetable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloneTable  Advantage Client Engine |  |  |  |  |

Creates a clone of an open table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloneTable (ADSHANDLE hTbl,  ADSHANDLE \*phClone); |

Parameters

|  |  |
| --- | --- |
| hTbl (I) | Original table to be cloned. |
| phClone (O) | Returned handle of the clone table. |

Remarks

AdsCloneTable will produce an identical copy of a table handle. The clone has the following properties identical to the original table handle: it opens the same indexes, it sets the same filter as the original table handle, and it is positioned at the same record number.

AdsCloneTable does NOT replicate properties pertaining to relation information, information stored by an AdsLocate call, or a value stored by calling AdsSetHandleLong.

A clone is only identical to the original table immediately after its creation. Further operations on the original table handle will not be replicated in the cloned handle. After the clone handle is created, it is no different than any other table handle.

Note It is not possible to clone a table that is opened exclusively.