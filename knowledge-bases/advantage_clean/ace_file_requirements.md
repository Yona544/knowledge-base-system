---
title: Ace File Requirements
slug: ace_file_requirements
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_file_requirements.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 98959b30b5fa0de14ab90ce03478ab2c9943f8c9
---

# Ace File Requirements

File Requirements

File Requirements

Advantage Client Engine

| File Requirements  Advantage Client Engine |  |  |  |  |

Windows

Verify the following DLL is in your system path on the PCs that will be running an Advantage Client Engine application.

ace32.dll or ace64.dll

The following file is only necessary when using the Advantage Client Engine with the Advantage Database Server.

axcws32.dll or axcws32.dll

The following files are only necessary when using the Advantage Client Engine with the Advantage Local Server.

adsloc32.dll or adsloc64.dll

adslocal.cfg

Linux

Verify the following shared objects are in your /usr/lib directory or in your LD\_LIBRARY\_PATH on the PCs that will be running an Advantage Client Engine application.

libace.so.X.YY.Z (where X,Y, and Z are version numbers)

The following files are only necessary when using the Advantage Client Engine with the Advantage Local Server.

libadsloc.so.X.YY.Z

adslocal.cfg

Note The Advantage communication library is built in to the Advantage Client Engine in Linux, so there is no separate communication library.

Communication Libraries

The Advantage communication library has been designed to auto-sense for IP or IPX communication.

IP communication is supported with the Advantage Database Server for Windows and the Advantage Database Server for Linux.

For updates or additions to the shipping files, please see the FILES.TXT file in the installation directory. The FILES.TXT file also lists the files that you should distribute with your application.
