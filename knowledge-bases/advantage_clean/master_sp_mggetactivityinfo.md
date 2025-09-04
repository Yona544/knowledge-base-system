---
title: Master Sp Mggetactivityinfo
slug: master_sp_mggetactivityinfo
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetactivityinfo.htm
source: Advantage CHM
tags:
  - master
checksum: 7927db0e42b2bf4702e787116ababe6db84421ba
---

# Master Sp Mggetactivityinfo

sp\_mgGetActivityInfo

sp\_mgGetActivityInfo

Advantage SQL Engine

| sp\_mgGetActivityInfo  Advantage SQL Engine |  |  |  |  |

This procedure returns information about the current activity on the Advantage Database Server.

Syntax

EXECUTE PROCEDURE sp\_mgGetActivityInfo()

Parameters

| Operations (O) | Total number of operations performed since the server started. |
| LoggedErrors (O) | Number of errors logged since server started. |
| UpTime (O) | Total time the Advantage Database Server has been in operation in Days, Hours, Minutes and Seconds. |
| EQThreshold (O) | The current Express Queue threshold used for determining if a request will be placed in the express queue. Note that the server only updates the threshold value if the number of  connections exceeds the number of worker threads. If the number of connections is less than the worker thread count, the threshold value is neither used or updated. |
| EQActiveThreads (O) | The current number of worker threads operating on Express Queue requests. |
| EQOperations (O) | The total number of requests that have been processed as Express Queue requests. |

Remarks

sp\_mgGetActivityInfo returns three parameters of the ADS\_MGMT\_ACTIVITY\_INFO structure returned by AdsMgGetActivityInfo. The additional items not returned from the ADS\_MGMT\_ACTIVITY\_INFO can be retrieved using sp\_mgGetUsageInfo.

For additional context with regard to the EQ\* output parameters, see the [Express Queue](master_express_queue.md) documentation.

Note With the Advantage Local Server, sp\_mgMgGetActivityInfo will only return information for the instance of Advantage Local Server currently loaded into memory.

Example

EXECUTE PROCEDURE sp\_mgGetActivityInfo();

See Also

[sp\_mgGetUsageInfo](master_sp_mggetusageinfo.md)
