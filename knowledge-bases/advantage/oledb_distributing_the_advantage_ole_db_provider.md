Distributing the Advantage OLE DB Provider




Advantage Database Server 12  

Distributing the Advantage OLE DB Provider

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Distributing the Advantage OLE DB Provider  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Distributing the Advantage OLE DB Provider Advantage OLE DB Provider (for ADO) oledb\_Distributing\_the\_advantage\_ole\_db\_provider Advantage OLE DB Provider (for ADO) > Installation and Distribution > Distributing the Advantage OLE DB Provider / Dear Support Staff, |  |
| Distributing the Advantage OLE DB Provider  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Building an Installation Program

When building an installation program for an Advantage OLE DB Provider application, the installation program should install several Advantage files, register the Advantage OLE DB Provider on each client computer, and also probably redistribute MDAC.

Advantage OLE DB Provider Files

Some or all of the following files will have to get redistributed and installed with your application.

|  |  |
| --- | --- |
| File | Description |
| ADSOLEDB.DLL | Dynamic-link library that implements the Advantage OLE DB Provider. This DLL must be installed in any directory to which the client computer has access. |
| ACE32.DLL or ACE64.DLL | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. This file must be installed into the same directory as ADSOLEDB.DLL, the applications current working directory, the clients path, or the Windows system directory. |
| AXCWS32.DLL or AXCWS64.DLL | Advantage remote communication library used when accessing data via the Advantage Database Server. This file is not necessary if only using the Advantage Local Server. If the Advantage Database Server is being used, this file must be installed into the same directory as ADSOLEDB.DLL, the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOC32.DLL or ADSLOC64.DLL | [Advantage Local Server](master_advantage_local_server.htm) DLL. Contains the core Advantage Local Server functionality. This file is not necessary if only using the Advantage Database Server. If the Advantage Local Server is being used, this file must be installed into the same directory as ADSOLEDB.DLL, the applications current working directory, the clients path, or the Windows system directory. |
| ADSLOCAL.CFG | [Advantage Local Server configuration](master_advantage_local_server_configuration.htm) file. This file only needs to be distributed if using the Advantage Local Server and you wish to use Local Server settings other than the default. If installed, place this file in the same directory as ADSLOC32.DLL. |
| EXTEND.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file only needs to be distributed if using a non-USA OEM character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file only needs to be distributed if not using a specified ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.htm) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| XXXX.ADD | Main Advantage Data Dictionary file, where the XXXX is the name that was given to the data dictionary database when it was created. If your application uses database tables and Advantage Data Dictionary functionality, this file must be distributed with your application. If the application connects to more than one Advantage Data Dictionary, each applicable .ADD file must be distributed with the application. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information about Advantage Data Dictionary functionality. |
| XXXX.AM | Advantage Data Dictionary file, where the XXXX is the name that was given to the data dictionary database when it was created. For each .ADD file that exists, a .AM file will exist. If distributing a .ADD file, the corresponding .AM file must also be distributed. |

Note To avoid conflicts that can occur with computers at the distribution site using various collation languages, do not distribute the corresponding .AI file (the Advantage Data Dictionary index file) that exists for each .ADD file. The .AI file will be automatically created at the distribution site when the Advantage Data Dictionary is first accessed. If upgrading an existing Advantage application that used an Advantage Data Dictionary, and replacing an old version of the Advantage Data Dictionary files with a new version of the Advantage Data Dictionary files, you should delete the old .AI file as part of the upgrade.

File Locations

All files should normally be installed in the application directory, the Windows System directory, or somewhere in the client's path. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. Because OLE DB providers' locations are registered, they do not have to be in the path to be found. Starting with version 7.0 of the provider, it is possible to put all redistributable files in same directory in which the ADSOLEDB.DLL is registered even if that directory is not in the path. In versions earlier than 7.0, the Advantage OLE DB Provider would not load the other DLLs if they were not in the path.

Registering the Advantage OLE DB Provider

The Advantage OLE DB Provider DLL, ADSOLEDB.DLL, must be registered on each client computer that will access the Advantage OLE DB Provider. Once registered, the ADSOLEDB.DLL file location must not change unless it is unregistered first and then re-registered. ADSOLEDB.DLL can be registered by calling the exported function, DllRegisterServer(), in ADSOLEDB.DLL or by using the REGSVR32.EXE utility that comes with Windows and passing the provider DLL as the sole parameter:

 

REGSVR32.EXE ADSOLEDB.DLL

Redistributing MDAC

Each release of MDAC includes a matched set of modules. These modules were tested together when Microsoft released them. The interdependencies of the modules are not simple; they must all be distributed as a set. Although it's tempting to try to distribute only the modules for the components that you think your application may need, there is no supported way to do that. Other applications will use MDAC components, and if they aren't part of the same released set, the applications will probably crash. The current version of MDAC includes a redistributable MDAC setup, in the file mdac\_typ.exe. This program is a self-extracting compressed file that installs the run-time components onto a workstation.

With MDAC version 2.1 or greater, the stand-alone and the redistributable MDAC setup programs will not update files on a Windows 2000/2003 system. With the release of Windows 2000/2003, MDAC is part of the operating system and must be updated using operating system service packs.