---
title: Devguide Scanning A Result Set 3
slug: devguide_scanning_a_result_set_3
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_scanning_a_result_set_3.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: feee9f4a09389a2084f4cc3231fcb06f539a98f0
---

# Devguide Scanning A Result Set 3

Scanning a Result Set

     Scanning a Result Set

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning is the process of sequentially reading every record in a result, or every record in the filtered view of the result set if a filter is active. In ADO.NET, scanning is performed using an AdsDataReader or AdsExtendedReader, which you obtain from an AdsCommand object that contains either a SQL SELECT statement, a table name, or a stored procedure call.

   
TIP: If you are using ADS, and you must scan a large number of records, consider implementing the operation using a stored procedure as described in Chapter 7. Scanning from a stored procedure installed on the same machine on which the data resides requires no network resources.  
 

The following code demonstrates scanning using an AdsDataReader. This code is associated with the List Products button shown in Figure 18-3:

private void listProductsBtn\_Click(object sender,  
  System.EventArgs e) {  
  command.CommandText = "SELECT \* FROM PRODUCTS";  
  dataReader = command.ExecuteReader();  
  while (dataReader.Read()) {  
    productList.Items.Add(dataReader.GetString(0) + "  " +  
      dataReader.GetString(1));  
  }  
  dataReader.Close();  
}
