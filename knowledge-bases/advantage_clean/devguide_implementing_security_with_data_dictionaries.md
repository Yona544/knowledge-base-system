---
title: Devguide Implementing Security With Data Dictionaries
slug: devguide_implementing_security_with_data_dictionaries
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_implementing_security_with_data_dictionaries.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 3d534d7a2ddd300aed18583e814d81d447910cc9
---

# Devguide Implementing Security With Data Dictionaries

Implementing Security with Data Dictionaries

 

     Implementing Security with Data Dictionaries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Implementing Security with Data Dictionaries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While encrypting your database tables prevents someone from viewing the data in your table files directly, it does nothing to prevent those tables from being accessed by client applications designed to work with a data dictionary. If you want to control who can access your tables, you have to implement security for your data dictionary.

You can take a number of specific steps to ensure that your data is accessed only by authorized users. These include requiring users to log in prior to providing them with access to your database tables, as well as setting up the user names and passwords that users use to log in. These topics are covered in the following sections.
