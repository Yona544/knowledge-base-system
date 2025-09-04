---
title: Error 8040 Error Creating Shared Memory Object
slug: error_8040_error_creating_shared_memory_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8040_error_creating_shared_memory_object.htm
source: Advantage CHM
tags:
  - error
checksum: 330c5ee7ff70b3a2da244ec10d4ea8594a93b7e0
---

# Error 8040 Error Creating Shared Memory Object

8040 Error creating shared memory object

8040 Error creating shared memory object

Advantage Error Guide

| 8040 Error creating shared memory object  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server failed to create a shared memory object to use for inter-process communications (IPC) with clients running on the same physical workstation. This error is logged for informational purposes and is not returned to the client. The entry preceding this error in the error log will show the specific system error code.

Solution: This error can occur if a client application has stopped responding and has been disconnected by Advantage Database Server. The client application will hold the IPC objects for a specific connection entry and prevent future use of them. Close the unresponsive client application to free up the IPC objects.
