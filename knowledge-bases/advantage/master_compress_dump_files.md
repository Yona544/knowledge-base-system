Compress\_Dump\_Files




Advantage Database Server 12  

Compress\_Dump\_Files

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Compress\_Dump\_Files  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Compress\_Dump\_Files Advantage Database Server Master\_Compress\_Dump\_Files Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Compress\_Dump\_Files  Advantage Database Server |  |  |  |  |

Default = 1 (compress dump files)

When Advantage creates a [dump file](master_adsdump_files.htm), the default behavior is to compress the dump file after it is created. While this typically reduces the file size significantly, it can take a relatively long time to complete the compression. To disable the compression step, add the following configuration parameter and set the value to zero (0).

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\Compress\_Dump\_Files=0