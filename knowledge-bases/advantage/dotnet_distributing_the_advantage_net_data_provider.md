Distributing the Advantage .NET Data Provider




Advantage Database Server 12  

Distributing the Advantage .NET Data Provider

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Distributing the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Distributing the Advantage .NET Data Provider Advantage .NET Data Provider dotnet\_Distributing\_the\_advantage\_net\_data\_provider Advantage .NET Data Provider > Installation and Distribution > Distributing the Advantage .NET Data Provider / Dear Support Staff, |  |
| Distributing the Advantage .NET Data Provider  Advantage .NET Data Provider |  |  |  |  |

Advantage .NET Data Provider Files

When building an installation program for an Advantage .NET Data Provider application, the installation program should install several Advantage files and also possibly the Microsoft .NET Framework Redistributable.

The installation includes multiple versions of the Advantage .NET Data Provider. When you run the provider installation on your development machine, the installer will put the appropriate version of the provider into the Global Assembly Cache based on the version of the .NET Framework that exists on the machine. When you install your finished application, be sure to use the correct version of the provider. Under the Advantage .NET Data Provider install directory, there should be directories named "1.0\" and "2.0\". The 1.0 directory contains the Advantage .NET Data Provider for the Microsoft .NET Framework 1.x. The 2.0 directory contains the provider for the Microsoft .NET Framework 2.x and greater.

The third portion of the internal version number of the Advantage.Data.Provider.Dll reflects the version of the framework for which it is built; it is either "1" or "2" to indicate the .NET Framework 1.x or 2.x and greater. For example, Advantage.Data.Provider.dll v9.0.2.15 is built for the Microsoft .NET Framework 2.0.

Some or all of the following files will have to get redistributed and installed with your application.

|  |  |
| --- | --- |
| File | Description |
| Advantage.Data.Provider.DLL | The .NET assembly that contains the Advantage .NET Data Provider classes. |
| Advantage.Data.Entity.DLL | The .NET assembly for support of the ADO.NET Entity Framework. |
| ACE32.DLL / ACE64.DLL | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. |
| AXCWS32.DLL / AXCWS64.DLL | Advantage remote communication library used when accessing data via the [Advantage Database Server](master_advantage_database_server.htm). Also used when accessing data via international versions of the [Advantage Internet Server](master_advantage_internet_server.htm). This file is not necessary if only using the Advantage Local Server. |
| ADSLOC32.DLL / ADSLOC64.DLL | Advantage Local Server DLL. Contains the core local server functionality. This file is not necessary if only using the [Advantage Database Server](master_advantage_database_server.htm) and/or [Advantage Internet Server](master_advantage_internet_server.htm). |
| ADSLocal.CFG | [Advantage Local Server](master_advantage_local_server.htm) configuration file. This file only needs to be distributed if using the Advantage Local Server and you wish to use Local Server settings other than the default. If installed, place this file in the same directory as ADSLOC32.DLL. |
| Extend.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file only needs to be distributed if using a non-USA OEM character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file only needs to be distributed if not using a specified ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.htm) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| XXXX.ADD | Main [Advantage Data Dictionary](master_advantage_data_dictionary.htm) file, where the XXXX is the name that was given to the data dictionary database when it was created. If your application uses database tables and Advantage Data Dictionary functionality, this file must be distributed with your application. If the application connects to more than one Advantage Data Dictionary, each applicable .ADD file must be distributed with the application. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information about Advantage Data Dictionary functionality. |
| XXXX.AM | Advantage Data Dictionary file, where the XXXX is the name that was given to the data dictionary database when it was created. For each .ADD file that exists, a .AM file will exist. If distributing a .ADD file, the corresponding .AM file must also be distributed. |

Note To avoid conflicts that can occur with computers at the distribution site using various collation languages, do not distribute the corresponding .AI file (the Advantage Data Dictionary index file) that exists for each .ADD file. The .AI file will be automatically created at the distribution site when the Advantage Data Dictionary is first accessed. If upgrading an existing Advantage application that used an Advantage Data Dictionary, and replacing an old version of the Advantage Data Dictionary files with a new version of the Advantage Data Dictionary files, you should delete the old .AI file as part of the upgrade.

File Locations

All redistributable files except for database tables and data dictionaries should be placed in the application directory or somewhere in the clients path. Under normal situations, all of the DLLs, CFG, and CHR file should be placed in the same directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation.

Microsoft .NET Framework

To be able to run applications using the Advantage .NET Data Provider, you must, at a minimum, have the Microsoft .NET Framework Version 1.1 Redistributable installed on each target machine.