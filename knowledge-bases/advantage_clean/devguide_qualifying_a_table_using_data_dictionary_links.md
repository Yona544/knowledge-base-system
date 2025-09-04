---
title: Devguide Qualifying A Table Using Data Dictionary Links
slug: devguide_qualifying_a_table_using_data_dictionary_links
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_qualifying_a_table_using_data_dictionary_links.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6fb21f99aadcfa52b2130547d9a31dabe1a8e21a
---

# Devguide Qualifying A Table Using Data Dictionary Links

Qualifying a Table Using Data Dictionary Links

     Qualifying a Table Using Data Dictionary Links

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Qualifying a Table Using Data Dictionary Links  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

In Chapter 4, you learned that you could use data dictionary links to refer to tables in two or more data dictionaries in your SQL statements using a single connection. Data dictionary links have an advantage over data dictionary paths in that you define the location of the data dictionary that the link refers to only once, in the data dictionary link object.

By comparison, when you use data dictionary paths, the path must appear in every SQL statement where tables from two or more dictionaries are used. When you use links, if you need to change the location of a data dictionary, you only have to update the link definition. The existing SQL statements do not need to be touched.

The following SQL statement demonstrates the use of a data dictionary link. Assume that the link named AccountLink has been created to point to the Accounting.ADD data dictionary, and access rights have been granted to this link to the groups that have permission to use the Accounting database. The following SQL statement shows how the AccountsReceivable table is referenced using a data dictionary link:

SELECT Link."Customer Account", Link."Amount Due",  
    Link."Due Date", Cust."Customer Account",   
    Cust."City", Cust."State"  
  FROM  
    AccountLink.AccountsReceivable Link, CUSTOMER Cust  
  WHERE Link."Customer Account" = Cust."Customer Account"

   
NOTE: If your data dictionary link name includes spaces or other special characters, you would need to enclose that link name in double quotation marks or square brackets in your view's SQL statement.  
 

In the next chapter, you will learn how to create stored procedures for use with Advantage.
