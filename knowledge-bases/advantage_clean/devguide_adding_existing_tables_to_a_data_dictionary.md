---
title: Devguide Adding Existing Tables To A Data Dictionary
slug: devguide_adding_existing_tables_to_a_data_dictionary
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_adding_existing_tables_to_a_data_dictionary.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 76baedf51f13a33e7dd38221ec86a313494c45e1
---

# Devguide Adding Existing Tables To A Data Dictionary

Adding Existing Tables to a Data Dictionary

     Adding Existing Tables to a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Adding Existing Tables to a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Adding existing tables to a data dictionary is easy. The following steps show you how:

With the DemoDictionary connection open in the Connection Repository, right-click the TABLES node and select Add Existing Table(s). The Open dialog box is displayed, pointing to the directory in which the data dictionary was created.

Because you created the data dictionary in the same directory into which you previously downloaded the sample database tables as described in Appendix A, free tables are displayed in the Open dialog box. Select the CUSTOMER.ADT and the EMPLOYEE.ADT tables. To do this, hold down the Ctrl key and click on CUSTOMER.ADT and on EMPLOYEE.ADT. With both tables listed in the File name field, click the Open button. The two newly added tables should now appear as nodes beneath the TABLES node, as shown in Figure 4-4 (click the + next to the Tables node if this node is not already expanded).

Figure 4-4: Two free tables have now been bound to the dictionary
