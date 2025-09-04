---
title: Dotnet Installing The Advantage Net Data Provider
slug: dotnet_installing_the_advantage_net_data_provider
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_installing_the_advantage_net_data_provider.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c76e44124bb822b1b0d144acdbc997db0a13044b
---

# Dotnet Installing The Advantage Net Data Provider

Installing the Advantage .NET Data Provider

Installing the Advantage .NET Data Provider

Advantage .NET Data Provider

| Installing the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  |  |  |

| 1. | Proceed through the introductory windows that appear on the screen. To properly perform string comparisons with local languages, Advantage provides OEM/localized character sets to match your country's language requirements. If your Advantage application uses OEM/localized character sets with Advantage Local Server, select the character set that matches your Advantage applications. Selecting a specific OEM/Localized character set for all Advantage installs will guarantee the OEM/Localized character sets used by all Advantage applications will be the same. |

 

| 2. | To properly perform string comparisons when using ANSI collation, Advantage provides ANSI character sets to match your country's language requirements. If your Advantage application uses ANSI character sets with Advantage Local Server, select an ANSI character set to be used by the Advantage Local Server. If <CURRENT SYSTEM LANGUAGE> is chosen, the currently configured ANSI character set will be used. If you do not wish to use the ANSI character set that is currently active, then select a specific character set from the list. Selecting a specific ANSI language for all Advantage installs, rather than selecting <CURRENT SYSTEM LANGUAGE>, will guarantee the ANSI character sets used by all Advantage applications will be the same. It is recommended that <CURRENT SYSTEM LANGUAGE> not be chosen unless all clients are running the same Windows operating system with the same regional settings configured. |

Advantage .NET Data Provider Installed Files

The following files are installed when the Advantage .NET Data Provider is installed. The default installation directory for these files is C:\[Program Files]\Advantage X.x\ADO.NET.

| File | Description |
| License.TXT | The software license agreement for this product. |
| ANSICHR.EXE | Utility for adding an ANSI collation language to ANSI.CHR. |
| Advantage.Data.Provider.DLL | The .NET assembly that contains the Advantage .NET Data Provider classes. |
| ACE32.DLL | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. This file must be located in the same directory as advantage.data.provider.dll, the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOC32.DLL | Advantage Local Server DLL. Contains the core local server functionality. This file is not necessary if only using the Advantage Database Server and/or Advantage Internet Server. If the Advantage Local Server is being used, this file must be located in the same directory as advantage.data.provider.dll, the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOCAL.CFG | [Advantage Local Server](master_advantage_local_server.md) configuration file. This file is only necessary if using the Advantage Local Server and you wish to use Local Server settings other than the default. |
| AXCWS32.DLL | Advantage remote communication library used when accessing data via the [Advantage Database Server](master_advantage_database_server.md). This file is not necessary if only using the Advantage Local Server. If the Advantage Database Server is being used, this file must be located in the same directory as advantage.data.provider.dll, the applications current working directory, the clients path, or the Windows system directory. |
| Extend.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file is only necessary if using a non-USA OEM character set with the Advantage Local Server. |
| ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file is only necessary if not using a specified ANSI character set with the Advantage Local Server. |
| Advantage.Data.Entity.dll | The .NET assembly used to interface with the ADO.NET Entity Framework. |

The following Help files are installed when the Advantage Help file directory is installed. The default installation directory for these files is C:\[Program Files]\Advantage X.x\help.

| File | Description |
| Advantage.chm | Advantage Help file. |

Advantage Data Architect

The [Advantage Data Architect](master_advantage_data_architect.md) can be optionally installed from the Advantage product CD. The Advantage Data Architect is a 32-bit application used for developing and maintaining databases and database applications. Data may be imported from Access 2000, SQL Server 7 or greater, or any version of Paradox, dBASE, or FoxPro to the Advantage Database Table format. Developers are also able to use the Advantage Management Utility or test functionality such as scopes, filters, searches, etc. The Advantage Data Architect works with both the Advantage Local Server and the Advantage Database Server Source code is included.
