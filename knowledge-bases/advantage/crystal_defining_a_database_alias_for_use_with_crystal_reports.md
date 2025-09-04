Defining a Database Alias for use with Crystal Reports




Advantage Database Server 12  

Defining a Database Alias for use with Crystal Reports

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Defining a Database Alias for use with Crystal Reports  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Defining a Database Alias for use with Crystal Reports Crystal Reports crystal\_Defining\_a\_database\_alias\_for\_use\_with\_crystal\_reports Advantage Crystal Reports > Using the Advantage Crystal Reports Driver > Defining a Database Alias for use with Crystal Reports / Dear Support Staff, |  |
| Defining a Database Alias for use with Crystal Reports  Crystal Reports |  |  |  |  |

The most common way of connecting a Crystal Report to Advantage is through the use of aliases (see [Configuring Crystal Reports at Runtime](crystal_configuring_crystal_reports_at_runtime.htm) for a more advanced method). Aliases are added to the [DATABASES] section in the ADS.INI file located in the WINDOWS directory (by default). Advantage clients use the search path to locate the ads.ini file, so this file can be placed in your application's directory or anywhere in the search path of the client machine. The key name is the name of the alias and the value is the "Data Path", semicolon, followed by the first letter of the index type. For example, adding an alias name "MyAlias" with a data path of "C:\MYPATH" using index type ADT will cause "MyAlias=C:\MYPATH;A" to be written to the ADS.INI file under the [DATABASES] section.

The ADS.INI file can be modified using a text editor, programmatically through Windows ini manipulation APIs, or it can be modified using the Advantage Data Architect (via the Connection Repository).

Example ADS.INI file:

[Settings]

ADS\_SERVER\_TYPE=2

[Databases]

ADS\_ADT=x:\MyAdtFiles;A

ADS\_CDX=x:\MyDbfFiles;C

ADS\_DD=x:\MyFiles\mydiction.add;D

The ADS\_SERVER\_TYPE key in the ADS.INI file can be used to select the Advantage server type(s) to use when obtaining an Advantage server connection. The available Advantage Server types are:ADS\_REMOTE\_SERVER which is the Advantage Database Server, ADS\_AIS\_SERVER which is the Advantage Internet Server, and ADS\_LOCAL\_SERVER which is the Advantage Local Server.

These Advantage server type constants are defined in the ACE.H and ACE.PAS files. ADS\_REMOTE\_SERVER has the value 2, ADS\_AIS\_SERVER has the value 4, and ADS\_LOCAL\_SERVER has the value 1. For example, if you wanted your Advantage application to attempt to connect to all Advantage server types, if necessary, you need to set the value for the ADS\_SERVER\_TYPE key to 7 (1 + 2 + 4 = 7). The default ADS\_SERVER\_TYPE value is to use ADS\_REMOTE\_SERVER and ADS\_AIS\_SERVER, which is 6 (2 + 4 = 6).