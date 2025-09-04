---
title: Devguide Navigational Actions With Ads And Java
slug: devguide_navigational_actions_with_ads_and_java
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_navigational_actions_with_ads_and_java.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: e02e0433d64a4a82ec4e99e4ba1b62259afe23e2
---

# Devguide Navigational Actions With Ads And Java

Navigational Actions with ADS and Java

     Navigational Actions with ADS and Java

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Navigational Actions with ADS and Java  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Unlike Delphi and ADO-based Advantage applications, which support a wide range of navigational operations, JDBC supports only simple navigation. Specifically, the ResultSet class permits you to navigate forward through the records of the result set, and if the cursor is bidirectional, you can move forward and backward using methods with names such as first, next, last, and previous. The use of simple forward navigation is demonstrated in the following section.

   
NOTE: Some classes in Borland's DataExpress in JBuilder support additional navigational capabilities, such as filtering. These classes are not, however, native to JDBC.
