AdsGetTableHandle25




Advantage Database Server 12  

AdsGetTableHandle25

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetTableHandle25  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetTableHandle25 Advantage Client Engine ace\_Adsgettablehandle25 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetTableHandle25  Advantage Client Engine |  |  |  |  |

Searches through the list of open tables on the specified connection to find the table with the given filename

Syntax

UNSIGNED32 AdsGetTableHandle25 ( ADSHANDLE hConnect, UNSIGNED8 \*pucName,

ADSHANDLE \*phTable );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection to search for the open table. If this parameter is zero, all connections are searched. |
| pucName (I) | Table name. The given name will be resolved to full path using the same algorithm as [AdsOpenTable](ace_adsopentable.htm). |
| phTable (O) | Handle of the table if found. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_TABLE\_CACHED | This table is marked as closed after a call to [AdsCloseTable](ace_adsclosetable.htm), but the close was cached. |
| AE\_NOT\_FOUND | A handle to the table was not found. |

Remarks

The Advantage Client Engine will attempt to resolve the given name (pucName) to a fully qualified path name and search for a matching filename.

This API is similar to [AdsGetTableHandle](ace_adsgettablehandle.htm) except that a connection handle can be specified to limit the scope of the search. If zero is specified as the connection handle when calling this API, the behavior is identical to AdsGetTableHandle API.

Example

ulRetCode = AdsGetTableHandle25( hConn, "Table1", &hTable );

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsCreateTable](ace_adscreatetable.htm)

[AdsGetTableFilename](ace_adsgettablefilename.htm)

[AdsGetTableAlias](ace_adsgettablealias.htm)

[AdsGetTableHandle](ace_adsgettablehandle.htm)