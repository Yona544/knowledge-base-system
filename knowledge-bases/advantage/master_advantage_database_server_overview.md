Advantage Database Server Overview




Advantage Database Server 12  

Advantage Database Server Overview

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Database Server Overview  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Advantage Database Server Overview Advantage Database Server master\_Advantage\_database\_server\_overview Advantage Database Server > Introduction > Advantage Database Server Overview / Dear Support Staff, |  |
| Advantage Database Server Overview  Advantage Database Server |  |  |  |  |

Advantage Database Server is a high performance client/server RDBMS for stand-alone, networked, Internet, and mobile database applications. Advantage Database Server allows developers the flexibility to combine powerful SQL statements and relational data access methods with the performance and control of navigational commands. Advantage has native development interfaces designed to leverage existing knowledge of popular development tools. With optimized data access methodology for easily delivering unparalleled performance, Advantage provides security, stability, and data integrity while being completely maintenance-free.

The Advantage Database Server is the key to improved database performance in network environments. The server can be visualized as an intelligent controller that reduces competition for resources and off-loads much of the work normally performed by each client workstation. It is responsible for all database access, including all reading and writing of data, and lock management. Working with the network operating system, the Advantage Database Server processes data requests and returns the information to the network clients.

Support for Windows and Linux Operating Systems

The Advantage Database Server supports the Windows and Linux operating systems. The Advantage Database Server for Windows operates as a Windows Service.

Note The Advantage Database Server for Windows is a Service. It cannot be run as a standard Windows application. See [Installing and Starting the Advantage Database Server for Windows](master_installing_and_starting_the_advantage_database_server_for_windows_nt_2000_2003.htm) , for more information on Windows Services and how to start them.

The Advantage Database Server retrieves requests for database operations to be performed on behalf of the clients. The Advantage Database Server locates tables on the server and processes the database operations. The result of the operation is then returned to the client across the network, eliminating the need to send the database to the client for processing. This provides far better concurrency control and system integrity than is otherwise available.

Traditional non-client/server applications send raw data from the server across the network to be processed on the workstation. With the Advantage Database Server, much of the data is processed by the Advantage Database Server on the file server. By decreasing network traffic, you increase performance.

The Advantage Database Server integrity system ensures that database updates either run to completion or do not begin. The Advantage Database Server will not execute partial commands. This means that the integrity of your database no longer depends on the stability of the workstations on the network. Because the Advantage Database Server is responsible for all database access (on behalf of the clients), it can do a far better job of concurrency control than traditional systems, where concurrency must be synchronized between remote workstations. Better concurrency control means better multi-user performance.