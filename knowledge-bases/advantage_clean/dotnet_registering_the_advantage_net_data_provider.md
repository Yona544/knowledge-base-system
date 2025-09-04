---
title: Dotnet Registering The Advantage Net Data Provider
slug: dotnet_registering_the_advantage_net_data_provider
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_registering_the_advantage_net_data_provider.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 606d54e975571023fbe67f10035617df64037445
---

# Dotnet Registering The Advantage Net Data Provider

Registering the Advantage .NET Data Provider

Registering the Advantage .NET Data Provider

Advantage .NET Data Provider

| Registering the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  |  |  |

When distributing your application, it may be necessary to register the Advantage .NET Data Provider in the Global Assembly Cache (GAC). It is possible to load the Advantage .NET Data Provider from your application without the provider being registered in the GAC if you are simply using the Advantage objects directly in your code. But, if you are using components that refer to .NET data providers in a generic fashion, or if you are using DbProviderFactories, then you will need to have the provider installed into the GAC. If you are writing your own installer, please refer to your installation utility's manual for instructions on installing an assembly into the GAC. It is possible to use the command line utility gacutil.exe to do this. For example, run the following command from a DOS command prompt:

gacutil /i Advantage.Data.Provider.dll

To remove the assembly from the GAC, use a similar command such as the following. Note that a specific version can also be included in the uninstall command, if necessary.

gacutil /u Advantage.Data.Provider

gacutil /u "Advantage.Data.Provider, Version=8.1.2.0"

.NET Framework

It is possible to install assemblies into the GAC from the Microsoft .NET Framework Configuration utility, which can be accessed from the Control Panel under the Administrative Tools.

It may also be necessary to add an entry to the .NET Framework machine.config file. If you are using DbProviderFactories to generically access the Advantage .NET Data Provider (as opposed to explicitly using the Advantage object instances), then the provider must be listed in the machine.config file. The file is located in a directory dependent on the version of the .NET Framework that is installed. For example, c:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\CONFIG\machine.config.

The new entry belongs in the DbProviderFactories section. The following is an example entry. The machine.config file should be backed up before modifying it. It is an XML file with a strict format. If the file is modified incorrectly, some applications, such as Visual Studio, may not load. Note that if you include the version portion of the entry, only that specific version of the provider will be used. If that version is not available on the machine, the system will not load another version. If the version information is not entered, it will not be tied to a specific version of the Advantage .NET Data Provider, which may be simpler when updating the provider with a new version but could lead to instability if your application is dependent on a specific version of the provider.

<system.data>

<DbProviderFactories>

<add name="Advantage Data Provider" invariant="Advantage.Data.Provider" description=".Net Framework Data Provider for Advantage Database Server" type="Advantage.Data.Provider.AdsFactory, Advantage.Data.Provider, Version=8.1.2.0, Culture=neutral, PublicKeyToken=e33137c86a38dc06"/>

</DbProviderFactories>

</system.data>
