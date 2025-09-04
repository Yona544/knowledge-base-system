---
title: Master Expression Engine Performance
slug: master_expression_engine_performance
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_expression_engine_performance.htm
source: Advantage CHM
tags:
  - master
checksum: 7d06c851adf399732afe3458ef8f47a8c08aa7fb
---

# Master Expression Engine Performance

Expression Engine Performance

Expression Engine Performance

Advantage Concepts

| Expression Engine Performance  Advantage Concepts |  |  |  |  |

When the Advantage server builds an index, the operation is performed using one thread on the server. The thread is not relinquished until index building is complete. If the number of indexes being built at any one time is equal to the number of threads configured with the Advantage server, other Advantage users' operations will be held off until an index creation completes. A thread is then released and other operations may be executed. If operations are being held off, increase the thread count. See the Advantage Database Server guide for information about how to change the Advantage server thread count parameter.
