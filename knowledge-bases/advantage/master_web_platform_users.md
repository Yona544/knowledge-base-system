Web Platform Users




Advantage Database Server 12  

Web Platform Users

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Web Platform Users  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Web Platform Users Advantage Database Server master\_Web\_Platform\_Users Advantage Concepts > Advantage Functionality > Web Platform Users / Dear Support Staff, |  |
| Web Platform Users  Advantage Database Server |  |  |  |  |

The Advantage Web Platform introduced to the Advantage product line in version 11 resulted in a new type of user connection to Advantage. Prior to this release, all connections to Advantage were considered "stateful". Typically, an application would make an explicit connection (e.g., through an API such as AdsConnect) and then eventually close the connection. Requests made through the Advantage Web Platform are considered stateless. Each individual request is effectively independent from previous (and future) requests. A client using the web platform does not make an explicit connection to Advantage Database Server. The web platform acquires a database connection on behalf of the request and makes the necessary calls to Advantage Database Server.

If the web platform were to make a brand new database connection for every individual request, it would result in poor performance. Therefore, these stateless connections are pooled for reuse between requests to greatly reduce the cost of each request. In order to maximize the underlying caching in Advantage Database Server, the web platform makes an attempt to reuse the same database connection for successive requests from a given client. This is not guaranteed but, typically, the same existing database connection will be used for the same client within a given time period. A connection will remain in the pool for approximately 15 minutes. If it goes unused longer than that, it will be released and the next request by that user will likely result in the web platform acquiring a new database connection.

Users connecting to Advantage through the Advantage Web Platform are counted as separate users. To prevent the possibility of all Advantage user connections being taken up by traditional fully connected (stateful) applications and leaving none available for web applications, Advantage now allows the total user count to be partitioned into two categories. The user count can be divided between users for traditional connected applications and Advantage Web Platform applications.

Advantage Database Server supports the configuration parameter [WEB\_PLATFORM\_USERS](master_web_platform_users_para.htm) for specifying the number of users to allocate for use by the Advantage Web Platform. For example, with a 20 user version of Advantage, you could set the configuration value to 5 to allow five concurrently active web platform users at a time and leave the remaining 15 users available for fully connected stateful applications (e.g., a Delphi application). With Advantage Database Server for Windows, you can adjust the configuration value through the [Advantage Configuration Utility](master_advantage_configuration_utility_for_windows_nt_2000_2003.htm) under the Database Settings tab.