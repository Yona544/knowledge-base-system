Viewing Configuration Parameters Not Affecting Memory




Advantage Database Server 12  

Viewing Configuration Parameters Not Affecting Memory

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Viewing Configuration Parameters Not Affecting Memory  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Viewing Configuration Parameters Not Affecting Memory Advantage Data Architect arc\_Viewing\_configuration\_parameters\_not\_affecting\_memory Advantage Data Architect > Advantage Utilities > Advantage Management Utility > Viewing Configuration Parameters Not Affecting Memory / Dear Support Staff, |  |
| Viewing Configuration Parameters Not Affecting Memory  Advantage Data Architect |  |  |  |  |

Many Advantage Database Server configuration parameters affect CPU and memory usage, and altering the default settings may affect memory requirements on your server.

The Configuration Parameters Not Affecting Memory screen displays the current parameters, such as error and assert log paths, that are defined at load time but have no direct affect on file server memory usage.

Field Descriptions

Maximum Size of Error Log (KBytes)

Default = 1000 Kbytes. Range = 1 - no upper limit.

The error log file size is the maximum file size the error log file (ADS\_ERR.DBF or ADS\_ERR.ADT), can reach. Once the maximum file size is attained, the first one-third of the records in the error log table are marked for deletion and packed automatically. With ADS\_ERR.DBF, new entries are appended to the end of the file. With ADS\_ERR.ADT, record recycling is used, so the new entries may not be at the physical end of the table. Viewing ADS\_ERR.ADT in ERROR\_NUMBER index order will ensure that the errors are displayed in the order they are logged.

The error log is a table used to record any errors encountered by the Advantage Database Server during execution of client applications. The ADS\_ERR.DBF error log file may be viewed using any standard DBF utility. ADS\_ERR.ADT is an Advantage proprietary format table and can be viewed with Advantage Data Architect.

Error Log and Assert Log Path

The error log is either ads\_err.dbf (a DBF table) or ads\_err.adt (an ADT table), used to record any errors encountered by the Advantage Database Server during execution of client applications.

Advantage Database Server for Windows

Default = Root of the drive where the Advantage Database Server service is installed.

The Advantage error log, ADS\_ERR.ADT or ADS\_ERR.DBF, and assert log, ASSERT.LOG, files may be stored in any directory on the server. The default path is the root of the drive where the Advantage Database Server is installed.

Example: C:\ADSERROR

Advantage Database Server for Linux

Default = /var/log/advantage.

The Advantage Database Server error log, ADS\_ERR.ADT or ADS\_ERR.DBF, and assert log, ASSERT.LOG, files may be stored in any directory on the file server. The default path is /var/log/advantage.

Example: ERROR\_ASSERT\_LOGS = /usr/local/advantage

Semaphore Connection File Path

When an Advantage application connects to the Advantage Database Server, it establishes a connection between the workstation and the Advantage Database Server. A semaphore connection file is opened to aid in determining the connection status between the workstation and the Advantage Database Server service. The default directory in which this semaphore connection file is opened is the server directory where the first database file is to be opened.

Note Semaphore connection files are only used if the configuration parameter Use\_Semaphore\_Files is set to a non-zero value. The default is zero to indicate that semaphore connection files are not used at all. See the configuration option [Use\_Semaphore\_Files](master_use_semaphore_files.htm) for more information.

Transaction Log File Path

Transaction log files are created by the Advantage Transaction Processing System to aid in recording all commands and functions executed within a transaction.

IP Port

By default, the Advantage Database Server will secure the next IP port available at startup time for use later to receive data via the IP protocol from Advantage clients. If you desire the Advantage Database Server to use a specific IP port, rather than the next available, then edit this setting. The NETSTAT utility with the option "-a" (i.e., "netstate -a") can be used to find out what IP ports are currently in use.

Internet Port

The Advantage Database Server must be setup to communicate with the clients through an IP address and port combination for Internet access. On a computer with only one IP address, Advantage Database Server automatically uses that IP address. To disable Internet access to the Advantage Database Server set the Internet Port value to zero.

See Also

[Viewing Configuration Parameters Affecting Memory](arc_viewing_configuration_parameters_affecting_memory.htm)