---
title: Devguide Views That Use Views
slug: devguide_views_that_use_views
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_views_that_use_views.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: a3e785d701bad96d071790cc3f4593d3de7cd3d8
---

# Devguide Views That Use Views

Views That Use Views

 

     Views That Use Views

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Views That Use Views  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Earlier in this chapter, you learned how to execute a SQL SELECT statement against the Employee Tab view using the SQL Utility. Since a view itself is defined using a SQL statement, there is no reason why the SQL SELECT statement used in a view cannot query a view.

Views that use views can be employed in a number of interesting ways. Two of these techniques are covered in this section. In the first technique, you will learn how views can be used to modularize operations on your data. In the second, you will see how a view can be used as a temporary table.
