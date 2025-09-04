Log Files




Advantage Database Server 12  

Linux Log Files

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Linux Log Files  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Linux Log Files Advantage Concepts master\_Log\_files Advantage Concepts > Advantage Linux Development Notes > Log Files / Dear Support Staff, |  |
| Linux Log Files  Advantage Concepts |  |  |  |  |

The Advantage Database Server for Linux uses the same general error log as all other Advantage servers (ads\_err.dbf and ads\_err.adt), but also includes a new text log (ads\_log.txt) used for reporting fatal errors. If the Advantage Database Server daemon stops responding, verify the process is still running and then check the ads\_log.txt file for error information.

The default location for both log files is in the /var/log/advantage directory. This location is configurable through the ERROR\_ASSERT\_LOGS parameter in the ads.conf file.

IMPORTANT NOTE: The "advantage" user must have write privileges to the error log directory, or it will not be able to create or write to the log files.