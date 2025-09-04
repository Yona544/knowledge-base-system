Error and Diagnostic Logs




Advantage Database Server 12  

Error and Diagnostic Logs

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Error and Diagnostic Logs  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Error and Diagnostic Logs Troubleshooting master\_Error\_and\_diagnostic\_logs Troubleshooting and Technical Support > Troubleshooting > Error and Diagnostic Logs / Dear Support Staff, |  |
| Error and Diagnostic Logs  Troubleshooting |  |  |  |  |

ADS\_ERR.DBF and ADS\_ERR.ADT

For troubleshooting purposes, the Advantage Database Server and the Advantage Local Server maintain an error log. This log file is only created when an error occurs while executing an operation in the Advantage server code. Many times, a client workstation may encounter errors that the server is not notified of; therefore, nothing is logged in the server's error log file. The size of the file can be limited and its location can be set via Advantage configuration parameters. The most important fields are, Date and Time, Error Code, and Filename. Other useful information, such as the connect name, Advantage version, and OS type and version, can be found in the error log file.

Advantage will use either ADS\_ERR.DBF or ADS\_ERR.ADT as the log file. The default behavior beginning with v8.0 is to use ADS\_ERR.ADT, which is the Advantage proprietary table (ADT) format. If Advantage cannot write to ADS\_ERR.ADT, it will revert to ADS\_ERR.DBF. In addition, the configuration parameter ERROR\_LOG\_TYPE=1 can be specified to force Advantage to use ADS\_ERR.DBF. The default setting of ERROR\_LOG\_TYPE=2 specifies that Advantage should use ADS\_ERR.ADT. The ADS\_ERR.ADT error log format provides some additional flexibility in logging of errors. For example, error log includes a memo field named More\_Info that may contain descriptive text for some errors. When viewing ADS\_ERR.ADT, you should sort it by the ERROR\_NUMBER index to view the errors in the order in which they were logged. Advantage Data Architect will, by default, select this index when ADS\_ERR.ADT is opened.

Another benefit to using the ADS\_ERR.ADT error log is that Advantage can write to the error log while it is open with Advantage Data Architect. If you have ADS\_ERR.DBF open with any other application, Advantage will not be able to write to the error log.

If Advantage encounters any internal (9000 class) errors, it will still log them to ADS\_ERR.DBF regardless of the ERROR\_LOG\_TYPE configuration parameter. Also, it is important to note that Advantage Local Server and Advantage Database Server cannot share the ADS\_ERR.ADT log file. If the table is open, for example, by Advantage Local Server, then Advantage Database Server will not be able to open and write to it.

To force Advantage to use the ads\_err.dbf log file, add the configuration parameter entry as follows:

For Advantage Database Server for Windows, add the parameter to the registry. Add a dword value of 1 with the name ERROR\_LOG\_TYPE.

The registry branch for Windows is:

HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration

WARNING Use the Registry Editor incorrectly can cause serious problems that may require you to reinstall the Windows operating system. If you are not familiar with the registry editor, allow an administrator to make the change for you. iAnywhere cannot guarantee that problems resulting from the incorrect use of the Registry Editor can be solved.

For Advantage Database Server for Linux and Advantage Local Server, add the following entry to the configuration file (ads.conf or adslocal.cfg respectively).

ERROR\_LOG\_TYPE=1

Environment Check Log File

The environment check utilities are probably the most popular Advantage network troubleshooting tools. Perhaps the most valuable information is the output of a log file containing all of the pertinent network information for a client workstation.