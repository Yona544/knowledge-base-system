---
title: Master Full Text Search Record Visibility
slug: master_full_text_search_record_visibility
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_record_visibility.htm
source: Advantage CHM
tags:
  - master
checksum: 56f9047a0812edde07e6b8558894536312d1cc83
---

# Master Full Text Search Record Visibility

Full Text Search Record Visibility

Full Text Search Record Visibility

Advantage Concepts

| Full Text Search Record Visibility  Advantage Concepts |  |  |  |  |

The CONTAINS() function is only evaluated at the server; it is never evaluated at the client. This primarily affects the Advantage TDataSet Descendant, which normally checks visibility of records at the client to keep result sets completely accurate. For example, if a TAdsTable instance has a filter of the form "lastname = Smith" and you edit a lastname value and change it from "Smith" to "Jones", that record will be removed from the result set because it no longer passes the filter condition. The most obvious case of this is when you edit the record in a grid; it will be removed from the grid after the edit.

Because the CONTAINS() function is only evaluated at the server, however, the record visibility will not be checked for that function. So, for example, if a filter (or SQL WHERE clause) has the expression "CONTAINS( lastname, Smith )" and you change "Smith" to "Jones" in the grid, that record will still be visible until you re-execute the filter or query.
