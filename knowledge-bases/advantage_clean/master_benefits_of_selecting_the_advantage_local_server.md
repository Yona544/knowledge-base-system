---
title: Master Benefits Of Selecting The Advantage Local Server
slug: master_benefits_of_selecting_the_advantage_local_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_benefits_of_selecting_the_advantage_local_server.htm
source: Advantage CHM
tags:
  - master
checksum: 30570f049baa5243230a66af6d8a0103dae46104
---

# Master Benefits Of Selecting The Advantage Local Server

Benefits of Selecting the Advantage Local Server

Benefits of Selecting the Advantage Local Server

Advantage Concepts

| Benefits of Selecting the Advantage Local Server  Advantage Concepts |  |  |  |  |

Access to Local and Remote Data

The Advantage Local Server can access data files located on a local drive or on a network drive. The computer where the data files are located can be running nearly any PC-based operation system: Windows 95, Windows 98, Windows ME, Windows, or Linux.

Ease of Distribution

The Advantage Local Server ships with all Advantage clients at no additional cost. In order to distribute your Advantage application that uses the Advantage Local Server, you only need to ship and install a few additional files; the Advantage Local Server (ADSLOC32.DLL in Windows, or libadsloc.so in Linux), and the Advantage Local Server configuration file (ADSLOCAL.CFG). If your application uses non-USA OEM or ANSI collation sequences, the files EXTEND.CHR and ANSI.CHR must also be shipped and installed. If [dynamic collations](master_collation_support.md) are used, the files adscollate.adt and adscollate.adm must also be shipped and installed.

Optimum Single-User Performance

In certain single user Windows environments, it is possible that application performance will be much better using the Advantage Local Server than with the Advantage Database Server. For this to be true, the following conditions must all be present:

- An Advantage application is running on a Windows client.

- The data files are located on a Windows Server or Workstation.

- No other user on the network has those data files open.

A special case exists when a Windows client is running against a Windows NT/2000/2003 server. If files are opened by a single user, the data will be cached on the client. Thus, the Advantage Local Server will cache all data on the client. Advantage client/server drivers that access data via the Advantage Database Server never cache data on the client. Data updates will always be sent to the server and data that is read will always be retrieved from the server. Thus, Advantage Local Server applications in this scenario may perform much better than client/server applications that use the Advantage Database Server because they will never have to re-read data from the file server.

Low Cost

The Advantage Local Server can be distributed royalty-free with your application. You can ship your Advantage application to as many sites as desired with no further expense, as far as Advantage is concerned, when using the Advantage Local Server.
