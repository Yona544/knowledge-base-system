Distributing Advantage ODBC Applications




Advantage Database Server 12  

Distributing Advantage ODBC Applications

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Distributing Advantage ODBC Applications  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - Distributing Advantage ODBC Applications Advantage ODBC Driver odbc\_Distributing\_advantage\_odbc\_applications Advantage ODBC Driver > Installation and Distribution > Distributing Advantage ODBC Applications / Dear Support Staff, |  |
| Distributing Advantage ODBC Applications  Advantage ODBC Driver |  |  |  |  |

Most off-the-shelf installation software packages have ODBC application installation functionality. Included among this functionality is registration of the ODBC driver and data source setup. In addition to using this kind of installation software to distribute your application that uses the Advantage ODBC Driver, some or all of the files mentioned below should be distributed as well.

Files to Distribute

|  |  |
| --- | --- |
| File Name | Description |
| ads.ini | File used to store Advantage initialization information. Among the information available to be stored in this file is the Advantage server type setting and the database engine type setting. This file only needs to be distributed if your application is making use of initialization information within it. See [ads.ini File Support](master_ads_ini_file_support.htm) for more information. |
| Windows: ace32.dll or ace64.dll  Linux: libace.so | Advantage Client Engine library. Contains the core Advantage Windows client and Linux client functionality. This file must be distributed with your application. |
| Windows: axcws32.dll or axcws64.dll | Advantage remote communication library used when accessing data via the Advantage Database Server. This file does not need to be distributed if using the Advantage Local Server only. No equivalent file exists for Linux as this functionality is built into the libace.so file. |
| Windows: adsloc32.dll or adsloc64.dll  Linux: libadsloc.so | [Advantage Local Server](master_advantage_local_server.htm) library Contains the core local server functionality. This file does not need to be distributed if using the Advantage Database Server only. |
| adslocal.cfg | [Advantage Local Server configuration](master_advantage_local_server_configuration.htm) file. This file only needs to be distributed if using the Advantage Local Server and you wish to use Local Server settings other than the default. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| extend.chr | This file is needed for international OEM language support with the Advantage Local Server. This file only needs to be distributed if using a non-USA OEM character set with the Advantage Local Server. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| ansi.chr | This file can be used for ANSI language support with the Advantage Local Server. This file only needs to be distributed if using a specific ANSI character set with the Advantage Local Server. If installed, place this file in the same directory as the Advantage Local Server library (adsloc32.dll or libadsloc.so). |
| adscollate.adt, adscollate.adm | These files contain [collations](master_collation_support.htm) that can be dynamically loaded at run time. These files only need to be distributed if you are using one of those collations with Advantage Local Server. |
| Windows: adsodbc.dll  Linux: libadsodbc.so | Advantage ODBC Driver. Contains core Advantage ODBC driver functionality. This file must be distributed with your application. |
| Windows: adsset.dll | Advantage ODBC Driver Administration DLL. This file must be distributed with your application in order to configure the Advantage ODBC Driver via the GUI setup utility. No equivalent file exists for Linux. |
| XXXX.add | Main Advantage Data Dictionary file, where the XXXX is the name that was given to the Data Dictionary database when it was created. If your application uses database tables and Advantage Data Dictionary functionality, this file must be distributed with your application. If the application connects to more than one Advantage Data Dictionary, each applicable .add file must be distributed with the application. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information about Advantage Data Dictionary functionality. |
| XXXX.am | Advantage Data Dictionary file, where the xxxx is the name that was given to the Data Dictionary database when it was created. For each .add file that exists, a .am file will exist. If distributing a .add file, the corresponding .am file must also be distributed. |

Note To avoid conflicts that can occur with computers at the distribution site using various collation languages, do not distribute the corresponding .AI file (the Advantage Data Dictionary index file) that exists for each .ADD file. The .AI file will be automatically created at the distribution site when the Advantage Data Dictionary is first accessed. If upgrading an existing Advantage application that used an Advantage Data Dictionary, and replacing an old version of the Advantage Data Dictionary files with a new version of the Advantage Data Dictionary files, you should delete the old .AI file as part of the upgrade.

File Locations

Windows

The files must be in the application directory, the Windows directory, the Windows System directory, or the client's path. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. If ADS.INI is located in the Windows directory, the Windows System directory, or a directory in the client's path, aliases will be shared with other Advantage applications. If located in the application directory, aliases will only be visible to this specific application.

Linux

The shared objects must be in the /usr/lib directory, the /lib directory, or a path specified in the LD\_LIBRARY\_PATH environment variable. See [Linux Shared Objects](master_linux_shared_objects.htm) for more details. The recommended location is in the application directory. This helps to avoid version conflict in the case of multiple Advantage applications on a workstation. If the ads.ini file is located in the /etc directory, aliases will be shared with other Advantage applications. If located in the application directory, aliases will only be visible to this specific application.