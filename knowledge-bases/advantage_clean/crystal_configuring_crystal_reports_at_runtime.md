---
title: Crystal Configuring Crystal Reports At Runtime
slug: crystal_configuring_crystal_reports_at_runtime
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_configuring_crystal_reports_at_runtime.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: b3a560bfee32927b8b48288340d0008b7252a006
---

# Crystal Configuring Crystal Reports At Runtime

Configuring Crystal Reports at Runtime

Configuring Crystal Reports at Runtime

Crystal Reports

| Configuring Crystal Reports at Runtime  Crystal Reports |  |  |  |  |

The most common way of connecting a Crystal Report to Advantage is through the use of aliases (See [Defining a Database Alias for use with Crystal Reports](crystal_defining_a_database_alias_for_use_with_crystal_reports.md) for more information). However, that method requires that at least some Advantage configuration settings be placed in the ads.ini file which then needs to be distributed with the report. This page describes a method in which the ads.ini file is not required and all the Advantage configuration settings are set at runtime when the report is run.

Ads.ini File Aliases and Runtime Options

When a report is designed in the Crystal Reports IDE, it is designed using an alias. The alias name is stored in the report and is used at runtime to gather configuration options from the ads.ini file. The only configuration option required to run the report is the connection path. This means that the connection path must either be set in the ads.ini file with the reports alias, or it must be specified at runtime via the DatabaseName report property. If the ads.ini file isnt found, or the alias isnt found in the ads.ini file, the default statement options will be used. Options set at runtime will override options found in the ads.ini file.

Advantage Runtime Report Options

The following options are allowed to be set in at runtime via the DatabaseName report property:

| Option Description | Option Name | Supported Values |
| Connection Path | DataDirectory | (Any connection path) |
| Connection Handle | ConnectionHandle | (String form of an Advantage Connection Handle) |
| Default Table Type | DefaultType | FoxPro, Clipper, Advantage (default is Advantage) |
| Compatibility Locking Mode | AdvantageLocking | On, Off (default is On) |
| Character Set | CharSet | Ansi, Oem (default is Ansi) |
| Collation Language | Language | (Any string Collation) ansi:en\_US, oem:cs\_CZ, etc. |
| Rights Checking Mode | RightsChecking | On, Off (default is On) |
| Username | UID | (Any username) |
| Password | PWD | (Any password) |
| Max number of closed cursors to cache | MaxTableCloseCache | (Any number, default is 25) |
| Show Deleted Rows | Rows | True, False (default is False) |
| Default Table Extension | TableExtension | Any file extension (default is ".adt") |
| Server Types | ServerTypes | 1 for local, 2 for remote, 4 for internet (default is 6, remote or internet) |
| Communication Compression | Compression | A, N, or I (Always, Never, Internet) |

Delphi Example

This example does not require an alias to be in the ads.ini file. All options not set via the DatabaseName property are set to their defaults.

procedure CrystalTest();

var

 Crpe1 : TCRpe;

begin

 try

   Crpe1 := TCRpe.Create( NIL );

   Crpe1.DiscardSavedData;

   Crpe1.ReportName := 'C:\test\_report.rpt';

   Crpe1.Connect.DatabaseName := 'DataDirectory=C:\data;RightsChecking=Off;';

   Crpe1.Show;

 finally

   Crpe1.CloseWindow;

   Crpe1.CloseJob;

   Crpe1.Destroy;

 end;

end;
