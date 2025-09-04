---
title: Vo Distributing Advantage Ca Visual Objects Applications
slug: vo_distributing_advantage_ca_visual_objects_applications
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_distributing_advantage_ca_visual_objects_applications.htm
source: Advantage CHM
tags:
  - vo
checksum: 5c27e55920318531b24f537194541d936cfe065b
---

# Vo Distributing Advantage Ca Visual Objects Applications

Distributing Advantage Visual Objects and Vulcan.NET Applications

Distributing Advantage Visual Objects and Vulcan.NET Applications

Advantage Visual Objects and Vulcan.NET RDD

| Distributing Advantage Visual Objects and Vulcan.NET Applications  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Required Files for both Visual Objects and Vulcan.NET Applications

| File Name | Description |
| ads.ini | File used to store Advantage initialization information. Among the information available to be stored in this file, is alias information, the Advantage server type setting, and the database engine type setting. This file only needs to be distributed if your application is using aliases or using any other initialization information within it. See [ads.ini File Support](master_ads_ini_file_support.md) for more information. |
| ace32.dll | Advantage Client Engine DLL. Contains the core Advantage Windows client functionality. This file must be distributed with your application. |
| axcws32.dll | Advantage remote communication library used when accessing data via the Advantage Database Server. This file does not need to be distributed if using the Advantage Local Server only. |
| adsloc32.dll | [Advantage Local Server](master_advantage_local_server.md) DLL. Contains the core local server functionality. This file does not need to be distributed if using the Advantage Database Server only. |
| adslocal.cfg | [Advantage Local Server Configuration](master_advantage_local_server_configuration.md) file. This file only needs to be distributed if using the [Advantage Local Server](master_advantage_local_server.md) and you want to use Local Server settings other than the default. If installed, place this file in the same directory as adsloc32.dll. |
| extend.chr | This file is needed for international OEM language support with the Advantage Local Server. This file only needs to be distributed if using a non-USA OEM character set with the Advantage Local Server. |
| ansi.chr | This file can be used for ANSI language support with the Advantage Local Server. This file only needs to be distributed if using a specific ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as adsloc32.dll. |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.md) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| XXXX.add | Main [Advantage Data Dictionary](master_advantage_data_dictionary.md) file, where the XXXX is the name that was given to the Advantage Data Dictionary database when it was created. If your application uses database tables and Advantage Data Dictionary functionality, this file must be distributed with your application. If the application connects to more than one Advantage Data Dictionary, each applicable .add file must be distributed with the application. See Advantage Data Dictionary for more information about Advantage Data Dictionary functionality. |
| XXXX.am | Advantage Data Dictionary file, where the XXXX is the name that was given to the Advantage Data Dictionary database when it was created. For each .add file that exists, an .am file will exist. If distributing an .add file, the corresponding .am file must also be distributed. |

Required Files for Visual Objects Applications

| axdbfntx.rdd | Advantage DBF/NTX/DBT RDD. Contains core Advantage RDD functionality. This must be distributed with your application if using the Clipper data format. |
| axdbfcdx.rdd | Advantage DBF/CDX/FPT RDD. Contains core Advantage RDD functionality. This must be distributed with your application if using the FoxPro data format. |
| axdbfvfp.rdd | Advantage DBF/CDX/FPT Visual FoxPro RDD. Contains core Advantage RDD functionality. This must be distributed with your application if using the Advantage RDD with the Visual FoxPro data format. |
| adsadt.rdd | Advantage ADT/ADI/ADM RDD. Contains core Advantage RDD functionality. This must be distributed with your application if using the Advantage Proprietary data format. |
| axsqladt.rdd | Advantage ADT/ADI/ADM SQL RDD. Contains core Advantage SQL RDD functionality. This must be distributed with your application if using the Advantage SQL RDD with the Advantage Proprietary data format. |
| Axsqlvfp.rdd | Advantage DBF/CDX/FPT Visual FoxPro SQL RDD. Contains core Advantage SQL RDD functionality. This must be distributed with your application if using the Advantage SQL RDD with the FoxPro data format. |
| axsqlcdx.rdd | Advantage DBF/CDX/FPT SQL RDD. Contains core Advantage SQL RDD functionality. This must be distributed with your application if using the Advantage SQL RDD with the FoxPro data format. |
| axsqlntx.rdd | Advantage DBF/NTX/DBT SQL RDD. Contains core Advantage SQL RDD functionality. This must be distributed with your application if using the Advantage SQL RDD with the CA-Clipper data format. |

Required Files for Vulcan.NET Applications

| AdvantageRDD.dll | Advantage RDDs for Vulcan.NET.  This .NET assembly contains all the Advantage RDDs for Vulcan.NET.  It also contains the Advantage Client Engine API prototypes and constants plus the DBFAXS library functions and constants.  This must be distributed with your Vulcan.NET application. |

Note To avoid conflicts that can occur with computers at the distribution site using various collation languages, do not distribute the corresponding .AI file (the Advantage Data Dictionary index file) that exists for each .ADD file. The .AI file will be automatically created at the distribution site when the Advantage Data Dictionary is first accessed. If upgrading an existing Advantage application that used an Advantage Data Dictionary, and replacing an old version of the Advantage Data Dictionary files with a new version of the Advantage Data Dictionary files, you should delete the old .AI file as part of the upgrade.

File Locations

The files must be in the application directory, the Windows directory, the Windows System directory, or the client's path. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. If ads.ini is located in the Windows directory, the Windows System directory, or a directory in the client's path, aliases will be shared with other Advantage applications. If located in the application directory, aliases will only be visible to this specific application.

Building an Installation Program

When building an installation program for an Advantage Visual Objects or Vulcan.NET application, simply have the installation program place the desired Advantage files in the application directory or desired location as described above. There are no registry entries or modifications required.

Configuration, ads.ini File

ads.ini is a configuration file that can be located in the application directory, or the Windows directory. It stores the settings used to define database aliases used by Advantage and determines what server types Advantage applications should use. For more information, see [ads.ini File Support](master_ads_ini_file_support.md).
