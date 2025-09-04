---
title: Devguide Scanning A Result Set 1
slug: devguide_scanning_a_result_set_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_scanning_a_result_set_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: d4f05267400c23aeb5459b6765839090e51c1aae
---

# Devguide Scanning A Result Set 1

Scanning a Result Set

     Scanning a Result Set

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Scanning a Result Set  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning is the process of sequentially reading every record in a result set. Although scanning is a common task, it is important to note that it necessarily requires the client application to retrieve all of the records in the result set. This is not a problem when few records are involved, but if a large number of records are being scanned, network resources may be taxed.

   
TIP: If you must scan a large number of records, implement the operation using a stored procedure. When ADS and the data are located on the same server, scanning from a stored procedure installed on ADS requires no network resources.  
 

The following code demonstrates scanning. It is associated with the actionPerformed event handler of the List Products button (shown in Figure 16-1), and it navigates the entire PRODUCTS table, assigning data from each record to the productList JListBox:

void listProductsBtn\_actionPerformed(ActionEvent e) {  
  DefaultListModel listModel =   
    new javax.swing.DefaultListModel();  
  try {  
    ResultSet rs = stmt.executeQuery(  
      "SELECT \* FROM PRODUCTS");  
    rs.first();  
    do {  
      listModel.addElement(rs.getString(1) + "     " +  
        rs.getString(2));  
    } while (rs.next());  
    productList.setModel(listModel);  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
  }  
}

Note that the do-while loop in the preceding event handler could also have been written as follows using a while-do loop:

while (rs.next()) do {  
  listModel.addElement(rs.getString(1) + "     " +  
    rs.getString(2));  
}

While the behavior of these two control structures is equivalent, there is a potential drawback to the second version, the while-do loop. Specifically, if the ResultSet has been navigated in any way prior to the while-do loop, the first record will be skipped. The do-while statement preceded by a call to the first method, by comparison, always processes every record in the ResultSet, whether or not the ResultSet has been navigated previously.
