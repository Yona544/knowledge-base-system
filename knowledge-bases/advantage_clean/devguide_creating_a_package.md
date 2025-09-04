---
title: Devguide Creating A Package
slug: devguide_creating_a_package
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_a_package.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9367e63acf7c0f2983dcaddb5f2f76a77b0f2ed7
---

# Devguide Creating A Package

Creating a Package

     Creating a Package

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating a Package  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a package by right-clicking the FUNCTION node in your data dictionary connection and selecting Create Package. You then use the Package dialog box to define the package name.

Use the following steps to create a package called Math:

1.        From your active and connected DemoDictionary connection, right-click the FUNCTION node and select Create Package. The Advantage Data Architect responds by displaying the Package dialog box shown in Figure 13-1.

Figure 13-1: The Package dialog box

2.        At Name, enter Math.

| 3. | Click OK to close the Package dialog box and create your new package. |

   
NOTE: In order to create a package, you must be connected to the data dictionary either on the ADSSYS administrative account or from a user who has create package rights.
