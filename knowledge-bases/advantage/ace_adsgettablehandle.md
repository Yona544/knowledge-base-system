AdsGetTableHandle




Advantage Database Server 12  

AdsGetTableHandle

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableHandle  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableHandle Advantage Client Engine ace\_Adsgettablehandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableHandle  Advantage Client Engine |  |  |  |  |

Searches through the list of open tables to find the table with the given filename

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetTableHandle (UNSIGNED8 \*pucName,  ADSHANDLE \*phTable); |

Parameters

|  |  |
| --- | --- |
| pucName (I) | Table name. The given name will be resolved to full path using the same algorithm as [AdsOpenTable](ace_adsopentable.htm). |
| phTable (O) | Handle of the table if found. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_TABLE\_CACHED | This table is marked as closed after a call to [AdsCloseTable](ace_adsclosetable.htm), but the close was cached. |
| AE\_NOT\_FOUND | A handle to the table was not found. |

Remarks

The Advantage Client Engine will attempt to resolve the given name (pucName) to a fully qualified path name and search for a matching filename.

To find open table on a specific connection, use [AdsGetTableHandle25](ace_adsgettablehandle25.htm).

Example

[Click Here](ace_examples.htm#adsgettablehandleexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableFilename](ace_adsgettablefilename.htm)

[AdsGetTableAlias](ace_adsgettablealias.htm)

[AdsGetTableHandle25](ace_adsgettablehandle25.htm)