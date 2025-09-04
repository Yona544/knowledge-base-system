---
title: Devguide Navigational Actions With Advantage And Ado Net
slug: devguide_navigational_actions_with_advantage_and_ado_net
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_navigational_actions_with_advantage_and_ado_net.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 89742bd1d2aedb922fcd98953eabc9b0dcc8059b
---

# Devguide Navigational Actions With Advantage And Ado Net

Navigational Actions with Advantage and ADO.NET

     Navigational Actions with Advantage and ADO.NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Navigational Actions with Advantage and ADO.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Most of the navigational features that you can access with other data access mechanisms, such as ADO and TDataSet, are implemented in the ADO.NET DataSet, DataTable, or DataView classes. For example, indexing, sorting, filtering, and seeking are all operations that are performed on a DataTable's cached records using a DataView. In other words, these operations do not involve Advantage, other than using Advantage as the original source of the data that is manipulated in memory.

There is, in fact, only one ADO.NET navigational operation that involves Advantage-scanning. Specifically, using an AdsDataReader (or an AdsExtendedReader, which as you learned earlier, also supports filters, ranges, and seeks), you can perform a record-by-record navigation of data. This operation is demonstrated in the following section.
