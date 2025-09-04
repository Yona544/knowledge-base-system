---
title: Devguide The Advantage Configuration Utility
slug: devguide_the_advantage_configuration_utility
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_advantage_configuration_utility.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 03bc4aa45d3681293c77d19db6471f6de22c26fe
---

# Devguide The Advantage Configuration Utility

The Advantage Configuration Utility

     The Advantage Configuration Utility

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The Advantage Configuration Utility  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When ADS is installed on your server on Windows NT/2000/2003, the Advantage Configuration Utility is also installed. This utility provides you with several important capabilities. It permits you to view statistics about your server's operation, and it also permits you to manually set many of the server's configurable properties. Because the Windows NT/2000/2003 server is the most popular server version, the Advantage Configuration Utility is described in this section.

The Linux installation of ADS does not include the Advantage Configuration Utility. Linux installations are configured from command-line parameters and/or configuration files. For these installations, refer to the documentation for information on configuring Advantage.

   
CODE DOWNLOAD: The Advantage documentation is located on this book's code download, as described in Appendix A. You can find more in-depth resources on Advantage at the Advantage Developer Zone Web site at http://Devzone.AdvantageDatabase.com.  
 

The Advantage Data Architect includes an Advantage Database Server Management Utility. The Management Utility contains information similar to the Advantage Configuration Utility described in this section. See the Advantage documentation for additional information on the Advantage Database Server Management Utility.

   
NOTE: The purpose of the following descriptions is to show you where you can get information about the server. This section is not designed to provide a detailed description of how these settings are used. For that information, please refer to the Advantage documentation.  
 

To use the Advantage Configuration Utility Windows, select the Start button, and then select Programs | Advantage Database Server | ADS Configuration Utility. The Advantage Configuration Utility shown in Figure 1-1 is displayed. There are three main tabs: Database Info, Installation Info, and Configuration Utility. These pages are described in the following sections.

Figure 1-1: The Advantage Configuration Utility

Database Info Page

The Database Info page, shown in Figure 1-1, contains basic statistics about attached users, connections, work areas, as well as open tables and indexes. The Current column on the Database Info page displays current usage statistics, while the Max Used column shows the highest value for each statistic since the server was started.

This information can help you determine whether you need to make adjustments to any of the configurable parameters of the server. For example, if you find that the maximum number of configured connections was used, and that some connections were rejected, you can use the Configuration Utility pages to increase the number of available connections. The Configuration Utility pages are described later in this section.

The Installation Info Page

The Installation Info page, shown in Figure 1-2, contains information about the installed server, including the licensed number of users, your serial number, and the server version you are running.

Figure 1-2: The Installation Info page of the Advantage Configuration Utility

The values on the Installation Info page are not configurable. If you need to change these values, you can either reinstall your server or use a special utility that ships with Advantage. This utility, called AdsStamp.exe, permits you to install a new license key and to change your character sets and a few other settings. AdsStamp is described briefly later in this chapter.

   
NOTE: Many of the settings that you can control from the Advantage Configuration Utility can also be adjusted using command-line parameters and/or configuration files. For information about these options, see the Advantage documentation.  
 

The remaining pages of the Advantage Configuration Utility are used to set the parameters used by the server. You display these additional pages by clicking on the Configuration Utility tab of the Advantage Configuration Utility.

In most cases, once you have adjusted the settings of the Advantage Database Server, you will not need to make further changes. However, after the server has been running for a while, you should inspect the Database Info page of the Advantage Configuration Utility to ensure that your initial settings are sufficient. If you find that you have to make adjustments to one or more of the settings found on the Configuration pages of the Advantage Configuration Utility, you will need to stop and then restart your server before your changes take effect.

   
NOTE: To view default values of configuration parameters, see the topic "Advantage Database Server Configuration Parameter Settings List" in the Advantage help.  
 

The Database Settings Page

