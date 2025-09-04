---
title: Devguide Improved Performance
slug: devguide_improved_performance
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_improved_performance.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 4c9a35718cff5c28b7af618584d016f686f39b54
---

# Devguide Improved Performance

Improved Performance

     Improved Performance

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Improved Performance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Performance is another area where file-server-based systems suffer. Specifically, the individual workstations are responsible for all processing. In other words, all user interface interaction as well as database manipulation is performed on each client workstation in a file-server-based system. The file server itself performs no processing, other than transferring files from the server to the workstation.

By comparison, client/server systems perform nearly all data manipulation on the database server, efficiently distributing the processing across multiple machines. When using ADS, your workstations are primarily responsible for the user interface, while the remote server takes care of data manipulation.

Most database applications are multiuser, and it is in these situations where the performance advantages of the client/server architecture are most profound. However, note that in stand-alone applications, where the data is used by only one workstation, ALS-based applications might actually outperform client/server applications, performance-wise. In short, if the data is used by only one workstation, and the data is stored on that workstation, ALS may offer faster performance (but with less functionality and poorer stability). For these applications, ADS provides you with a seamless, high-performance migration path when these applications are converted to multiuser use.
