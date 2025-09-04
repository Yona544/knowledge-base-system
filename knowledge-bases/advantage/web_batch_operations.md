Advantage Web Platform Batch Operations




Advantage Database Server 12  

Batch Operations

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Batch Operations  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Batch Operations Advantage Web Platform web\_batch\_operations Advantage Web Development > Advantage Web Platform > Batch Operations / Dear Support Staff, |  |
| Batch Operations  Advantage Web Platform |  |  |  |  |

It should be noted that the BATCH documentation below details the nuts and bolts of a batch request. OData clients typically implement this functionality for you and provide easy-to-use abstractions.

The BATCH operation is defined to allow a single request to define multiple update operations. With the Advantage Web Platform, the operations define in a single change set within a batch operation will be performed within a transaction if Advantage Database Server is being used as the back end.

A BATCH operation is, basically, a mechanism that allows a request to package up multiple POST, PUT/MERGE, and DELETE operations into a single atomic request. A BATCH request is sent as a POST operation and the body of the request contains one or more change sets.

See the following sub-topics for details:

[Example Batch Request](web_batch_request_example.htm)

[Example Batch Response](web_batch_response_example.htm)

[References in Batch Requests](web_batch_references.htm)

[Example Batch Request using JSON](web_batch_response_json.htm)

[Example Batch Response using JSON](web_batch_response_json.htm)