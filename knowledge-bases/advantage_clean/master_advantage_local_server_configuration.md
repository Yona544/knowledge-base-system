---
title: Master Advantage Local Server Configuration
slug: master_advantage_local_server_configuration
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_local_server_configuration.htm
source: Advantage CHM
tags:
  - master
checksum: 862533eb0497a773aac67f8a9679060ca3d0d220
---

# Master Advantage Local Server Configuration

Advantage Local Server Configuration

Advantage Local Server Configuration

Advantage Concepts

| Advantage Local Server Configuration  Advantage Concepts |  |  |  |  |

The Advantage Local Server can be configured in a variety of ways to fine-tune the Advantage Local Server to more effectively use resources. This topic describes the configuration information available with the Advantage Local Server. A configuration file, ADSLOCAL.CFG, is provided with the Advantage Local Server to ease in assigning and re-using configuration parameters. The parameters in ADSLOCAL.CFG can be changed by editing the file with a standard text editor. The configuration file is used when the Advantage Local Server DLL is loaded into memory. If an application is already running that is using the Advantage Local Server, you must re-start the Advantage Local Server application to use any newly changed settings.

The ADSLOCAL.CFG file follows standard INI file format with "keyword=value" type of entries. Therefore, it may be possible to use existing APIs to programmatically manage the configuration file if desired. For example, the Win32 development environment has APIs such as GetPrivateProfileString and WritePrivateProfileString for reading and writing string values in INI files. It may be necessary to add a section name to the file in order to use the APIs. Beginning with version 6.2, the shipping ADSLOCAL.CFG file contains a section title [SETTINGS] at the top of the file.

Low Lock Offsets

Windows

Default = 0 Range = 0 1

Linux

Default = 1 Range = 0 1

Keyword = USE\_LOW\_LOCK\_OFFSETS

Linux kernels older than version 2.4 did not have full support for large files (files greater than 2 GB). Standard lock offsets for ADT tables start above the 2 GB range, and could not be supported with older Linux kernels. Because of this, a new lock offset range was declared and used by default from the Advantage Local Server for Linux (no matter what the kernel version). The Windows version of the Advantage Local Server still defaults to the "standard" high lock offsets. All clients sharing ADT tables should use the same lock offset range.

To use low lock offsets, and therefore maintain lock offset compatibility no matter what version of the Linux kernel is in use:

USE\_LOW\_LOCK\_OFFSETS=1

To use high lock offsets, which will avoid lock/data collision for tables that have over 2GB of data:

USE\_LOW\_LOCK\_OFFSETS=0

The USE\_LOW\_LOCK\_OFFSETS configuration parameter is not included in the adslocal.cfg file by default. Manually add the entry if necessary.

Important If all clients (Windows and Linux) sharing tables do not have the same lock offset setting data corruption will occur.

Number of Connections

Default = 20. Range = 1 - no upper limit.

Keyword = CONNECTIONS

This is the initial number of connections that can be active with the Advantage Local Server at one time. Connections are defined as a single application using the Advantage Local Server DLL. Additional "connections" to the Advantage Local Server can be obtained via calls to the Advantage "connect" API, using an Advantage connection component, or using an Advantage connection object.

For example, to minimize memory usage, if you only have 2 connections to the Advantage Local Server, you can save a small amount of memory by configuring the number of connections to 2.

If your Advantage application attempts to connect to the Advantage Local Server more times than there are number of connections configured, the Advantage Local Server will attempt to allocate more resources to accommodate more connections. If that allocation fails, the application will receive a 7033 error, Connection Table Full, until a connection becomes available.

Number of Tables

Default = 50. Range = 1 no upper limit.

Keyword = TABLES

This is the initial number of tables that can be open at one time. To be safe, this setting should be at least as large as the number of tables you open in your application.

If your Advantage application attempts to open a table via the Advantage Local Server that has not yet been opened by your application, and the configured number of tables have already been opened, the Advantage Local Server will attempt to allocate more resources to accommodate more tables. If that allocation fails, your Advantage application will receive a 7005 error, Maximum number of tables exceeded, until a table "element" becomes available.

Number of Index Files

Default = 75. Range = 1 no upper limit.

Keyword = INDEXES

This is the initial number of index files that can be open at any one time.

If your Advantage application attempts to open an index file via the Advantage Local Server that has not yet been opened by your application, and the configured number of index files have already been opened, the Advantage Local Server will attempt to allocate more resources to accommodate more index files. If that allocation fails, your Advantage application will receive a 7006 error, Maximum number of index files exceeded, until an index file "element" becomes available.

Note This configurable setting is per index FILE. It does not matter if the index file is a single-order index file, such as an NTX or IDX index, or if it is a multiple-order index file, such as a CDX or ADI index. The number of orders that exist in a CDX or ADI index file that are opened has no effect on this setting.

Number of Data Locks

