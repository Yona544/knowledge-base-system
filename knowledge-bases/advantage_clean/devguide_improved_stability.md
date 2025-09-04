---
title: Devguide Improved Stability
slug: devguide_improved_stability
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_improved_stability.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2133dc0e883949a148c597440b467ac3b6c4487b
---

# Devguide Improved Stability

Improved Stability

     Improved Stability

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Improved Stability  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The final drawback to file-server-based systems is stability. Because there is no centralized control over locking and transactions, the failure of a single workstation can result in corruption to parts of the database. Developers familiar with Clipper-based local table applications occasionally encounter errors such as corrupt or out-of-date indexes.

The issue of stability disappears almost completely when the Advantage Database Server is involved. In these applications, ADS itself is managing the data, and failure of an individual workstation or the network simply cannot harm the data.
