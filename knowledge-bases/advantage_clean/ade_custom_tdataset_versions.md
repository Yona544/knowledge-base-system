---
title: Ade Custom Tdataset Versions
slug: ade_custom_tdataset_versions
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_custom_tdataset_versions.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 910df23064e42fb55c419869f71833ac58acd290
---

# Ade Custom Tdataset Versions

Custom TDataSet Versions

Custom TDataSet Versions

Advantage TDataSet Descendant

Managing Multiple Versions

| Custom TDataSet Versions  Advantage TDataSet Descendant  Managing Multiple Versions |  |  |  |  |

Custom TDataSet Versions allow developers to configure the utility to be able to detect their own TDataSet classes that descend from the Advantage TDataSet Descendants as well as versions of the Advantage TDataSet Descendant prior to version 7.1.

To access this functionality, click on the "Configure Custom Versions" button on the main TDataSet Switch form. The menu that is displayed allows you to configure a TDataSet Descendant name and installation path. The configured TDataSet installation path should point to a directory structure that mirrors the TDataSet install directory. Specifically, this directory needs to contain "DelphiX" and "CBlderX" directories corresponding to each version of Delphi/C++ Builder that can use this version of the TDataSet. Additionally, the directory should contain a "Redistribute" directory that contains the ACE DLL files (ace32.dll, axcws32.dll, and adsloc32.dll) for this version of the TDataSet Descendant.

For instance, if Delphi 2006 and C++Builder 2007 are present for a given version of the TDataSet Descendant, the configured path should point to a directory that contains the following directories:

TDataSet\

TDataSet\Delphi2006\

TDataSet\CBlder2007\

TDataSet\Redistribute\