Use the Database Settings page, shown in Figure 1-3, to adjust the maximum permitted connections, work areas, and simultaneously opened tables and indexes. Note that the maximum number of connections is not the same as the maximum number of users. Each machine that is currently accessing the server counts as a user. Each user can have multiple connections. You should set Number of Connections to the maximum user count times the maximum number of connections each user requires.

The Database Info pages, as well as the remaining pages under the Configuration Utility tab, include a Restore Defaults button. This button, when clicked, restores all settings under the Configuration Utility tag. You can also find a list of the default configuration values by searching the Advantage help for "configuration parameters."

Figure 1-3: The Database Settings page of the Advantage Configuration Utility

The File Locations Page

Use the File Locations page, shown in Figure 1-4, to change the location of the error and transaction log files, as well as the semaphore connection file path.

Figure 1-4: The File Locations page of the Advantage Configuration Utility

The error file, ads\_err.dbf or ads\_err.adt, is updated when ADS encounters a problem at runtime. This log file is a free table that you can open using the Advantage Data Architect, or using any other utility capable of viewing ADT or DBF files. (This file was a DBF in Advantage 7.x, but defaults to an ADT table in Advantage 8.)

The assert log file, assert.log, is a log of unexpected conditions encountered by the server. The Advantage technical support team sometimes uses this file to help identify the source of unusual problems that you encounter.

Transaction log files are files that the ADS transaction processing system (TPS) creates while updates to a database are being performed within the context of a transaction. These important files permit ADS to either commit or roll back changes if there is a failure somewhere in the system before the transaction is complete. These files, which have the .tps extension, are deleted by ADS when the associated transaction is complete.

Unlike the ads\_err table, TPS files are intended for the internal use of ADS. You should not manually delete or attempt to view these files.

A semaphore connection file is a file that might be created by the server for each user connection. The 16-bit versions of Advantage use this file internally to manage each user's connection to the server. The 32-bit versions of Advantage do not create or use a semaphore file.

The Communications Page

If you want to permit applications to connect to your server over the Internet, use the Communications page to define how this communication will be permitted. The Communications page of the Advantage Configuration Utility is shown in Figure 1-5.

Figure 1-5: The Communications page of the Advantage Configuration Utility

LAN Port permits you to set the UDP and TCP ports on which the server will listen for client connections. (IP, UDP, and TCP stand for Internet protocol, user datagram protocol, and transmission control protocol, respectively.) If LAN Port is set to the default 0, it will try to use UDP and TCP port 6262. If you want to use a port other than 6262, set LAN Port to a port that is available for both UDP and TCP.

If you want to connect to ADS over the Internet, you set Internet Port to the UDP and/or TCP port that applications will use to connect to your server. This port must also be opened in any firewalls separating the server and the applications that need to access it. Leaving Internet Port set to the default of 0 disables Internet access.

You also use this page to configure whether to use a semaphore file, the client connection timeout, and level of data compression.

   
NOTE: To enable Internet access to the Advantage Database Server, you must also configure the data dictionary used to access the data to accept Internet connections. Depending on the data access mechanism or the specifics of your connection, each client machine may also require an ADS configuration file that contains additional information about the connection. For information on setting up client applications to connect over the Internet, see the topic "Advantage Internet Server" in the Advantage documentation.  
 

The Misc. Settings Page

Use the Misc. Settings page of the Advantage Configuration Utility, shown in Figure 1-6, to set the maximum number of worker threads as well as the maximum number of records to save in the error log.

You also use this page to suppress message boxes, which is useful when you want to stop and start the server without dialog boxes being displayed (particularly useful when you need to manage a cluster of servers). For security purposes, you can also prohibit connections that do not use data dictionaries.

Figure 1-6: The Misc. Settings page of the Advantage Configuration Utility

The Language Page

Use the Language page of the Advantage Configuration Utility, shown in Figure 1-7, to change the ANSI character set (and the OEM character set when using international versions of ADS).

Figure 1-7: The Language page of the Advantage Configuration Utility
