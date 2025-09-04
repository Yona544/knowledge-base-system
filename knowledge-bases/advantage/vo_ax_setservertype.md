AX\_SetServerType()




Advantage Database Server 12  

AX\_SetServerType()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetServerType()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_SetServerType() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_setservertype Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetServerType() / Dear Support Staff, |  |
| AX\_SetServerType()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Determines which type of Advantage server the client application can use

Syntax

AX\_SetServerType( lUseRemoteServer, lUseInternetServer, lUseLocalServer )

 

|  |  |
| --- | --- |
| lUseRemoteServer [.T.|.F.] | A logical value that determines if the Advantage Database Server should be used. |
| lUseInternetServer [.T.|.F.] | A logical value that determines if the Internet server should be used. |
| lUseLocalServer [.T.|.F.] | A logical value that determines if the Advantage Local Server should be used. |

Description

AX\_SetServerType determines which types of Advantage servers the client application can use. By default, all three Advantage server types are enabled. The following precedence (by default) is followed when attempting to connect: highest priority is given to the [Advantage Database Server](master_advantage_database_server.htm), second priority to the [Advantage Internet Server](master_advantage_internet_server_overview.htm), and lowest priority to the [Advantage Local Server](master_advantage_local_server.htm). The first parameter enables connections to the Advantage Database Server. The second parameter enables connections to the Advantage Internet Server functionality, and the third parameter enables connections to the Advantage Local Server. If multiple server types are enabled, then the connection type is determined by the precedence mentioned above.

Example

AX\_SetServerType( .T., .T., .T. ) // use all server types

USE test VIA "DBFNTXAX"