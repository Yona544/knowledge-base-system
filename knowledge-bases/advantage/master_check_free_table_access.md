Check\_Free\_Table\_Access




Advantage Database Server 12  

Check\_Free\_Table\_Access

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Check\_Free\_Table\_Access  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Check\_Free\_Table\_Access Advantage Database Server master\_check\_free\_table\_access Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Check\_Free\_Table\_Access  Advantage Database Server |  |  |  |  |

Default = 0 (False)

By default, free tables (those not associated with a dictionary) can be accessed through data dictionary connections. With ADT tables, this is not necessarily a problem or security because when ADT tables are added to a data dictionary, then they can no longer be accessed as free tables and, thus, can only be accessed through the data dictionary in which they exist. DBF tables, though, cannot be directly associated with a data dictionary because that would render them incompatible with other non-Advantage applications.

To prevent applications from accessing free tables through dictionary connections on a server-wide basis, you can set this configuration value to 1. This is similar to the CheckFreeTableAccess [connection string option](ace_adsconnect101.htm), however that setting is for a per connection basis and still allows free table access by dictionary administrators and by stored procedures and views. In contrast, if this server configuration setting is enabled, then no free tables can be accessed even under those administrative conditions.

Note that for this setting to be effective from a security standpoint, it would also be necessary to disable all free connections via the [Disable\_Free\_Connections](master_disable_free_connections.htm) configuration setting. Otherwise, someone could bypass the Check\_Free\_Table\_Access restriction simply by making a free connection to the server and accessing free tables through that connection.

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\Check\_Free\_Table\_Access=1

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf):

Check\_Free\_Table\_Access=1

See Also

[Disable\_Free\_Connections](master_disable_free_connections.htm)