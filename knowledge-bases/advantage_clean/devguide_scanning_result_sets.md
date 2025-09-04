---
title: Devguide Scanning Result Sets
slug: devguide_scanning_result_sets
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_scanning_result_sets.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5b7a2fe2e9eddb3e3a0f3fe0db9702193587310d
---

# Devguide Scanning Result Sets

Scanning Result Sets

     Scanning Result Sets

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Scanning Result Sets  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Scanning involves the sequential navigation of the records in a result set. Scanning is often done when you want to manually insert HTML based on your result set into the stream that is inserted in place of the PHP commands.

The following PHP commands are located in the showproducts.php script. These commands produce an HTML form that includes one radio button for each product found in the PRODUCT table. Because of the action attribute of the HTML form, the product code of the selected product name will be appended to the query string part of the HTTP GET command that will be submitted to the showproducts.php script.

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn, "SELECT [Product Name], ".  
  "[Product Code] FROM Products" );  
$rResult = ads\_execute( $rStmt );  
while ( ads\_fetch\_row( $rStmt ) )  
   {  
   $strProductName = ads\_result( $rStmt, "Product Name" );  
   $strProductCode = ads\_result( $rStmt, "Product Code" );  
   echo "<INPUT Type = \"radio\" Name = \"rb\" Value = \"" .   
      trim( $strProductCode ) .  "\" > " .   
      $strProductName . "<br>\n";     
   }  
ads\_close( $rConn );  
?>

When this PHP file is processed, it produces the Web page shown in Figure 19-6.

Figure 19-6: The output from showproducts.php
