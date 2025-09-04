Using Full Text Search with Versions of Advantage Prior to 7.0




Advantage Database Server 12  

Using Full Text Search with Versions of Advantage Prior to 7.0

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Full Text Search with Versions of Advantage Prior to 7.0  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Using Full Text Search with Versions of Advantage Prior to 7.0 Advantage Concepts master\_Using\_full\_text\_search\_with\_versions\_of\_advantage\_prior\_to\_7\_0 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Using Full Text Search with Versions of Advantage Prior to 7.0  Advantage Concepts |  |  |  |  |

Versions of Advantage prior to 7.0 do not recognize full text search indexes. If you are using Advantage Database Server 7.0 or greater and attempt to open a full text search index with an older client, Advantage will return error code 7105 to the client and not allow the client to open the index.

If you attempt to open an ADI (Advantage proprietary) index file containing an FTS index with a version of Advantage Database Server prior to 7.0, it will not recognize the new index version and will return a 7058 error. It is not possible to open an ADI index file that has FTS indexes in it with a version of Advantage prior to 7.0.

If you open a CDX (FoxPro-compatible) index file containing an FTS index with a version of Advantage Database Server prior to 7.0, Advantage will not generate any errors initially. This can lead to unpredictable behavior. If the FTS index is built on a memo or BLOB field, the Advantage client will generate a 3005 error. If the index is built on a character or raw field, however, the client and server will determine that the index is valid and will attempt to use it. If, for example, the SQL engine uses it, it may cause queries to return empty result sets or produce 7017 errors. If a client uses it for ordering result sets, records may appear in unpredictable order and may also result in 7017 errors.