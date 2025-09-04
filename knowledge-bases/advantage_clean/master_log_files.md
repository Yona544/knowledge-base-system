---
title: Master Log Files
slug: master_log_files
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_log_files.htm
source: Advantage CHM
tags:
  - master
checksum: d341ef8e7cd331da9157e20edc07bc5afb0001c7
---

# Master Log Files

Log Files

Linux Log Files

Advantage Concepts

| Linux Log Files  Advantage Concepts |  |  |  |  |

The Advantage Database Server for Linux uses the same general error log as all other Advantage servers (ads\_err.dbf and ads\_err.adt), but also includes a new text log (ads\_log.txt) used for reporting fatal errors. If the Advantage Database Server daemon stops responding, verify the process is still running and then check the ads\_log.txt file for error information.

The default location for both log files is in the /var/log/advantage directory. This location is configurable through the ERROR\_ASSERT\_LOGS parameter in the ads.conf file.

IMPORTANT NOTE: The "advantage" user must have write privileges to the error log directory, or it will not be able to create or write to the log files.
