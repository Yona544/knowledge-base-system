Use Dynamic Cursors




Advantage Database Server 12  

Use Dynamic Cursors

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Use Dynamic Cursors  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Use Dynamic Cursors Advantage Database Server master\_Use\_dynamic\_cursors Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Use Dynamic Cursors  Advantage Database Server |  |  |  |  |

Default is to use dynamic cursors.

A dynamic cursor is one that is updated to reflect changes to the underlying table. When dynamic cursors are turned on, changes made by any user to the underlying table are reflected in all Advantage Optimized Filters (AOFs) set on that table by other users. If dynamic cursors are turned off, the only changes made to an Advantage Optimized Filter are changes that are made to the table by the owner of the Advantage Optimized Filter. Because many optimizations by the SQL engine are performed through Advantage Optimized Filters, this setting can affect SQL statements as well. Turning dynamic cursors off may increase performance when AOFs are set on the table in which records are being modified. See [Differences Between AOFs and Traditional Record Filters](master_differences_between_aofs_and_traditional_record_filters.htm).

To turn off dynamic cursors, perform one of the following.

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf).

USE\_DYNAMIC\_CURSORS=0

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry.

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\USE\_DYNAMIC\_CURSORS=0

Note If setting filters manually (not using SQL) this behavior does not need to be modified at the server level (globally). Multiple filter types exist, which can modify the filter behavior at the work area level. See the Delphi TAdsDataSet.Filter documentation or the ACE AdsSetAOF documentation for details.