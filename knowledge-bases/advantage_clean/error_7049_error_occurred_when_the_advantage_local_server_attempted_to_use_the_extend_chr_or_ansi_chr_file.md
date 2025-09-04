---
title: Error 7049 Error Occurred When The Advantage Local Server Attempted To Use The Extend Chr Or Ansi Chr File
slug: error_7049_error_occurred_when_the_advantage_local_server_attempted_to_use_the_extend_chr_or_ansi_chr_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7049_error_occurred_when_the_advantage_local_server_attempted_to_use_the_extend_chr_or_ansi_chr_file.htm
source: Advantage CHM
tags:
  - error
checksum: ace90b8d0fbc73883e54c261e111b29341c28fcc
---

# Error 7049 Error Occurred When The Advantage Local Server Attempted To Use The Extend Chr Or Ansi Chr File

7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file

7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file

Advantage Error Guide

| 7049 Error occurred when the Advantage Local Server attempted to use the EXTEND.CHR or ANSI.CHR file  Advantage Error Guide |  |  |  |  |

Problem: The Advantage Local Server had a problem when using the EXTEND.CHR or ANSI.CHR file. Either it could not be opened, could not be read from, or did not contain the expected data.

Solution: Verify the OEM\_CHAR\_SET configuration setting in ADSLOCAL.CFG is a valid OEM character set language available in EXTEND.CHR. Also verify the ANSI\_CHAR\_SET configuration setting in ADSLOCAL.CFG is a valid ANSI character set language available in ANSI.CHR. Re-install the EXTEND.CHR or ANSI.CHR from the installation diskette.
