Setting Up Your Clients Using ADS.INI




Advantage Database Server 12  

Setting Up Your Clients Using ADS.INI

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Setting Up Your Clients Using ADS.INI  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Setting Up Your Clients Using ADS.INI Advantage Database Server master\_Setting\_up\_your\_clients\_using\_ads\_ini Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Setting Up Your Clients Using ADS.INI  Advantage Database Server |  |  |  |  |

The Advantage Internet Server configuration can be specified in the ADS.INI file by adding a couple of sections.

The [Drives] section lists the complete UNC path to which a drive letter is mapped. If your client application uses drive letters, you will need to define the drive letter mappings.

Example:

[ Drives ]

R:=\\SERVER1\SHARE

For each Advantage Database Server you want to connect to, you will need to have a separate server-name entry.

Example:

[ <server name> ]

INTERNET\_PORT=<the Internet port for the server>

INTERNET\_IP=<the IP address for the Advantage Database Server>

Example:

[Drives]

Q:=\\serverA\testsys\

r:=\\serverB\data\

[serverA]

INTERNET\_PORT=2001

INTERNET\_IP=198.169.1.69

[serverB]

INTERNET\_PORT=2002

INTERNET\_IP=198.70.169.72