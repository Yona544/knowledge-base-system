7181 Maximum Number of Connected (Stateful) Users Exceeded




Advantage Database Server 12  

7181 Maximum Number of Connected (Stateful) Users Exceeded

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7181 Maximum Number of Connected (Stateful) Users Exceeded  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7181 Maximum Number of Connected (Stateful) Users Exceeded Advantage Error Guide Error\_7181\_stateful\_connection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7181 Maximum Number of Connected (Stateful) Users Exceeded  Advantage Error Guide |  |  |  |  |

Problem: The maximum configured number of connected (stateful) users has been exceeded.

Solution: The Advantage user count can be allocated between stateful connections (e.g., those consumed by a Delphi application) and stateless connections (e.g., those used by the Advantage Web Platform) . The [WEB\_PLATFORM\_USERS](master_web_platform_users_para.htm) configuration parameter can be used to specify the [maximum number of web platform users](master_web_platform_users.htm). Reducing that value will allow for more concurrent stateful connections.