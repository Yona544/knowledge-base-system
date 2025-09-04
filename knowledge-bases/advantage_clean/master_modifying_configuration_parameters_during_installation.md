---
title: Master Modifying Configuration Parameters During Installation
slug: master_modifying_configuration_parameters_during_installation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_modifying_configuration_parameters_during_installation.htm
source: Advantage CHM
tags:
  - master
checksum: 900db42711be16f591ee5dd0aa15cb80384578ab
---

# Master Modifying Configuration Parameters During Installation

Modifying Configuration Parameters During Installation

Modifying Configuration Parameters During Installation

Advantage Database Server

| Modifying Configuration Parameters During Installation  Advantage Database Server |  |  |  |  |

The configuration parameters of the Advantage Database Server for Windows can be modified during installation. This is useful when redistributing the Advantage Database Server with your application. Modifying parameter values, such as the file locations, adds consistency when deploying the Advantage Database Server with your application. Most of the other parameters do not need to be altered from their default values.

You will need to create an ADS\_CFG.REG file by installing the Advantage Database Server and setting the parameter's values as desired.

For the Advantage Database Server for Windows, execute REGEDIT.EXE and select the folder \\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration.

Copy this file to the location of the setup files (setup.exe, setup.ini and the Windows Installer package (.MSI file).

The registry file will be merged during the installation process. The file must reside in the same directory as SETUP.EXE, SETUP.INI and the Windows Installer package (MSI file). The file will be merged silently (i.e., "regedit.exe /s ads\_cfg.reg").

Note If for any reason the bootstrap utility (SETUP.EXE) is NOT being used, the INST\_SRC\_DIR property must be set to the location of the install files in order to merge the ADS\_CFG.REG file when calling MsiExec.exe. If the bootstrap utility is used, this property is set AUTOMATICALLY (do NOT set the property in SETUP.INI). See the SETUP.INI file in the server install directory for details on properties required for server installs.

See Also

[Performing Silent Installs](master_performing_silent_installs.md)
