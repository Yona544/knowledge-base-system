---
title: Error 5092 Ae Collation Sequence Mismatch
slug: error_5092_ae_collation_sequence_mismatch
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5092_ae_collation_sequence_mismatch.htm
source: Advantage CHM
tags:
  - error
checksum: f648d157fee111504833967717437422a6fa627f
---

# Error 5092 Ae Collation Sequence Mismatch

5092 AE\_COLLATION\_SEQUENCE\_MISMATCH

5092 AE\_COLLATION\_SEQUENCE\_MISMATCH

Advantage Error Guide

| 5092 AE\_COLLATION\_SEQUENCE\_MISMATCH  Advantage Error Guide |  |  |  |  |

Different OEM or ANSI collation languages were being used by different connections to the Advantage Database Server and/or Advantage Local Server.

Avoiding OEM Collation Mismatch Errors

A single Advantage application can connect to multiple Advantage Database Servers, or one or more Advantage Database Servers and the Advantage Local Server. If such an application is using ANSI or OEM collation with non-USA collation sets, care must be taken to avoid a 5092 Collation Mismatch error. To avoid such an error, make sure the same OEM collation language is selected when installing the Advantage Database Server and the Advantage clients. The OEM collation language selected during an Advantage client install will be placed in the Advantage Local Server configuration file, ADSLOCAL.CFG. Note that when installing the U.S. version of the Advantage Database Server, USA is the only OEM collation language available, so there is no ability to select a different OEM collation language.

Note If one of the following conditions is present, no Collation Mismatch errors will occur:

- Your application is connecting to a single Advantage Database Server

- Your application is connecting to just the Advantage Local Server

- USA OEM collation language is always being used.

 

Note If you change your OEM collation language from one language to another, you need to rebuild all of your index files.

Avoiding ANSI Collation Mismatch Errors

A single Advantage application can connect to multiple Advantage Database Servers, or one or more Advantage Database Servers and the Advantage Local Server. If such an application is using ANSI or OEM collation with non-USA collation sets, care must be taken to avoid a 5092 Collation Mismatch error. To avoid such an error, make sure the same ANSI collation language is being used with all connections. To ensure the ANSI collation languages are the same, verify one of the following is true:

1) This first option is strongly recommended and is the simpler method to make sure the ANSI collation languages are the same for all connections. Specifically select an ANSI collation language when installing the Advantage Database Server and Advantage clients. Be sure to specify the same ANSI language for all installs. The ANSI collation language selected during an Advantage client install will be placed in the Advantage Local Server configuration file, ADSLOCAL.CFG. If the ANSI language you desire is not shown in the list, the ANSICHR.EXE utility can be used to add an ANSI language to the file containing the available ANSI languages.

2) If you do not wish to use option 1 above, select <CURRENT SYSTEM LANGUAGE> for the ANSI collation language when installing the Advantage Database Server and the Advantage clients. Only select <CURRENT SYSTEM LANGUAGE> if all of the following are True. All computers used for installation of the Advantage Database Server should be running the same Windows operating system. The computer running an application that connects to the Advantage Local Server should also be running this same OS. In addition to the operating systems being the same, all computers should be using the same ANSI collation language (specified via the Regional Settings icon).

Note If one of the following conditions is present, no Collation Mismatch errors will occur:

- Your application is connecting to a single Advantage Database Server

- Your application is connecting to just the Advantage Local Server

- USA ANSI collation language is always being used.

 

Note If you change your ANSI collation language from one language to another, you need to rebuild all of your index files.