Default = 500. Range = 1 - no upper limit.

Keyword = LOCKS

This is the initial number of record locks, table locks, implicit header locks, and implicit index locks that can be in effect at one time. It may not be necessary to change this parameter. Increase this parameter only if Data Locks have been rejected. Reducing this setting is hardly necessary as very little memory will be saved.

If your Advantage application attempts to obtain a record, table, or index lock, and the configured number of data locks have already been used, the Advantage Local Server will attempt to allocate more resources to accommodate more data locks. If that allocation fails, your application will receive a 7007 error, Maximum number of locks exceeded, until a lock "element" becomes available. Data locks take very little memory. Setting this value to a very high number should not require much RAM to be used.

Maximum Size of Error Log

Default = 1000 KBytes. Range = 1 KByte - no upper limit.

Keyword = ERROR\_LOG\_MAX

The error log file size is the maximum file size the error log file (ADS\_ERR.DBF or ADS\_ERR.ADT), can reach. Once the maximum file size is attained, the first one-third of the records in the error log table are marked for deletion and packed automatically. With ADS\_ERR.DBF, new entries are appended to the end of the file. With ADS\_ERR.ADT, record recycling is used, so the new entries may not be at the physical end of the table. Viewing ADS\_ERR.ADT in ERROR\_NUMBER index order will ensure that the errors are displayed in the order they are logged.

The error log is a table used to record any errors encountered by the Advantage Database Server during execution of client applications. The ADS\_ERR.DBF error log file may be viewed using any standard DBF utility. ADS\_ERR.ADT is an Advantage proprietary format table and can be viewed with Advantage Data Architect.

Error Log and Assert Log Path

Default = Root of the C: drive.

Keyword = ERROR\_ASSERT\_LOGS

The Advantage Local Server error log, ADS\_ERR.ADT or ADS\_ERR.DBF, and assertion failure log, ASSERT.LOG, files may be stored in any directory.

ANSI Character Set

Default = Use the currently configured ANSI character set that is active on the workstation. Options are: Baltic, Danish, Dutch, Engl(Amer), Engl(UK), Engl(Can), Finnish, French, French Can, German, Duden\_DE, Icelandic, Italian, Norwegian, Polish, Portuguese, Spanish, Span(Mod), Swedish, Russian, ASCII, Turkish, or Ukrainian.

Keyword = ANSI\_CHAR\_SET

This is the ANSI character set that can be used when reading and storing data in tables opened with ANSI specified as the character set type. If this value is not specified, the currently configured ANSI character set on the workstation will be used. If you do not wish to use the ANSI character set that is active on the current workstation, this setting can be used to select one. This setting is useful to guarantee that the same ANSI character set is used both by local connections using the Advantage Local Server and remote connections to the Advantage Database Server. This setting does not apply to tables opened with OEM as the specified character set type.

Note The Duden\_DE collation is the same as the German collation except that it makes the following characters equivalent to each other: A = Ä, a = ä, O = Ö, o = ö, U = Ü, and u = ü. Because of this mapping, the Xbase DESCEND() function may not produce results identical to a descending index on the same data.

OEM/Localized Character Set

Default = USA. Options are: USA, BOSNIAN, DANISH, DUTCH, FINNISH, FRENCH, GERMAN, GREEK437, GREEK851, ICELD850, ICELD861, ITALIAN, NORWEGN, PORTUGUE, SPANISH, SWEDISH, MAZOVIA, PC\_LATIN, ISOLATIN, RUSSIAN, NTXCZ852, NTXCZ895, NTXSL852, NTXSL895, NTXHU852, NTXPL852, or TURKISH.

Keyword = OEM\_CHAR\_SET

This is the OEM/Localized character set used when reading and storing data in tables opened with OEM specified as the character set type. This setting does not apply to tables opened with ANSI as the specified character set type.

Local File Flush Frequency

Default = 20000 milliseconds (20 seconds). Range = 0 milliseconds -100000.

Keyword = FLUSH\_FREQUENCY

Windows 98, ME, NT, 2000, and 2003 do not always commit (flush) to disk updates made to files opened on the local computer in a timely manner. This Local File Flush Frequency value determines how often updates to files on local hard drives are forcibly flushed to disk by an Advantage background local server thread. This value does not have any effect on files opened on remote drives, since the Windows operating systems seems to flush updates to disk on remote files in a timely manner. As this flush time interval decreases, the committing of local file updates occurs more often, which increases data stability (in cases where the client computer crashes), but decreases application performance. Setting this value to zero disables the forcible flush to disk functionality.

Lowercase All Paths

Default = 0 (for false). Options are 0 (for false) or 1 (for true)

Keyword = LOWERCASE\_ALL\_PATHS

This option can be used to force the Advantage Local Server for Linux to change all paths and filenames to lowercase before attempting to access them on disk. This option is ignored by the Advantage Local Server DLL for Windows.
