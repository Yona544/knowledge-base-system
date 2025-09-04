---
title: Devguide Downloading And Installing
slug: devguide_downloading_and_installing
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_downloading_and_installing.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6cc66cabecd50630e5b20ce947a69712e2ee9ee2
---

# Devguide Downloading And Installing

Downloading and Installing

    Downloading and Installing

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Downloading and Installing  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The two-user developer edition of Advantage, the individual Advantage clients, and the sample database and associated files referred to in this book are available online for download. To download these files, point your Web browser to the following URL:

http://www.AdvantageDatabase.com/book

At a minimum, you will need to download ADS and the Advantage client that corresponds to the development environment that you use to build your database applications. To follow along with the book examples, you will need to download the sample database and associated files.

Once you have downloaded the appropriate files, you will want to install them. For ADS, the file you download is a self-extracting file that will extract the program installation files. Once you have extracted the installation files, run setup.exe (setup.pl for Linux).

For the Advantage Data Architect and any of the Advantage clients, installation is simply a matter of running the downloaded executable and responding to a few options from the installation program's dialog boxes. The installation of the database and associated files for the book examples is discussed in the next section.

While most installations are quite simple, there is one point to keep in mind: Servers, and some of the utilities, require you to specify the collation sequence or OEM character set that you want to use. It is critical that the server and all clients that will access it use the same collation sequence or OEM character set. Mixing collation sequences or OEM character sets can result in incompatible clients.

At the end of each installation, you are given a chance to view the README file associated with that installation. We recommend that you read this README file. If you want to read it at a later time, you can find the associated README file in the directory in which the server, driver, or utility is installed.

Normally, we suggest that you install the server first. However, if you already have a licensed version of ADS version 8.1 or later, there is no need to install the server.

Note that when you install the Advantage Data Architect or one of the Advantage clients, those installation programs also install the Advantage Local Server (only the Advantage JDBC Driver does not install ALS, as this driver requires ADS). As discussed in Chapter 1, ALS is a five-user, local engine version of ADSsporting the same API as ADS, making it a great platform for developing your applications. However, some features available in ADS, such as online backup, replication, transactions, and Java connectivity, are unavailable when you are using ALS.
