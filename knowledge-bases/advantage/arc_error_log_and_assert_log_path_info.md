Error Log and Assert Log Path Info




Advantage Database Server 12  

Error Log and Assert Log Path Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Error Log and Assert Log Path Info |  |  | Feedback on: Advantage Database Server 12 - Error Log and Assert Log Path Info arc\_Error\_log\_and\_assert\_log\_path\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Error Log and Assert Log Path Info |  |  |  |  |

The error log is either ads\_err.dbf (a DBF table) or ads\_err.adt (an ADT table) to which any application or data error or warning is recorded. The default is to use ads\_err.adt and can be controlled via the ERROR\_LOG\_TYPE configuration parameter. Errors and warnings written to this error log file are not necessarily critical errors but are key to tracing potential problems in the system or client applications. This error log may be configured to a maximum file size to prevent excessive disk space usage.

Advantage Database Server for Windows

Default = Root of the drive where Advantage Database Server service is installed.

The Advantage error log, ADS\_ERR.ADT or ADS\_ERR.DBF, and assert log, ASSERT.LOG, files may be stored in any directory on the server. The default path is the root of the drive where the Advantage Database Server is installed.

Example: C:\ADSERROR

Advantage Database Server for Linux

Default = /var/log/advantage.

The Advantage Database Server error log, ADS\_ERR.ADT or ADS\_ERR.DBF, and assert log, ASSERT.LOG, files may be stored in any directory on the file server. The default path is /var/log/advantage.

Example: ERROR\_ASSERT\_LOGS = /usr/local/advantage