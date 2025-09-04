---
title: Master Express Queue
slug: master_express_queue
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_express_queue.htm
source: Advantage CHM
tags:
  - master
checksum: 07474a5515a9d89ee25fc145913417c56dc9941d
---

# Master Express Queue

Express Queue

Express Queue

Advantage Concepts

| Express Queue  Advantage Concepts |  |  |  |  |

When a client request such as an SQL command arrives at the server and there is at least one unused worker thread available, that thread will immediately start processing the request. If all worker threads are busy with other operations, the new request is placed in the request queue to be processed by the next available worker thread. Typically, these requests are processed in order of arrival. Beginning with Advantage v10, Express Queue functionality changes this behavior slightly. Requests are still placed in the queue in the order received. However, requests from connections that have a history of short operations are also placed in the express queue.

A limited number of worker threads are allowed to take items from the express queue but only when the remaining number of available worker threads drops below that limit. This can allow short operations to be processed in a more timely fashion and not have to wait behind connections that have a history of running long (costly) operations.

The type of situation that is helped by the express queue is when there is a mix of application types running against the server. If, for example, the number of applications making costly server requests exceeds the number of configured worker threads, they could, in previous versions of Advantage, limit the number of requests made by other applications. Requests from applications making short requests would be intermingled with the long requests and, effectively, run at the same rate as the more costly requests. With the express queue, a number of worker threads are allowed to process the shorter requests ahead of the longer requests. This can make time-critical applications that have short requests such as interactive user applications operate in a more responsive fashion.

The cost prediction for each connection is based on an estimated sliding average of the previous requests. The threshold for being placed on the express queue is recomputed regularly by the server so that it is always based on the current set of connections. Therefore, Advantage automatically adjusts the express queue behavior to conform to the current workload. It is possible to retrieve the current threshold by calling the system procedure sp\_mgGetActivityInfo, and individual connections estimated costs can be retrieved with sp\_mgGetConnectedUsers. However, it is important to note that the server only updates the threshold value if the number of connections exceeds the number of worker threads. If the number of connections is less than the worker thread count, there is no need to give express queue priority to any requests since there would always be an available worker thread to process each request. In that situation, therefore, the server does not maintain the threshold value.

It is possible to tune specific connections to always be included or excluded from the express queue. The system procedure sp\_SetRequestPriority controls this. Typically, though, it should not be necessary to use sp\_SetRequestPriority. Thus, it is unlikely that any changes need to be made to applications in order to benefit from this new functionality.
