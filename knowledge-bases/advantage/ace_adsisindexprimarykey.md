AdsIsIndexPrimaryKey




Advantage Database Server 12  

AdsIsIndexPrimaryKey

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexPrimaryKey  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexPrimaryKey Advantage Client Engine ace\_Adsisindexprimarykey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexPrimaryKey  Advantage Client Engine |  |  |  |  |

Determines if the given index order is the primary key.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexPrimaryKey (ADSHANDLE hIndex,  UNSIGNED16 \*pbPrimaryKey); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbPrimaryKey (O) | Returns True if index order is the primary key. |

Remarks

Returns True if the index handle provided is the table's primary key.

See Also

[AdsDDSetTableProperty](ace_adsddsettableproperty.htm)

[AdsDDGetTableProperty](ace_adsddgettableproperty.htm)