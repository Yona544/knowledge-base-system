Replication\_Library




Advantage Database Server 12  

Replication\_Library

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication\_Library  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Replication\_Library Advantage Database Server Master\_replication\_library Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Replication\_Library  Advantage Database Server |  |  |  |  |

Default = none

The replication engine (beginning with v11 of Advantage) has the ability to load a specific version of the Advantage Client Engine library. This provides the capability to replicate to an older version of Advantage Database Server (e.g., replicate from v11.0 to v10.1). Specify the path and file name of the desired client library.  See [Replicating to Older Servers](master_replicating_to_older_servers.htm) for more details.

For Windows:

Add the following string value using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\REPLICATION\_LIBRARY=c:\pathtolibrary\ace64.dll

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf):

REPLICATION\_LIBRARY=/usr/lib/libace.so.10