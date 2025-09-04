Avoiding ANSI Collation Mismatch Errors




Advantage Database Server 12  

Avoiding ANSI Collation Mismatch Errors

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Avoiding ANSI Collation Mismatch Errors  Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Avoiding ANSI Collation Mismatch Errors Troubleshooting master\_Avoiding\_ansi\_collation\_mismatch\_errors Troubleshooting and Technical Support > Troubleshooting > Avoiding ANSI Collation Mismatch Errors / Dear Support Staff, |  |
| Avoiding ANSI Collation Mismatch Errors  Troubleshooting |  |  |  |  |

A single Advantage application can connect to multiple Advantage Database Servers, or one or more Advantage Database Servers and the Advantage Local Server. If such an application is using ANSI or OEM collation with non-USA collation sets, care must be taken to avoid a 5092 Collation Mismatch error. To avoid such an error, make sure the same ANSI collation language is being used with all connections. To ensure the ANSI collation languages are the same, verify one of the following is true:

|  |  |
| --- | --- |
| 1. | This first option is strongly recommended and is the easier method to make sure the ANSI collation languages are the same for all connections. Specifically select an ANSI collation language when installing the Advantage Database Server and Advantage clients. Make sure to specify the same ANSI language for all installs. The ANSI collation language selected during an Advantage client install will be placed in the Advantage Local Server configuration file, ADSLOCAL.CFG. |

|  |  |
| --- | --- |
| 2. | If you do not wish to use option 1 above, select <CURRENT SYSTEM LANGUAGE> for the ANSI collation language when installing the Advantage Database Server and the Advantage clients. Only select <CURRENT SYSTEM LANGUAGE> if all of the following are True. All computers used for installation of the Advantage Database Server should be running the same Windows operating system. The computer running an application that connects to the Advantage Local Server should also be running this same OS. In addition to the operating systems being the same, all computers should be using the same ANSI collation language (which is specified via the Regional Settings icon). |

Note If your application is connecting to a single Advantage Database Server, just the Advantage Local Server, or English ANSI collation language is always being used, no Collation Mismatch errors will occur.

 

Note If you change your ANSI collation language from one language to another, you need to rebuild all of your index files.