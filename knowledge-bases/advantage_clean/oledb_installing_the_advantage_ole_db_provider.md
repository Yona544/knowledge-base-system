---
title: Oledb Installing The Advantage Ole Db Provider
slug: oledb_installing_the_advantage_ole_db_provider
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_installing_the_advantage_ole_db_provider.htm
source: Advantage CHM
tags:
  - oledb
checksum: 91ab08d7abfc4f0d8757a61282bff31b9673f9e9
---

# Oledb Installing The Advantage Ole Db Provider

Installing the Advantage OLE DB Provider

Installing the Advantage OLE DB Provider

Advantage OLE DB Provider (for ADO)

| Installing the Advantage OLE DB Provider  Advantage OLE DB Provider (for ADO) |  |  |  |  |

| 1. | Proceed through the introductory windows that appear on the screen. To properly perform string comparisons with local languages, Advantage provides OEM/localized character sets to match your country's language requirements. If your Advantage application uses OEM/localized character sets with Advantage Local Server, select the character set that matches your Advantage applications. Selecting a specific OEM/Localized character set for all Advantage installs will guarantee the OEM/Localized character sets used by all Advantage applications will be the same. |

| 2. | To properly perform string comparisons when using ANSI collation, Advantage provides ANSI character sets to match your country's language requirements. If your Advantage application uses ANSI character sets with Advantage Local Server, select an ANSI character set to be used by the Advantage Local Server. If <CURRENT SYSTEM LANGUAGE> is chosen, the currently configured ANSI character set will be used. If you do not wish to use the ANSI character set that is currently active, this setting can be used to select a specific character set. Selecting a specific ANSI language for all Advantage installs, rather than selecting <CURRENT SYSTEM LANGUAGE>, will guarantee the ANSI character sets used by all Advantage applications will be the same. It is recommended that <CURRENT SYSTEM LANGUAGE> not be chosen unless all clients are running the same Windows operating system with the same regional settings configured. |

Advantage OLE DB Provider Installed Files

The following files are installed when the Advantage OLE DB Provider is installed. The default installation directory for these files is c:\Program Files\Advantage X.x\OLEDB.

| File | Description |
| README.TXT | The Advantage OLE DB Provider readme file. Contains specific release level information about the Advantage OLE DB Provider that may not be in the ADSOLEDB.HLP Help documentation. |
| READ\_LOC.TXT | The Advantage Local Server readme file. Contains specific information about the Advantage Local Server. |
| ADSOLEDB.H | Header file used for developing the Advantage OLE DB Provider consumers in Microsoft Visual C++. |
| LICENSE.TXT | The software license agreement for this product. |
| ANSICHR.EXE | Utility for adding an ANSI collation language to ANSI.CHR. |
| DATA | Subdirectory with sample Advantage data. Includes the Microsoft Access Nwind.mdb database converted to the equivalent Advantage database. |

The following Help files are installed when the Advantage Help file directory is installed. The default installation directory for these files is c:\Program Files\Advantage X.x\HELP.

| File | Description |
| ADVANTAGE.HLP | Advantage master Help file. |
| ADVANTAGE.CNT | Advantage master contents file. ADVANTAGE.CNT must reside in the same location as the ADVANTAGE.HLP file. |
| ADSOLEDB.HLP | This Help documentation. |
| ADSOLEDB.CNT | Contents file for this Help file (ADSOLEDB.HLP). ADSOLEDB.CNT must reside in the same location as the ADSOLEDB.HLP file. |
| ADSERROR.HLP | The Advantage Error Guide Help file. This file contains error codes and explanations. |
| ADSERROR.CNT | Advantage error codes contents file. ADSERROR.CNT must reside in the same location as the ADSERROR.HLP file. |

The default installation directory for these files is C:\WINDOWS\SYSTEM and C:\Program Files\Advantage X.x\OLEDB\REDISTRIBUTE.

| File | Description |
| ADSOLEDB.DLL | Registered Dynamic-link library that implements the Advantage OLE DB Provider. Advantage DLLs are loaded by default from the directory in which this file was registered. This file will be registered in the Redistribute directory unless it was selected to only install these files to the System directory. In that case, this file will be registered in the System directory. |
| ACE32.DLL or ACE64.DLL | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. This file must be located in the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOC32.DLL OR ADSLOC64.DLL | Advantage Local Server DLL. Contains the core local server functionality. This file is not necessary if only using the Advantage Database Server and/or Advantage Internet Server. If the Advantage Local Server is being used, this file must be located in the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOCAL.CFG | Advantage Local Server configuration file. This file is only necessary if using the Advantage Local Server and you wish to use Local Server settings other than the default. |
| AXCWS32.DLL OR AXCWS64.DLL | Advantage remote communication library used when accessing data via the Advantage Database Server. This file is not necessary if only using the Advantage Local Server. If the Advantage Database Server is being used, this file must be located in the applications current working directory, the clients path, or the Windows system directory. |
| EXTEND.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file is only necessary if using a non-USA OEM character set with the Advantage Local Server. |
| ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file is only necessary if not using a specified ANSI character set with the Advantage Local Server. |

Advantage Client Engine API

The Advantage Client Engine API can be optionally installed from the Advantage product CD. The Advantage Client Engine API installation includes the files necessary to directly write to the Advantage Client Engine API from your application. This includes the Pascal .PAS for Delphi applications, and the C++ .H and .LIB files for C++ applications. The Advantage Client Engine API also includes Advantage Client Engine DLLs, utilities, Help files, Readme files, and other informational text files.

Advantage Data Architect

The Advantage Data Architect can be optionally installed from the Advantage product CD. The Advantage Data Architect is a 32-bit application used for developing and maintaining databases and database applications. Data may be imported from Access 2000, SQL Server 7 or greater, or any version of Paradox, dBASE, or FoxPro to the Advantage Database Table format. Developers are also able to use the Advantage Management Utility or test functionality such as scopes, filters, searches, etc. The Advantage Data Architect works with both the [Advantage Local Server](master_advantage_local_server.md) and the [Advantage Database Server](master_advantage_database_server.md) Source code is included.

MDAC SDK

The primary source of information for OLE DB is the OLE DB Programmers Reference available with the Microsoft Data Access Components (MDAC) SDK.

Advantage does not install the MDAC SDK. To develop OLE DB applications, it may be necessary to install the MDAC SDK in order to get the necessary development tools depending on your development environment. At a minimum, it is necessary to install MDAC (the redistributable components) to use the OLE DB provider. For installation information, see the Universal Data Access Web site at http://www.microsoft.com/data.
