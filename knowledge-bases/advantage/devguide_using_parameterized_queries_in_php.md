Using Parameterized Queries in PHP




Advantage Database Server 12  

     Using Parameterized Queries in PHP

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Parameterized Queries in PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Using Parameterized Queries in PHP Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Using\_Parameterized\_Queries\_in\_PHP Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 19 - ODBC, PHP, DBI/Perl > Using Parameterized Queries in PHP / Dear Support Staff, |  |
| Using Parameterized Queries in PHP  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Once you have established a connection, you invoke the ads\_prepare function to prepare a parameterized query. This function takes two parameters. The first parameter is the connection resource obtained by calling ads\_connect, and the second is a string containing the parameterized query.

Once you have prepared your parameterized query, you bind the parameters and execute the query by calling ads\_execute. This function takes two parameters: the handle of the prepared statement returned from the ads\_prepare function, and an array of values to bind to the parameters, based on their ordinal position within the query.

The execution of a parameterized query is demonstrated in the following listing, which contains the PHP statements from the getcustomer.php file:

<?  
$rConn = ads\_connect( "DataDirectory=\\\\server\\share\\".  
  "adsbook\\DemoDictionary.add;ServerTypes=2;",   
  "adsuser", "password" );  
$rStmt = ads\_prepare( $rConn, "SELECT \* FROM customer ".  
  "WHERE [Customer ID] = ?" );  
$aParams = array( 1 => $\_GET[ "custnumber" ] );  
$rResult = ads\_execute( $rStmt, $aParams );  
if ( ads\_fetch\_row( $rStmt ) )  
   {  
   $strFirstName = ads\_result( $rStmt, "First Name" );  
   $strLastName = ads\_result( $rStmt, "Last Name" );  
   $strAddress = ads\_result( $rStmt, "Address" );  
   echo "Name: " . $strFirstName . " " .  
     $strLastName . "<br>";  
   echo "Address: " . $strAddress . "<br>";  
   }  
else  
   {  
   echo "Invalid Customer Number! <br>";  
   }  
   
ads\_close( $rConn );  
?>

As you can see, once the connection is established, and the parameterized query is prepared, a single element array is constructed from the custnumber value passed in the query string of this HTTP GET request (if you used a POST action, you would have read this value using the $\_POST PHP function). The query is then executed.

Following the execution of the query, ads\_fetch\_row is called to retrieve one record from the result set. Individual fields of this record are read using the ads\_result function.

If you enter customer number 12037 in the Customer Number field of the Get a customer record HTML form of index.htm and click Submit, your browser will display the page shown in Figure 19-4.

Figure 19-4: Result from the parameterized query example