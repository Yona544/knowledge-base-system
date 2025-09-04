MAX\_CACHE\_MEMORY




Advantage Database Server 12  

MAX\_CACHE\_MEMORY

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MAX\_CACHE\_MEMORY  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - MAX\_CACHE\_MEMORY Advantage Database Server master\_Max\_cache\_memory Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MAX\_CACHE\_MEMORY  Advantage Database Server |  |  |  |  |

Default = Half of the available system memory (RAM) at startup

This configuration entry specifies the maximum amount of memory (RAM) in megabytes (MB) the Advantage Database Server will use to cache index files, table headers, memo headers, and temporary files. If this setting is not found, the Advantage Database Server will determine an appropriate maximum value by dividing the currently available amount of free memory by two. In 32-bit operating systems, Advantage will use no more than 256MB for cache unless the MAX\_CACHE\_MEMORY specifies a higher value. The amount of free memory is polled once per minute, and if the Advantage Database Server is using more than half of 80% of free memory, it will release enough memory so there will be at least 100MB memory available in the system.

If the configured amount is zero, the Advantage Database Server will not cache any file data.

To set a specific amount of memory for the Advantage Database Server to use for caching, perform one of the following where "x" is replaced by the actual integer memory amount in megabytes (MB). To disable the cache system, specify a value of zero.

For Windows:

Add or modify the following DWORD value using the Registry Editor (REGEDIT.EXE):

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\MAX\_CACHE\_MEMORY=x

For Linux:

Add or modify the following line in the Advantage Database Server configuration file (adsd.conf):

MAX\_CACHE\_MEMORY=x

For Local Server:

Add or modify the following line in the Advantage Local Server configuration file (adlocal.cfg):

MAX\_CACHE\_MEMORY=x