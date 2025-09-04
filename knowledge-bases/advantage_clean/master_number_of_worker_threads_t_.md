---
title: Master Number Of Worker Threads T
slug: master_number_of_worker_threads_t_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_number_of_worker_threads_t_.htm
source: Advantage CHM
tags:
  - master
checksum: d20aa3317ce0283dcb4ce7904d9b88aa32d7aff7
---

# Master Number Of Worker Threads T

Number of Worker Threads (-T)

Number of Worker Threads (-T)

Advantage Database Server

| Number of Worker Threads (-T)  Advantage Database Server |  |  |  |  |

Range = 0 - 1024.

If the value is not specified or is zero (0), Advantage Database Server will compute the number of threads based on the number of CPUs on Linux and Windows servers. The default number will be the number of CPUs multiplied by 8.

While individual circumstances and client application development style may call for a different value, a general rule is to set the configuration value from 8 to 16 worker threads per CPU Core. For example, on a server with 4 CPU Cores, configuring Advantage Database Server to use between 32 and 64 worker threads may produce the best performance for typical usage patterns. Specifying larger numbers of worker threads can often be counterproductive because the OS will have to spend more time managing the threads (e.g., performing context switches), and there may be higher contention for shared resources.

This configuration parameter specifies the number of Advantage Database Server worker threads used to service client database requests. If the number of requests exceeds the number of threads, the requests are queued until a worker thread completes its current request. Increasing this parameter may improve the responsiveness of individual client applications, but it may also reduce the performance of other concurrent server functions.

The Advantage Database Server uses multiple worker threads to execute multiple requests concurrently. If the worker thread count is set to 1, the Advantage Database Server acts as a single-tasking system, processing each database request sequentially in the order it is received.

The result of increasing the number of worker threads is environment dependent. The system administrator may want to experiment with the number of worker threads in an attempt to balance system throughput versus individual application performance.

When the Advantage Database Server performs a time consuming operation such as processing a long SQL query or building an index, the operation is performed using one worker thread and the worker thread is not relinquished until the operation is complete. If all worker threads are being used in this manner, other requests are held off until a thread completes the operation. In this type of situation, it may be desirable to have additional worker threads available to respond to other requests. However, the total system throughput will decrease in most cases as the number of worker threads increases. [Express Queue](master_express_queue.md) functionality can help with balancing the processing of short server requests.
