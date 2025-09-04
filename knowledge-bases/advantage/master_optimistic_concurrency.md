Optimistic Concurrency Control




Advantage Database Server 12  

Optimistic Concurrency Control

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Optimistic Concurrency Control  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Optimistic Concurrency Control Advantage Web Platform master\_Optimistic\_Concurrency Advantage Web Development > Advantage Web Platform > Optimistic Concurrency Control / Dear Support Staff, |  |
| Optimistic Concurrency Control  Advantage Web Platform |  |  |  |  |

To help with caching issues when using OData, it is possible to enable optimistic concurrency control on individual tables. To enable this option on a table, the table must have a ROWVERSION field. To enable the option with Advantage Data Architect, go to the Table Properties in the table designer (e.g., right click on a table in the connection repository). Choose "Yes" for the Web Service Concurrency Enabled option. To enable the option programmatically, you can use a system procedure:

EXECUTE PROCEDURE [sp\_ModifyTableProperty](master_sp_modifytableproperty.htm)( 'tablename', 'TABLE\_CONCURRENCY\_ENABLED', 'TRUE', null, null );

For tables with this concurrency mode enabled, the OData server will:

|  |  |
| --- | --- |
| · | Return ConcurrencyMode="Fixed" attribute in the Property Name tag for the ROWVERSION field of the table in the top level $metadata document. |

|  |  |
| --- | --- |
| · | Return ETag header values in responses (e.g., singleton GET requests, POST, PUT, and MERGE responses). |

|  |  |
| --- | --- |
| · | Return an etag value/pair in the \_\_metadata for JSON responses. |

|  |  |
| --- | --- |
| · | Return m:etag value/pair in the entry tag for ATOM/XML responses (e.g., <entry m:etag="12345">). |

|  |  |
| --- | --- |
| · | Recognize If-Match and If-None-Match headers on GET, PUT, MERGE, and DELETE requests. Note that for PUT, MERGE, and DELETE requests on concurrency-enabled tables, an If-Match or If-None-Match header is required otherwise a 412 (Precondition Failed) response will be returned. If the ETag value is not known and the update/delete is required and ETag value of '\*' (an asterisk) can be specified. |

The use of ETags is a standard feature, so if you are using an existing OData client such as the Advantage OData client for Delphi, then it should not be necessary to do anything other than enable the concurrency option on the table. Once enabled, the client and server will handle the requests and responses appropriately.

When the concurrency option is enabled, and update request (PUT, MERGE, or DELETE) from the client will send the last known ETag value for the record with an If-Match header. If the ETag value does not match that of the current record state, a 412 (Precondition Failed) error will be returned and the record will not be updated.  In addition, a client may take advantage of ETag values for client-side caching. A GET request with an If-None-Match header will only retrieve the record contents if it has been modified since the given ETag.

Examples

For a table that has the concurrency option enabled, the Property Name tag in the $metadata response:

<Property Name="rowversion" Type="Edm.Decimal" Nullable="false" Scale="0" Precision="21" ConcurrencyMode="Fixed"/>

In a GET, PUT, MERGE, or POST response, an ETag header value will be returned:

HTTP/1.1 200 OK

Date: Fri, 03 Jan 2014 20:48:44 GMT

Server: Apache/2.2.22 (Win32)

DataServiceVersion: 2.0

ETag: "23424993"

...

The corresponding JSON response might look like this:

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "http://.../tasks(1)",

         "key\_fields": "id",

         "etag": "23424993"

       },

       "id": 123,

       "rowversion": 23424993,

       "name": "Connection and Statement Pooling",

       "started": "2010-11-05T00:00:00",

       "finished": null

     }

   ]

 }

}

A PUT request to update a concurrency-enabled table must include the ETag in an If-Match header:

MERGE http://...table('id1') HTTP/1.1

User-Agent: Microsoft ADO.NET Data Services

DataServiceVersion: 1.0;NetFx

MaxDataServiceVersion: 2.0;NetFx

If-Match: "23424993"