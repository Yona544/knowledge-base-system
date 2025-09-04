Semaphore Connection File Path




Advantage Database Server 12  

Semaphore Connection File Path

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Semaphore Connection File Path  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Semaphore Connection File Path Advantage Database Server master\_Semaphore\_connection\_file\_path Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Semaphore Connection File Path  Advantage Database Server |  |  |  |  |

Default = Path of first table opened.

Note Semaphore connection files are only used if the configuration parameter Use\_Semaphore\_Files is set to a non-zero value. The default is zero to indicate that semaphore connection files are not used at all. See the configuration option [Use\_Semaphore\_Files](master_use_semaphore_files.htm) for more information.

When an Advantage application calls either an Advantage "connect" API (if available) or opens the first table, it establishes a connection between the application and the Advantage Database Server. During the connect, a semaphore connection file is created by the Advantage Database Server. That file is implicitly opened by the Advantage application using a generic file open call. That is, the file is not opened through the Advantage Database Server. The semaphore connection file is used to aid in determining the connection status between the workstation and the server. The file allows Advantage to properly maintain connections and abort connections if the client connection is inactive. The default directory in which this semaphore connection file is opened is the server directory specified in the "connect" API or where the first table is to be opened. Since the semaphore connection file is actually opened from the workstation and not via the Advantage Database Server, the user must have network READ rights in the directory in which the semaphore connection file exists.

The semaphore connection file is a temporary file and will be named \_T-#####.TMP, where ##### is a five digit number.

A non-default semaphore connection file path is necessary when the first table opened is located in a directory where the user does not have at least network READ privileges. In this case, the semaphore connection file path should be set to a directory where the user does have at least network READ privileges. When using the Advantage "ignore rights" method of security, user access rights are usually revoked from the directory where the data exists and, thus, where the semaphore connection file is created. Therefore, it usually makes sense to configure a specific semaphore connection file directory where no important data exists, but where all users have been given network READ access.

A single semaphore connection file path might also be desirable so that all semaphore connection files for all applications are maintained in a single location.

The network administrator can further take advantage of this semaphore connection file creation to limit which users can connect to the Advantage Database Server and have access to the database. Each user's network rights to the configured semaphore connection file directory will determine if a user can connect to the Advantage Database Server. Those users with network READ rights in the semaphore connection file directory will be able to connect to the Advantage Database Server. Users who do not have network READ rights will not be able to connect to the Advantage Database Server and will not be able to open any data files.

Windows

The Semaphore Connection File Path must be specified as a UNC path. This path may consist of any valid Share on the server.

Example: \\SERVER1\SHARE1\ADSSEM.

Linux

This parameter is only used if 16-bit applications connect to the Advantage Database Server for Linux. The path must be specified in native Linux format. The root directory of the path must be the name of a directory that is shared through Samba, and all directory names included in the path must conform to the DOS 8.3 file format.

Example: /myshare/data/sema4s