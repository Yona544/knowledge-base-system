---
title: Devguide Calling A Stored Procedure 4
slug: devguide_calling_a_stored_procedure_4
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_calling_a_stored_procedure_4.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 21a1202b1cd5ef2fe3686dd23f4cd21932d00679
---

# Devguide Calling A Stored Procedure 4

Calling a Stored Procedure

     Calling a Stored Procedure

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

This final example demonstrates the execution of a stored procedure using PHP. Actually, as you can see from these statements, executing a stored procedure is no different than any other type of parameterized query. After a call to ads\_prepare, an array is created to hold the parameter values, after which it is passed as an argument to ads\_execute. Once again, the ads\_result\_all function is used to render an HTML table from the query result set. The following PHP commands are located in the storedproc.php script:

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn,   
  "EXECUTE PROCEDURE SQLGet10Percent ( ? )" );  
$aParams = array( 1 => $\_GET[ "custnumber" ] );  
$rResult = ads\_execute( $rStmt, $aParams );  
if ( $rResult == FALSE )   
   {  
   echo ads\_errormsg( $rConn ) . "<br>\n";  
   }  
else  
   {  
   ads\_result\_all( $rStmt );  
   }  
ads\_close( $rConn );  
?>
