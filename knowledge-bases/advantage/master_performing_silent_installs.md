Performing Silent Installs




Advantage Database Server 12  

Performing Silent Installs

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Performing Silent Installs  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Performing Silent Installs Advantage Database Server master\_Performing\_silent\_installs Advantage Database Server > Installing the Advantage Database Server > Performing Silent Installs / Dear Support Staff, |  |
| Performing Silent Installs  Advantage Database Server |  |  |  |  |

Silent Installs are useful when calling the Advantage install from your own install. It can also be used so your customers are not required to input information such as paths or serial numbers.

The Advantage Windows based installs use the Microsoft Windows Installer. Silent installs can be accomplished by running the bootstrap utility with the /s command line parameter. Alternatively, the /q switch may be added to the Parameters key in the Bootstrap section of the SETUP.INI file:

[Bootstrap]

Parameters=/q

It is recommended that the bootstrap utility (SETUP.EXE) be used to start installs. While MsiExec.exe may be used directly with the appropriate command line switches (see Microsoft documentation for details), certain checks for platform requirements will be bypassed and any properties configured in the SETUP.INI file will be ignored. Server installations REQUIRE certain properties in order to run silently.

Advantage Database Server Installs

The Advantage Database Server installs require that certain properties be set in order to run silently. These properties are all listed in the Silent\_Install section of the SETUP.INI file. When the bootstrap utility (SETUP.EXE) is run, these properties will all be passed to the Windows Installer. If required information is missing or is invalid, the server install WILL NOT RUN SILENTLY. Silent installs should be tested to ensure all properties are set as you intended. See also [Modifying Configuration Parameters During Installation](master_modifying_configuration_parameters_during_installation.htm).

Advantage Client Installs

In most cases you would not want to run a silent install of the client software at your customer's site. It is more likely that you would install a few selected Advantage DLLs along with your application using your own installation program. See the Advantage Local Server Merge Module for Developers topic in the help file for information on automatically adding files and language configuration interfaces to you MSI install.