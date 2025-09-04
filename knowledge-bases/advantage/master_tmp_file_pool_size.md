TMP\_FILE\_POOL\_SIZE




Advantage Database Server 12  

TMP\_FILE\_POOL\_SIZE

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TMP\_FILE\_POOL\_SIZE  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - TMP\_FILE\_POOL\_SIZE Advantage Database Server master\_TMP\_FILE\_POOL\_SIZE Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TMP\_FILE\_POOL\_SIZE  Advantage Database Server |  |  |  |  |

Default = 200

This configuration entry specifies the size of the [temporary file pool](master_temporary_file_pooling.htm).  If this value is set to 0, the temporary file pool will not be used.  The lifetime of temporary files that are in the pool is typically only a few seconds.  Their primary purpose is to enhance performance of a very busy system.

To specify the size of the temporary file pool, perform one of the following where "x" is replaced by the actual integer size of the pool. To disable the temporary file pool, specify a value of zero.

 

For Windows NT/2000/2003:

Add or modify the following DWORD value using the Registry Editor (REGEDIT.EXE):

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\TMP\_FILE\_POOL\_SIZE=x

 

For Linux:

Add or modify the following line in the Advantage Database Server configuration file (adsd.conf):

TMP\_FILE\_POOL\_SIZE=x

 

For Local Server:

Add or modify the following line in the Advantage Local Server configuration file (adlocal.cfg):

TMP\_FILE\_POOL\_SIZE=x

 

See Also

[Temporary File Pooling](master_temporary_file_pooling.htm)