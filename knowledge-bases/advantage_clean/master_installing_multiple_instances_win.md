---
title: Master Installing Multiple Instances Win
slug: master_installing_multiple_instances_win
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_installing_multiple_instances_win.htm
source: Advantage CHM
tags:
  - master
checksum: 10978d90852a40a93127c3e881faba4404923fe9
---

# Master Installing Multiple Instances Win

Installing Multiple Instances on a Single Server in Windows

Installing Multiple Instances on a Single Server in Windows

Advantage Database Server

| Installing Multiple Instances on a Single Server in Windows  Advantage Database Server |  |  |  |  |

When installing multiple instances of the Advantage Database Server on Windows, each instance must be completely separate from other instances.  Changes must be made to the installer MSI file and the setup.ini file.

Modifying the MSI File

The setup.exe executable is used to generate the Product and Upgrade Codes along with modifying the MSI file.

Each side by side install needs a unique product name to prevent your instance of the Advantage Database Server from being uninstalled accidentally from the Add\Remove Programs Dialog.  Names with spaces should be wrapped in double quotes.   The following command line should be used with the setup.exe executable to create a side by side install.

setup.exe sidebyside  <your custom install name> [UpgradeCode] [ProductCode]

 

Every install is identified by two GUIDs:  the Product Code and the Upgrade Code.  To make a side by side install, both GUIDs must be changed.  The Product Code is used for all instances of a major product version.  For example, all 9.10 versions of the 32-bit Windows Advantage Database Server share the same Product Code.   The Upgrade Code is used to identify the side by side install of Advantage regardless of the version.  All versions of the 32-bit Windows Advantage Database Server since 8.10 share the same Upgrade Code.  The 32 and 64-bit versions of the Advantage Database Server for Windows must have different Product and Upgrade Codes.

The Upgrade Code should be generated once and then reused again for all side by side instances of that install.  If no Upgrade Code is specified when calling the setup executable, a GUID will be generated automatically.  The GUID must be in following format {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} with all letter uppercase.

The Product Code should be generated once for each major release and then reused for all minor releases.  If no Product Code is specified when calling the setup executable, a GUID will be generated automatically.  The GUID must be in following format {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX} with all letter uppercase.

Properties in the Setup.ini File

The setup executable must be informed that the install will be a side by side install.  This is done with the SideBySide flag in the Bootstrap section.

[Bootstrap]

SideBySide = 1

Installation Directory

Each instance of the Advantage Database Server must be installed into a different directory.   The INSTALLDIR entry of the setup.ini file should be set to a custom default for the install.  Do not use the default Advantage directory for this path.

[Properties]

INSTALLDIR= "c:\Program Files\Initech \Advantage 10.0\"

Error Log

Each instance of the Advantage Database Server must have a unique location to log errors to.  The CONFIG\_ERROR\_ASSERT\_LOGS entry of the setup.ini file should be set to a subdirectory under the install path.

[Properties]

CONFIG\_ERROR\_ASSERT\_LOGS     = "c:\Program Files\Initech\Advantage 10.0\logs"

TPS File Location

Each instance of the Advantage Database Server must have a unique location to create tops log files in.  The CONFIG\_ERROR\_ASSERT\_LOGS entry of the setup.ini file should be set to a subdirectory under the install path.

[Properties]

CONFIG\_TPS\_LOGS = "c:\Program Files\Initech\Advantage 10.0 \logs"

Service Name

Each Windows Service must have a unique name.  Service name comparisons are case insensitive and service names may not contain slashes.   The maximum length of a service name is 256 characters.  All configuration properties for this instance of the Advantage Database Server are stored in a registry key under the service name, \\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\<Service\_Name>\Configuration

[Properties]

SERVICE\_NAME = "Advantage\_Initech"

For the current example, registry information would be stored in \\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\_Initech\Configuration

Service Display Name

The name displayed by Windows user interface programs to identify the instance of Advantage.  The maximum length of a service display name is 256 characters and may not contain slashes.

[Properties]

SERVICE\_DISPLAY\_NAME = "Initech Instance of Advantage Database Server "

Service Description

Each service has an optional description associated with it.  Place any extra information that should be stored about the service here.

[Properties]

SERVICE\_DESCRIPTION = "Initech Instance of Advantage Database Server for Credit Union Account Management"

Start Menu

A shortcut to the Advantage Configuration Utility configured to manage the side-by-side instance of the Advantage Database Server will be created in the Windows Start Menu.  Each instance of the Advantage Database Server requires a unique short cut to the Advantage Configuration Utility.

