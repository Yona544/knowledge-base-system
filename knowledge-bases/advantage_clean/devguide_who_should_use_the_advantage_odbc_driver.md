---
title: Devguide Who Should Use The Advantage Odbc Driver
slug: devguide_who_should_use_the_advantage_odbc_driver
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_who_should_use_the_advantage_odbc_driver.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 4f90089b4e4421791e1e0da60828aeed5061a88a
---

# Devguide Who Should Use The Advantage Odbc Driver

Who Should Use the Advantage ODBC Driver

     Who Should Use the Advantage ODBC Driver

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Who Should Use the Advantage ODBC Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are two groups of users who should use the Advantage ODBC Driver. The first group consists of those developers who are using development environments for which there are no alternative drivers. For example, if you are using a proprietary development environment that does not support the ACE (Advantage Client Engine) API, Java, .NET, ADO, or VCL, the Advantage ODBC Driver is your fallback solution.

For those developers for whom there is an alternative to ODBC, ODBC is usually a poor choice for connecting to Advantage. This is because the alternative solutions offer more options than does ODBC. In short, ODBC is the lowest common denominator for data access. All other data access solutions, including the two others covered in this chapter, provide a more extensive API than that supplied by ODBC alone.

The second group of developers who will use ODBC to access Advantage are those that use the Advantage PHP Extension or the Advantage DBI Driver. Both of these drivers, which are used by Web developers through the PHP and Perl languages, respectively, connect to Advantage through the ODBC driver. However, these drivers supply additional support beyond that provided by plain ODBC.
