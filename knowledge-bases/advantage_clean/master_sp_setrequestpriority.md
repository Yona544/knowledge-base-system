---
title: Master Sp Setrequestpriority
slug: master_sp_setrequestpriority
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_setrequestpriority.htm
source: Advantage CHM
tags:
  - master
checksum: 9b6adfd8d6c7942b2f58a7a7d5ebc6f330bc175d
---

# Master Sp Setrequestpriority

sp\_SetRequestPriority

sp\_SetRequestPriority

Advantage SQL Engine

| sp\_SetRequestPriority  Advantage SQL Engine |  |  |  |  |

Set the current connection's request queue priority.

Syntax

sp\_SetRequestPriority( Priority, MEMO )

Parameters

| Priority (I) | The priority to use for this connection. Valid values are 'low', 'normal', 'high', and 'critical'. The default is 'normal'. You should only use critical with extreme caution. |

Output

None

Remarks

The Express Queue is a dynamic queuing mechanism that allows Advantage Database Server to process shorter requests in a more timely fashion, thus allowing applications with short requests to have a better response time. By default, connections with a history of short requests are considered for the express queue. See Express Queue for more information. The procedure sp\_SetRequestPriority allows developers to tune their own applications if necessary. Typically, it should not be necessary to use this procedure.

It is possible to retrieve the current threshold via sp\_mgGetActivityInfo and the current average cost for a user with sp\_mgGetConnectedUsers.

The possible parameter values are:

low  - This specifies that the connection's requests will never be placed in the express queue.

normal - This is the default behavior that allows requests to be placed in the express queue if their average cost is below the threshold.

high - This specifies that the connection's requests always be placed in the express queue regardless of the average cost. This setting can be useful for interactive applications that rarely make costly server requests. Note that if all connected applications use this setting, then the behavior will be the same as if the express queue were not used at all.

critical - This specifies that all of the connection's requests will be placed at the front of the request queue. This setting should be used only with extreme caution. If multiple connections use critical priority, they can easily starve other connections. If any other requests are waiting in the queue to be processed by a worker thread, the critical request will always precede those entries. The other entries will only be processed if no more critical requests arrive while they are in the queue. A possible use of the critical priority setting is in an application that monitors the server and requires a fast response time and will not be making a large number of requests.

See Also

[sp\_mgGetConnectedUsers](master_sp_mggetconnectedusers.md)

[sp\_mgGetActivityInfo](master_sp_mggetactivityinfo.md)

[Express Queue](master_express_queue.md)
