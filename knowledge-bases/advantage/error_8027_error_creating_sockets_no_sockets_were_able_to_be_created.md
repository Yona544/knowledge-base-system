8027 Error creating sockets. No sockets were able to be created




Advantage Database Server 12  

8027 Error creating sockets. No sockets were able to be created

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 8027 Error creating sockets. No sockets were able to be created  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 8027 Error creating sockets. No sockets were able to be created Advantage Error Guide error\_8027\_error\_creating\_sockets\_no\_sockets\_were\_able\_to\_be\_created Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 8027 Error creating sockets. No sockets were able to be created  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to create any sockets for communications. Advantage Database Server on Windows or Linux will continue to run and allow direct inter-process communications with clients running on the same physical machine as the server. It will not be able to accept connections from clients running on remote machines.

Solution: Verify that a networking protocol (TCP/IP or IPX) is installed and enabled on the server. If a LAN\_IP\_ADDRESS or INTERNET\_IP\_ADDRESS is specified in the Advantage Database Server configuration, verify that it is correct.