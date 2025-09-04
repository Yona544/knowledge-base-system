---
title: Ade Silent Mode
slug: ade_silent_mode
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_silent_mode.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 31aefa5bc39ae6e225f2dd3048b3c142a6391bf5
---

# Ade Silent Mode

Silent Mode

Silent Mode

Advantage TDataSet Descendant

Managing Multiple Versions

| Silent Mode  Advantage TDataSet Descendant  Managing Multiple Versions |  |  |  |  |

To facilitate the use of batch files to automate switching between TDataSet Versions, the Switch utility can operate in a silent mode. To use the utility in silent mode, specify all required parameters via the command-line.

The command-line syntax is as follows:

TDataSet\_Switch.exe <Delphi\_IDE\_Ver> <New\_TDS\_Ver> [<Current\_TDS\_Ver>]

Where <Delphi\_IDE\_Ver> is the version of Delphi/C++Builder whose installed TDataSet is to be changed, <New\_TDS\_Ver> is the version of the TDataSet to switch to, and <Current\_TDS\_Ver> is the currently-installed TDataSet version for the Delphi IDE specified.

Note If <Current\_TDS\_Ver> is specified, the current TDataSet version will be backed-up.

To change the installed TDataSet version for Delphi 7 to version 7.1 without backing up the current TDataSet version, the following command would be used:

TDataSet\_Switch.exe "Delphi 7" "Version 7.1"
