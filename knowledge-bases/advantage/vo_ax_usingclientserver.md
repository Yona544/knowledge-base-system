AX\_UsingClientServer()




Advantage Database Server 12  

AX\_UsingClientServer()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_UsingClientServer()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_UsingClientServer() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_usingclientserver Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_UsingClientServer() / Dear Support Staff, |  |
| AX\_UsingClientServer()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Indicates whether the current work area is using the Advantage Database Server

Syntax

AX\_UsingClientServer() -> logical

Returns

AX\_UsingClientServer returns a .T. if the current Advantage work area is accessing the Advantage Database Server. Returns .F. if the current Advantage work area has opened the database file using the local RDD.

Description

AX\_UsingClientServer indicates whether the current Advantage work area is accessing the Advantage Database Server in "client/server" mode.

Example

oDB1 := AxDBServer{ "TEST1", .F., .F., "AXDBFNTX" }

if AX\_UsingClientServer()

? "File open in Client/Server mode."

else

? "Warning: File opened in Local mode."

endif