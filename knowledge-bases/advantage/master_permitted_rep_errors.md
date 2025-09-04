Permitted\_Rep\_Errors




Advantage Database Server 12  

Permitted\_Rep\_Errors

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Permitted\_Rep\_Errors  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Permitted\_Rep\_Errors Advantage Database Server master\_Permitted\_rep\_errors Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Permitted\_Rep\_Errors  Advantage Database Server |  |  |  |  |

Default = 7137

Keyword = PERMITTED\_REP\_ERRORS

This configuration parameter can be used to specify which errors are "allowed" during replication updates. This is a server-wide setting that affects subscriptions that have the Ignore Replication Failures option enabled (see [Replication Options](master_replication_options.htm)). By default, only 7137 errors are permitted and any other errors that occur will cause replication to the target to be blocked until the replication update succeeds or is manually removed from the replication queue.

If there are other errors that you want the server to allow during replication to a target, you can specify them with this configuration setting. Note, that by customizing the list, it will no longer ignore error 7137 by default. Therefore, if new error codes are added, you must include 7137 in the list if you still want to allow that error. The configuration setting is a string that contains a list of the permitted errors delimited by spaces, commas, or semicolons. For example:

PERMITTED\_REP\_ERRORS=7137,7057

For Windows:

Add or modify the following string value using the Registry Editor (REGEDIT.EXE):

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\PERMITTED\_REP\_ERRORS=x

For Linux:

Add or modify the following line in the Advantage Database Server configuration file (adsd.conf):

PERMITTED\_REP\_ERRORS=x