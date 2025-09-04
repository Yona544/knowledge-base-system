Editing Data




Advantage Database Server 12  

     Editing Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Editing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Editing Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Editing\_Data Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Editing Data / Dear Support Staff, |  |
| Editing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Since PHP uses ODBC, and ODBC uses SQL to edit data, you change data from a PHP script by executing a SQL UPDATE statement. This is demonstrated in the following PHP statements from the script named changeaddress.php. This script expects two values, a customer ID and a string containing a new address, to be passed in the HTTP GET query string. These values are used to execute a parameterized UPDATE query statement. Once the update has been executed, this script performs a SQL SELECT to read the newly updated address from the CUSTOMER table:

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn, "UPDATE customer ".  
  "SET Address = ? WHERE [Customer ID] = ?" );  
$aUpdateParams = array( 1 => $\_GET[ "newaddress" ],  
                        2 => $\_GET[ "custnumber" ] );  
$rResult = ads\_execute( $rStmt, $aUpdateParams );  
$iRowsAffected = ads\_num\_rows( $rStmt );  
if ( $iRowsAffected == 0 )   
   {  
   echo "Invalid customer ID!<br><br>\n";  
   }  
$rStmt = ads\_prepare( $rConn, "SELECT \* FROM customer ".  
  "WHERE [Customer ID] = ?" );  
$aSelectParams = array( 1 => $\_GET[ "custnumber" ] );  
$rResult = ads\_execute( $rStmt, $aSelectParams );  
if ( ads\_fetch\_row( $rStmt ) )  
   {  
   $strFirstName = ads\_result( $rStmt, "First Name" );  
   $strLastName = ads\_result( $rStmt, "Last Name" );  
   $strAddress = ads\_result( $rStmt, "Address" );  
   echo "Address successfully changed!<br><br>";  
   echo "The new address is: " . $strAddress . "<br>";  
   }  
ads\_close( $rConn );  
?>