[Properties]

STARTMENUNAME = "Initech"

LAN IP Port

Each instance of the Advantage Database Server requires a unique LAN IP Port for communication.   The value 6262 should not be used, since this is the standard Advantage Database Server port.   A list of common ports used by other applications can found at <http://www.iana.org/assignments/port-numbers>.  Selecting a port number from an unassigned range will greatly reduce the chance of collisions.

[Properties]

CONFIG\_RECEIVE\_IP\_PORT = 6299

Example

The following example is a completed setup.ini file to create a side by side installation for the version 10.0 32-bit version of Advantage Database Server.  The values of Msi and MSIProduct in the Bootstrap section would need to be modified for the 64-bit version of the Advantage Database Server.

[Bootstrap]

; The first four lines should never be modified

Msi=Advantage Database Server for Windows v10.0.msi

ProductName=Advantage Database Server for Windows

ProductSupport=Advantage Support (www.advantagedatabase.com)

MSIProductCode={F8E47026-F121-4C7F-BE32-2E2442F9DAF5}

 

; Set this parameter to 1 to signal that this is a side-by-side install.

SideBySide = 1

 

; The Parameters key allows additional command line switches to be appended

; when launching the windows installer. The "/q" disables the users interface

; (silent install). For details on Windows Installer command line switches:

; http://support.microsoft.com/default.aspx?scid=kb;EN-US;227091

;Parameters=/q

 

 

; To run the Advantage Database Server install without prompting the user for

; information, all values below must be specified.  If required values are

; missing, the install program will prompt the user for the missing information.

; To use silent install capabilities, remove the ";" from the beginning of each

; setting you want to use, and modify the value.

;

;    ------------------------------------------------------------------------------

;    NOTE: All values in the [Properties] section that contain spaces must be

;    quoted in order for the windows installer to corretly parse the values.

;    Example: REGISTERED\_OWNER="John Doe"

;    ------------------------------------------------------------------------------

;

; If INSTALLDIR is not specified, Advantage Database Server will be installed to

; the default location.

;

; The window prompting for serial number, validation code, and Register Owner

; will show if all three of these keys are not specified or Automatic Startup

; has a value that is not a 0 or a 1. If Automatic Startup is not specified but

; serial number, validation code, and Register Owner are specified then the

; window will not show but "AUTOMATIC\_STARTUP=1" is assumed.

;

; If OEM\_LANGUAGE or ANSI\_LANGUAGE is not set then the user will be prompted

; for the OEM and/or ANSI Language.

;

; The configuration parameters of the Advantage Database Server (ADS) can be

; modified during installation. This is useful when re-distributing the server

; with your application. Modifying parameter values, such as the file locations,

; adds consistency when deploying ADS with your application. Most of the other

; parameters do not need to be altered from their default values.

 

 

; You will need to create an ADS\_CFG.REG file by installing ADS and setting the

; parameter's values as desired. Execute REGEDIT.EXE and select the folder

; \\HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration.

; Export the configuration settings by selecting the "Registry" menu item and

; select "Export Registry File...". Name the file ADS\_CFG.REG. Copy the

; ADS\_CFG.REG file to the same location as this SETUP.INI file (along with

; SETUP.EXE and the MSI file). This registry file is executed before the

; installation program finishes. The file will be executed silently

; (i.e. "regedit.exe /s ads\_cfg.reg")

;

;    ------------------------------------------------------------------------------

;    NOTE: This functionality will not work when installing ADS on Windows NT 3.51.

;    No errors will be produced and the registry will not be modified to the values

;    in the registry file.

;    ------------------------------------------------------------------------------

 

 

; NOTE: All these parameters can also be specified as command-line parameters.

; This option can be valuable when calling this install from your own install and

; the files are on a CD, where this file is read only.

;

; Either command-line parameters or SETUP.INI settings can be used, BUT NOT BOTH.

; If ANY command-line parameters are given, the Parameters value (in Bootstrap

; section) and the entire Properties section of SETUP.INI will be ignored.

;

; Command line parameters must be specified with the full property name. Use quotes

; if the parameter value contains spaces.

;

; Example:

; Setup.exe /q SERIAL\_NUMBER=121212 VAL\_CODE=GHFYT REGISTERED\_OWNER=Owner OEM\_LANGUAGE=USA

 

 

 

 

[Properties]

; Path to the directory where the ADS files are to be installed.

INSTALLDIR="c:\Program Files\Initech\Advantage 10.0\"

 

; OEM language setting.  Options are:

