---
title: Vo When To Make Direct Calls To The Advantage Client Engine
slug: vo_when_to_make_direct_calls_to_the_advantage_client_engine
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_when_to_make_direct_calls_to_the_advantage_client_engine.htm
source: Advantage CHM
tags:
  - vo
checksum: 5aa4641057fb652bb410f66cb23112a5c29a879f
---

# Vo When To Make Direct Calls To The Advantage Client Engine

When to Make Direct Calls to the Advantage Client Engine

When to Make Direct Calls to the Advantage Client Engine

Advantage Visual Objects and Vulcan.NET RDD

| When to Make Direct Calls to the Advantage Client Engine  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Most likely you will not need to access the Advantage Client Engine directly. On occasion, however, when developing Advantage-enabled Visual Objects or Vulcan.NET applications, you may find that the functionality provided by the Advantage RDD is not exactly what you need.

It is sometimes easier to call the Advantage Client Engine directly to obtain specific information. For example, the Advantage Client Engine API AdsMgGetUserNames() can report all users that are connected or have a certain file open.

The Advantage RDDs wrap most functionality provided by the Advantage Client Engine. Only in rare circumstances will it be necessary to circumvent the RDD methods and call the engine directly. Because the Advantage Client Engine API is the lowest interface that can be used to access the Advantage functionality, it is more versatile and more complex.

See Also

[How to use the Advantage Client Engine](vo_how_to_use_the_advantage_client_engine.md)
