---
title: Ace Distributing An Advantage Client Engine Enabled Application
slug: ace_distributing_an_advantage_client_engine_enabled_application
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_distributing_an_advantage_client_engine_enabled_application.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7f816a265fd8f1e2ebc5ffba762fba53761d4b91
---

# Ace Distributing An Advantage Client Engine Enabled Application

Distributing an Advantage Client Engine-Enabled Application

Distributing/Deploying an Advantage Client Engine-Enabled Application

Advantage Client Engine

| Distributing/Deploying an Advantage Client Engine-Enabled Application  Advantage Client Engine |  |  |  |  |

Required Files

| File Name | Description |
| ads.ini | File used to store Advantage initialization information. Among the information available to be stored in this file is the Advantage server type setting and the database engine type setting. This file only needs to be distributed if your application is making use of initialization information within it. See [ads.ini File Support](master_ads_ini_file_support.md) for more information. |
| Windows: ace32.dll or ace64.dll  Linux: libace.so | Advantage Client Engine. Contains the core Advantage Windows and Linux client client functionality. This file must be distributed with your application. |
| Windows: axcws32.dll or axcws64.dll | Advantage remote communication library used when accessing data via the Advantage Database Server. This file does not need to be distributed if using the Advantage Local Server only. No equivalent file exists for Linux as this functionality is built into the libace.so file. |
| Windows: adsloc32.dll or adsloc64.dll  Linux: libadsloc.so | [Advantage Local Server](master_advantage_local_server.md) library. Contains the core local server functionality. This file does not need to be distributed if using the Advantage Database Server only. |
| adslocal.cfg | [Advantage Local Server configuration](master_advantage_local_server_configuration.md) file. This file only needs to be distributed if using the Advantage Local Server and you wish to use Local Server settings other than the default. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| extend.chr | This file is needed for international OEM language support with the Advantage Local Server. This file only needs to be distributed if using a non-USA OEM character set with the Advantage Local Server. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| ansi.chr | This file can be used for ANSI language support with the Advantage Local Server. This file only needs to be distributed if using a specific ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.md) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| xxxx.add | Main Advantage Data Dictionary file, where the XXXX is the name that was given to the Advantage Data Dictionary database when it was created. If your application uses database tables and Advantage Data Dictionary functionality, this file must be distributed with your application. If the application connects to more than one Advantage Data Dictionary, each applicable .ADD file must be distributed with the application. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information about Advantage Data Dictionary functionality. |
| xxxx.am | Advantage Data Dictionary file, where the XXXX is the name that was given to the Advantage Data Dictionary database when it was created. For each .ADD file that exists, an .AM file will exist. If distributing an .ADD file, the corresponding .AM file must also be distributed. |

Note To avoid conflicts that can occur with computers at the distribution site using various collation languages, do not distribute the corresponding .AI file (the Advantage Data Dictionary index file) that exists for each .ADD file. The .AI file will be automatically created at the distribution site when the Advantage Data Dictionary is first accessed. If upgrading an existing Advantage application that used an Advantage Data Dictionary, and replacing an old version of the Advantage Data Dictionary files with a new version of the Advantage Data Dictionary files, you should delete the old .AI file as part of the upgrade.

File Locations

Windows

The files must be in the application directory, the Windows directory, the Windows System directory, or the client's path. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. If ADS.INI is located in the Windows directory, the Windows System directory, or a directory in the client's path, aliases will be shared with other Advantage applications. If located in the application directory, aliases will only be visible to this specific application.

Linux

The shared objects must be in the /usr/lib directory, the /lib directory, or a path specified in the LD\_LIBRARY\_PATH environment variable. See [Linux Shared Objects](master_linux_shared_objects.md) for more details. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. If the ads.ini file is located in the /etc directory, aliases will be shared with other Advantage applications. If located in the application directory, aliases will only be visible to this specific application.

Building an Installation Program

When building an installation program for an Advantage Client Engine application, simply have the installation program place the desired Advantage files in the application directory or desired location as described above. There are no registry entries or modifications required.

Configuration, ads.ini File

ads.ini is a configuration file that stores the settings used to determine what server types Advantage applications should use, among other things. For more information, see [ads.ini File Support](master_ads_ini_file_support.md).

Windows

ads.ini is a configuration file that can be located in the application directory, or the Windows directory.

Linux

ads.ini is a configuration file that can be located in the application directory, the /etc directory, the current users home directory (in this case the file should be named ".ads.ini") or in the directory pointed to by an environment variable named ADSPATH.
