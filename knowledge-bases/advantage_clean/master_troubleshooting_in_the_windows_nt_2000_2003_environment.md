---
title: Master Troubleshooting In The Windows Nt 2000 2003 Environment
slug: master_troubleshooting_in_the_windows_nt_2000_2003_environment
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_troubleshooting_in_the_windows_nt_2000_2003_environment.htm
source: Advantage CHM
tags:
  - master
checksum: bfd6b67dd2e6108460a0be691637b2e62a296f9a
---

# Master Troubleshooting In The Windows Nt 2000 2003 Environment

Troubleshooting in the Windows Environment

Troubleshooting in the Windows Environment

Troubleshooting

| Troubleshooting in the Windows Environment  Troubleshooting |  |  |  |  |

Note The Advantage Database Server for Windows is a Windows Service. It cannot run as a standard Windows application. If running the Advantage Database Server Service is attempted from Windows 98 or Windows ME, the following error will occur: "The ADS.EXE file is linked to missing export NETAPI32.DLL NetShareGet Info". Refer to Installing and Starting the Advantage Database Server for Windows for more information on Windows Services and how to start them.

Event Log

Windows event logging provides a centralized way for applications and services to record events such as when a service was stopped or started as well as error conditions. The Windows Event Viewer provides a standard user interface for viewing logged events. There are three types of event logs:

- System Log - tracks Windows system information

- Security Log - tracks events triggered by security violations

- Application Log - tracks events written by an application

The Event Viewer is accessed through the Administrative Tools group/folder. Select the type of log file you want to view (System, Security, or Application). Double click the event in the list to view the Event Detail Window.

Information, warnings, and errors pertaining to the Advantage Database Server Service is recorded in the Event Viewer Application Log. Information messages are used to record when the Advantage Database Server Service was started or stopped. Advantage Database Server Service warnings alert users of recoverable problems. Errors, however, are used to display non-recoverable conditions that are likely to cause an application failure.

Error Log

For troubleshooting purposes, the Advantage Database Server Service maintains an error log file, which can be either ADS\_ERR.DBF or ADS\_ERR.ADT.

As a default, the error log is located in the root of the C: drive. This error log file may be configured to be located on any valid server directory. When an error occurs, pertinent error information is appended to this file.

Errors are logged when a recoverable, invalid condition occurs in the Advantage Database Server Service. All errors are returned to the client. For specific error explanations, see the online Error Help file, ADSERROR.HLP.

Assertions

A primary functional requirement of the Advantage Database Server Service is to not cause an exception or server crash. During development of the Advantage Database Server Service, every effort was made to detect possible causes of exceptions and to properly recover in those situations.

As an additional safeguard, the Advantage Database Server Service contains assertion checks. An assertion check is a run-time verification of the current state of the Advantage Database Server Service. Assertion checks are used to verify function parameters, memory contents, etc. Assertion checks will halt Advantage Database Server Service processing when an unknown state is encountered, rather than allow the Advantage Database Server Service to continue processing and possibly cause an exception.

A failed assertion check causes the currently active Advantage Database Server Service thread to enter an infinite loop that displays a warning message on the main console screen of the server. A message box is also displayed on the server screen. An entry is made in the Advantage Assert Log (ASSERT.LOG) and a current Advantage Database Server Service memory dump is written to an ADS\_SNAP.LOG file. By default, the ASSERT log file and ADS\_SNAP.LOG file are located at the root of the C: drive.

The ASSERT log file can be configured to be located on any valid server directory.

Important! If an assertion failure occurs, all users must exit their Advantage applications.

Stopping an Advantage Database Server Service in an assertion failure state does not generally cause problems. However, an assertion failure creates an unknown state, so the possibility exists that an exception may occur. To minimize possible damage:

| 1. | Have all users connected to the Advantage Database Server exit their applications. |

| 2. | Wait a few minutes for the server to flush all buffers. |

| 3. | Stop the Advantage Database Server Service. Once the Advantage Database Server Service is stopped, you can resume normal activity. |

| 4. | Save the following files: |

- Advantage Assert Log file (ASSERT.LOG)

- The ADS\_SNAP.LOG file containing the Advantage Database Server memory dump

- Advantage Database Server Error Log file (ADS\_ERR.DBF)

| 5. | After you save the necessary files, re-start the Advantage Database Server Service and resume your Advantage applications. Then, contact Advantage Technical Support. |
