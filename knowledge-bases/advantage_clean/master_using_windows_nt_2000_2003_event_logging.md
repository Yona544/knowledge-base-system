---
title: Master Using Windows Nt 2000 2003 Event Logging
slug: master_using_windows_nt_2000_2003_event_logging
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_using_windows_nt_2000_2003_event_logging.htm
source: Advantage CHM
tags:
  - master
checksum: e8c85401248fce82d75fad788021b340d491d49a
---

# Master Using Windows Nt 2000 2003 Event Logging

Using Windows Event Logging

Using Windows Event Logging

Advantage Database Server

| Using Windows Event Logging  Advantage Database Server |  |  |  |  |

Windows event logging provides a centralized way for applications and services to record events such as when a service was stopped or started as well as error conditions. The Windows Event Viewer provides a standard user interface for viewing logged events. There are three types of event logs:

- System Logtracks Windows system information

- Security Logtracks events triggered by security violations

- Application Logtracks events written by an application

The Event Viewer is accessed through the Administrative Tools group/folder. Select the type of log file you want to view (System, Security, or Application) from the Log menu option. Double click on any event in the events list to view event details.

Event Logging and the Advantage Database Server Service

Information, warnings and errors pertaining to the Advantage Database Server Service are recorded in the Event Application Log. Information messages are used to record when the Advantage Database Server Service was started or stopped. Advantage Database Server service warnings alert users of recoverable problems. Errors, however, are used to display non-recoverable conditions that are likely to cause a service failure.

The Advantage Database Server Service also maintains an error log for additional, non-system related Advantage Database Server errors. By default, the error log is located in the root directory of the drive where the Advantage Database Server is installed. The location of this log is configurable. For more information about the Advantage Database Server error log, see [Troubleshooting in the Windows Environment](master_troubleshooting_in_the_windows_nt_2000_2003_environment.md).
