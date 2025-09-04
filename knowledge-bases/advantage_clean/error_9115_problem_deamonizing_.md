---
title: Error 9115 Problem Deamonizing
slug: error_9115_problem_deamonizing_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9115_problem_deamonizing_.htm
source: Advantage CHM
tags:
  - error
checksum: f90940dec150bf68d4a0386f04a50f87f9f74112
---

# Error 9115 Problem Deamonizing

9115 Problem "Deamonizing"

9115 Problem "Deamonizing"

Advantage Error Guide

| 9115 Problem "Deamonizing"  Advantage Error Guide |  |  |  |  |

The Advantage Database Server for Linux encountered a problem while attempting to "daemonize". One of the following operations may have failed:

- Fork new daemon process

- The "advantage" user was not found on the system

- User executing the Advantage Daemon does not have rights to change user IDs (not root)

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
