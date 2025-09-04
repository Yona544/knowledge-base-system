---
title: Web Batch Operations
slug: web_batch_operations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_batch_operations.htm
source: Advantage CHM
tags:
  - web
checksum: 6f58166bbb1e98acb1ecb9742b86806a006e4ee9
---

# Web Batch Operations

Advantage Web Platform Batch Operations

Batch Operations

Advantage Web Platform

| Batch Operations  Advantage Web Platform |  |  |  |  |

It should be noted that the BATCH documentation below details the nuts and bolts of a batch request. OData clients typically implement this functionality for you and provide easy-to-use abstractions.

The BATCH operation is defined to allow a single request to define multiple update operations. With the Advantage Web Platform, the operations define in a single change set within a batch operation will be performed within a transaction if Advantage Database Server is being used as the back end.

A BATCH operation is, basically, a mechanism that allows a request to package up multiple POST, PUT/MERGE, and DELETE operations into a single atomic request. A BATCH request is sent as a POST operation and the body of the request contains one or more change sets.

See the following sub-topics for details:

[Example Batch Request](web_batch_request_example.md)

[Example Batch Response](web_batch_response_example.md)

[References in Batch Requests](web_batch_references.md)

[Example Batch Request using JSON](web_batch_response_json.md)

[Example Batch Response using JSON](web_batch_response_json.md)
