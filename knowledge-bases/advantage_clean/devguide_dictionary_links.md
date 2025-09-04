---
title: Devguide Dictionary Links
slug: devguide_dictionary_links
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_dictionary_links.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: fd5db21ef4809ecc935ba5599ba0a8831aff55a7
---

# Devguide Dictionary Links

Dictionary Links

 

     Dictionary Links

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Dictionary Links  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As you have learned, a given ADT table can be bound to only one data dictionary. But what if you need to work with tables in two different data dictionaries?

One solution is to use two different connections, one to each dictionary. This requires that you use two (or more) connection objects, and program your client application to make the connections to the dictionaries.

Fortunately, there is an easier solution: data dictionary links. Data dictionary links, sometimes referred to as link aliases, are objects that you define in one data dictionary that refer to another data dictionary. Importantly, when using a data dictionary link, you only need one connection--the connection to the dictionary that includes one or more data dictionary links. When you use a link to refer to a table in a linked data dictionary, Advantage takes responsibility for using the link to connect to the additional dictionary. Using data dictionary links in SQL statements is discussed in Chapter 6.
