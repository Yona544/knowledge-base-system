AdsIsIndexUnique




Advantage Database Server 12  

AdsIsIndexUnique

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexUnique  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexUnique Advantage Client Engine ace\_Adsisindexunique Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexUnique  Advantage Client Engine |  |  |  |  |

Determines if the given index order is unique.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexUnique (ADSHANDLE hIndex,  UNSIGNED16 \*pbUnique); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbUnique (O) | Return True if index order was built with the ADS\_UNIQUE option. |

Remarks

A unique index will have no repeated key values.

Example

[Click Here](ace_examples.htm#adsisindexuniqueexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsIsIndexCandidate](ace_adsisindexcandidate.htm)