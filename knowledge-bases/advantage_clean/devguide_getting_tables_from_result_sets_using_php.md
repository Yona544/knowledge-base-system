---
title: Devguide Getting Tables From Result Sets Using Php
slug: devguide_getting_tables_from_result_sets_using_php
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_getting_tables_from_result_sets_using_php.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: a3d77084ecc82e9d45eb8008f4fc9f863f075002
---

# Devguide Getting Tables From Result Sets Using Php

Getting Tables from Result Sets Using PHP

     Getting Tables from Result Sets Using PHP

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Getting Tables from Result Sets Using PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

After executing a query, you can easily display the entire result set by calling ads\_result\_all. This function takes the handle returned from a call to ads\_execute in its first parameter, and an optional string containing HTML table element attributes in the second, and returns a string containing a complete HTML <TABLE> definition that includes one row for each record in the result set. This function is only used when you execute a query that returns one or more records.

The use of ads\_result\_all is demonstrated in the showtables.php script. The PHP statements from this file are shown in the following listing:

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn, "SELECT Name FROM ".   
  "system.tables" );  
$rResult = ads\_execute( $rStmt );  
ads\_result\_all( $rStmt );  
ads\_close( $rConn );  
?>

When this script is rendered, it produces the Web page shown in Figure 19-5.

Figure 19-5: The Web page returned by showtables.php

As mentioned earlier, the ads\_result\_all function can accept a second, optional parameter. You use this parameter to pass a string that will be incorporated into the <TABLE> element. Normally you use this parameter to pass one or more table attributes that will be used to control the table's format and behavior, such as bgcolor, border, onclick, style, id, and width, to name a few.
