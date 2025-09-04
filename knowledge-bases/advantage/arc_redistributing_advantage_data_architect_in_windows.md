Redistributing Advantage Data Architect




Advantage Database Server 12  

Redistributing Advantage Data Architect

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Redistributing Advantage Data Architect  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Redistributing Advantage Data Architect Advantage Data Architect arc\_Redistributing\_advantage\_data\_architect\_in\_windows Advantage Data Architect > Redistributing Advantage Data Architect / Dear Support Staff, |  |
| Redistributing Advantage Data Architect  Advantage Data Architect |  |  |  |  |

Some or all of the following files will need to be redistributed with the Advantage Data Architect in the Windows environment.

|  |  |
| --- | --- |
| File | Description |
| ARC32.EXE | Advantage Data Architect Executable. Main executable for the program. |
| ACE32.DLL | Advantage Client Engine DLL. Contains the core Advantage client functionality. This file must be located in the same directory as the Advantage Data Architect executable. |
| AXCWS32.DLL | Advantage remote communication library used when accessing data via the Advantage Database Server. This file is not necessary if only using the Advantage Local Server. If the Advantage Database Server is being used, this file must be located in the same directory as the Advantage Data Architect executable. |
| ADSLOC32.DLL | Advantage Local Server DLL. Contains the core Advantage Local Server functionality. This file is not necessary if only using the Advantage Database Server and/or Advantage Internet Server. If the Advantage Local Server is being used, this file must be located in the same directory as the Advantage Data Architect executable. |
| ADSLOCAL.CFG | Advantage Local Server configuration file. This file is only necessary if using the Advantage Local Server and you wish to use Local Server settings other than the default. If installed, place this file in the same directory as ADSLOC32.DLL. |
| EXTEND.CHR | This file is needed for international OEM language support with the Advantage Local Server. This file is only necessary if using a non-USA OEM character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| ANSI.CHR | This file may be needed for ANSI language support with the Advantage Local Server. This file is only necessary if not using a specified ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as ADSLOC32.DLL. |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.htm) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| WIN32ENV.EXE | This file is needed by the Advantage Data Architect to perform environment checking when connecting to the Advantage Database Server. This file must be located in the same directory as the Advantage Data Architect executable. |
| FREEADT.EXE | This file is needed by the Advantage Data Architect to free dictionary bound tables when the Advantage Data Dictionary associated with the table has been deleted. Caution should be used when redistributing this file because it allows any user to remove tables from an Advantage Data Dictionary. This file must be located in the same directory as the Advantage Data Architect executable. |