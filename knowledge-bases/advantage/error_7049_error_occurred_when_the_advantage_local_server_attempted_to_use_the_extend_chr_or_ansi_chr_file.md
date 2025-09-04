7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file




Advantage Database Server 12  

7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file Advantage Error Guide error\_7049\_error\_occurred\_when\_the\_advantage\_local\_server\_attempted\_to\_use\_the\_extend\_chr\_or\_ansi\_chr\_file Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file  Advantage Error Guide |  |  |  |  |

Problem: The Advantage Local Server had a problem when using the EXTEND.CHR or ANSI.CHR file. Either it could not be opened, could not be read from, or did not contain the expected data.

Solution: Verify the OEM\_CHAR\_SET configuration setting in ADSLOCAL.CFG is a valid OEM character set language available in EXTEND.CHR. Also verify the ANSI\_CHAR\_SET configuration setting in ADSLOCAL.CFG is a valid ANSI character set language available in ANSI.CHR. Re-install the EXTEND.CHR or ANSI.CHR from the installation diskette.