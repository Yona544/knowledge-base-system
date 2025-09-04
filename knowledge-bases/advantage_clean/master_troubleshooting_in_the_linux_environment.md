---
title: Master Troubleshooting In The Linux Environment
slug: master_troubleshooting_in_the_linux_environment
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_troubleshooting_in_the_linux_environment.htm
source: Advantage CHM
tags:
  - master
checksum: 3efab7a73919ed13bfa26ad98b6af9bb006a885a
---

# Master Troubleshooting In The Linux Environment

Troubleshooting in the Linux Environment

Troubleshooting in the Linux Environment

Troubleshooting

| Troubleshooting in the Linux Environment  Troubleshooting |  |  |  |  |

Error Logs

The Advantage Database Server provides error and warning information in these files: ads\_err.dbf, ads\_err.adt, assert.log, and ads\_log.txt. Errors and warnings are logged when a recoverable, invalid condition occurs on the Advantage Database Server.

The error log is either ads\_err.dbf (a DBF table) or ads\_err.adt (an ADT table), to which any application or data error or warning is recorded. The default is to use ads\_err.adt and can be controlled via the ERROR\_LOG\_TYPE configuration parameter. Errors and warnings written to this error log file are not necessarily critical errors but are key to tracing potential problems in the system or client applications. This error log may be configured to a maximum file size to prevent excessive disk space usage.

ads\_log.txt is a text file to which all fatal errors are logged. If the Advantage daemon will not load, crashes, or encounters any other critical errors, check the ads\_log.txt file for more information.

assert.log is a file to which critical Advantage internal assertion failures are recorded. Assertions are internal "sanity checks" placed throughout the Advantage Database Server code to verify that code paths and data are valid during operation. If an assertion failure occurs on your file server, the Advantage daemon will be stopped and a message will appear on in the ads\_log.txt file. An error will also be recorded to the Advantage error log file.

These log file locations are configurable, with the default directory being /var/log/advantage. If you modify the default location, verify that the advantage user has privileges to the directory in question. See [Advantage Database Server Configuration](master_advantage_database_server_configuration_overview.md) for more information.