; USA, DANISH, DUTCH, FINNISH, FRENCH, GERMAN, GREEK437, GREEK851, ICELD850,

; ICELD861, ITALIAN, NORWEGN, PORTUGUE, SPANISH, SWEDISH, MAZOVIA, PC\_LATIN,

; ISOLATIN, RUSSIAN, NTXCZ852, NTXCZ895, NTXSL852, NTXSL895, NTXHU852,

; NTXPL852, TURKISH, or BOSNIAN.

; These language character sets are taken from the EXTEND.CHR file.

;OEM\_LANGUAGE=USA

 

; Advantage Database Server Serial Number

;SERIAL\_NUMBER=

 

; Advantage Database Server Validation Code

; Use this for non-evaluation servers.

; Set the Validation Code or the Authorization Code but not both.

;VAL\_CODE=

 

; Advantage Database Server Authorization Code.

; Use this for evaluation servers only.

;AUTH\_CODE=

 

; Advantage Database Server Replication Code

; Use this for non-evaluation servers.

;REP\_CODE=

 

; Registered Owner

; Supply a string of less than 30 characters.

;REGISTERED\_OWNER=

 

; Whether the Advantage Database Server service is an automatic startup service.

; Specify 1 if you want the ADS service to be an automatic startup service.

; Specify 0 if you want the ADS service to be a manual startup service.

;AUTOMATIC\_STARTUP=1

 

 

; ANSI Character set

;

; <Default> = Use the currently configured ANSI character set that is active

;             on the workstation.

; If you do not wish to use the ANSI character set that is active on the

;   current workstation, the available ANSI character sets to be used are:

;     Danish, Dutch, Engl(Amer), Engl(UK), Engl(Can), Finnish, French,

;     French Can, German, Icelandic, Italian, Norwegian, Portuguese, Spanish,

;     Span(Mod), Swedish, Russian, ASCII, Turkish, Polish, Baltic, Ukrainian,

;     Duden\_DE.

;   The character sets are taken from the ANSI.CHR file.

;ANSI\_LANGUAGE=<Default>

 

; Overwrite the ANSI.CHR file?

; If ANSI.CHR already exist on your machine it is recommended that a new

; ANSI.CHR is installed. If support for another language has been added

; to your version of ANSI.CHR set this value to "NO".

; If a new language has not been added to the ANSI.CHR file then set

; this value to "YES".

; Do you want to install ANSI.CHR?

;NEW\_ANSI=YES

 

;   ------------------------------------------------------------------------------

;    The following section contains entries for doing a side by side install of

;    the Advantage Database Server on Windows.

;   ------------------------------------------------------------------------------

 

; Name of the service registered with Windows Service control manager.

; Service name comparisons are case insensitive and slashes are invalid

; characters.  Maximum length of the string is 256 characters.

SERVICE\_NAME = "Advantage\_Initech"

 

; Name displayed in the Service Control Manager user interface.  The

; maximum number of characters is 256.

SERVICE\_DISPLAY\_NAME = "Initech Instance of Advantage Database Server"

 

; Optional description displayed by the Service Control user interface.

SERVICE\_DESCRIPTION = "Initech Instance of Advantage Database Server for Credit Union Account Management."

 

; An IP port must be specified for the server to use.  Do not use the

; standard Advantage port of #6262.  A list of port numbers to avoid

; can be found at http://www.iana.org/assignments/port-numbers.

CONFIG\_RECEIVE\_IP\_PORT = #6299

 

; Specify a path for storing the error logs associated with this

; instance of Advantage.

CONFIG\_ERROR\_ASSERT\_LOGS = "c:\Program Files\Initech\Advantage 10.0\logs"

 

; Specify a path for creating the files used by the TPS system.

CONFIG\_TPS\_LOGS = "c:\Program Files\Initech\Advantage 10.0\logs"

 

; Set folder name under the Start Menu for this instance of

; Advantage.  The Advantage Configuration Utility in this

; folder will be used to control the side-by-side install.

STARTMENUNAME= "Initech"

 

 

[Uninstall]

; These keys will cause the setup.exe utility to uninstall Advantage

; Database Server (versions 7.0 and older) prior to the installation of

; the current version. Do not change these values.

;UninstallKey=Advantage Database Server for Windows NT/2000/2003

;UninstallVal=UninstallString

; The following command line parameters will may be appended to the uninstall

; string. They are optional, and may be used to execute the uninstall

; silently. For details on InstallShield command line parameters:

; http://support.installshield.com/kb/view.asp?articleid=q100021

;UninstallParams=-y -a
