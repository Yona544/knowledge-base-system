adsdump Files




Advantage Database Server 12  

adsdump Files

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| adsdump Files  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - adsdump Files Troubleshooting master\_Adsdump\_files Troubleshooting and Technical Support > Troubleshooting > adsdump Files / Dear Support Staff, |  |
| adsdump Files  Troubleshooting |  |  |  |  |

Note The following documentation is specific to the Advantage Database Server for Windows.

Overview

If the Advantage Database Server detects an internal error or an exception, it will create a dump file in the Advantage error log directory (the default directory is c:\). The dump file name will be in the following format:

adsdump-CCYYMMDD-HHMMSS.dmp.gz

where CCYYMMDD represents the date the error occurred, and HHMMSS represents the time of the error.

A Windows event log entry will be made providing notification of the dump file creation. If your server generates a dump file, please forward the dump file, all ads\_err.\* files, and the ADS\_SNAP.LOG file (if it exists) to your Advantage support provider.

Configuration Options

Dump files are generally created if the server encounters an exception, or logs a 9000 class error. If for any reason you do not want the server to create these files, or if you want the server to stop creating these files while the Advantage support team is working on your current issue, you can disable the dump file functionality by adding the following DWORD registry entry and setting its value to zero:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\MINIDUMPINTERVAL

This registry entry can also be used to specify an interval between file dumps, in cases where the default value (24 hours) is either not sufficient, or is too long. The interval value should be specified in seconds. For example, the default of 24 hours would be specified using a value of 86,400 seconds (24 hours).

It is also possible to disable the compression of the dump files. The compression step can take a significant amount of time for very large files. To disable it, add the following DWORD registry entry and set its value to zero (0). The default value if it does not exist is 1. Note that if the dump file compression is disabled, the name of the file will not include the ".gz" extension.

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\[COMPRESS\_DUMP\_FILES](master_compress_dump_files.htm)