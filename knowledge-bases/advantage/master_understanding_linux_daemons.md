Understanding Linux Daemons




Advantage Database Server 12  

Understanding Linux Daemons

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Understanding Linux Daemons  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Understanding Linux Daemons Advantage Database Server master\_Understanding\_linux\_daemons Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Understanding Linux Daemons  Advantage Database Server |  |  |  |  |

In Linux, many server-side programs act as a daemon. Unlike regular applications, daemons run in the background providing application support and have no user interface of their own. Because the Advantage daemon does not have a user interface, all errors are logged in the ads\_err.adt or ads\_err.dbf file, and server messages are logged in the ads\_log.txt file. Both of these files can be found (if any errors have occurred) in the advantage error log directory (default is /var/log/advantage).

Advantage Database Server Daemon

The Advantage Database Server was designed as a daemon to provide the most robust and safest database management possible. As a daemon, Advantage has better control over how and when the program is started and shut down. For example, if the daemon is started from an init.d script (see [Example init.d Script](master_example_init_d_script.htm)), the Advantage Database Server daemon will automatically start when the server comes up again after being shut down. This provides a benefit over regular applications because it does not require a user to log in to get the Advantage Database Server service up and running again after a power failure or other unexpected shut down.

Starting and Stopping the Advantage Database Server Daemon

The Advantage Database Server daemon must be started before applications can run using the Advantage Database Server. Superuser privileges are required to start and stop the Advantage daemon.

Note An alternative to the steps described below is to use an init.d script. See [Example init.d Script](master_example_init_d_script.htm) for more details.

To start the Advantage Database Server Daemon:

|  |  |
| --- | --- |
| 1. | Go to the directory where the adsd file resides. |

|  |  |
| --- | --- |
| 2. | As superuser, type the command "./adsd" |

|  |  |
| --- | --- |
| 3. | If the Advantage Database Server daemon fails to run, check the ads\_log.txt log for details. |

To stop the Advantage Database Server Daemon:

|  |  |
| --- | --- |
| 1. | As superuser, type the command "ps A | more", to get a list of all running processes. |

|  |  |
| --- | --- |
| 2. | Note the pid of the first adsd process in the list. |

|  |  |
| --- | --- |
| 3. | Type the command "kill X", where X is the pid of the first adsd process reported by the ps command. |

The "advantage" user and group

The Advantage Database Server for Linux installation will create a new user and group. When the Advantage Database Server daemon is started, it will begin running as this new user. All files it creates will be owned by the new "advantage" user.

MOST IMPORTANTLY: The "advantage" user must have privileges to (or own) the tables you wish to open using the Advantage Database Server. If you copy a database to your Linux server be sure to change the owner to "advantage". A command similar to:

chown advantage <file-list>

followed by:

chgrp advantage <file-list>

will configure the correct permissions, allowing Advantage to open your tables.