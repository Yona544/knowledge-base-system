---
title: Master Sp Mggetcrashdumpinfo
slug: master_sp_mggetcrashdumpinfo
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetcrashdumpinfo.htm
source: Advantage CHM
tags:
  - master
checksum: a3c5a66a4147032caf30d23332d51b6cb1f362d9
---

# Master Sp Mggetcrashdumpinfo

sp\_mgGetCrashDumpInfo

sp\_mgGetCrashDumpInfo

Advantage SQL Engine

| sp\_mgGetCrashDumpInfo  Advantage SQL Engine |  |  |  |  |

Retrieve a listing of ADSDump files located  on the server.

Syntax

EXECUTE PROCEDURE sp\_mgGetCrashDumpInfo()

Parameters

| CrashDumpName (O) | Filename of the ADSDump file. |
| CreationTime (O) | Timestamp the ADSDump file was created from the OS.  Note: This may differ slightly from the timestamp in the ADSDump filename. |
| FileSize (O) | The size of the file in Bytes. |

Remarks

sp\_mgGetCrashDumpInfo is an administrative procedure that will list the names, dates, and sizes of any existing crash dump files on the system.  This procedure may only be run on the active [root dictionary](master_root_dictionary.md) and the user must be a member of the SERVER:Admin group.

Example

EXECUTE PROCEDURE sp\_mgGetCrashDumpInfo();
