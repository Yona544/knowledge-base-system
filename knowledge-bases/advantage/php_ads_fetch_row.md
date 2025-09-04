ads\_fetch\_row




Advantage Database Server 12  

ads\_fetch\_row

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_fetch\_row  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_fetch\_row Advantage PHP Extension php\_Ads\_fetch\_row Advantage PHP Extension > Extension Functions > ads\_fetch\_row / Dear Support Staff, |  |
| ads\_fetch\_row  Advantage PHP Extension |  |  |  |  |

Retrieves a single row from a result set.

Syntax

bool ads\_fetch\_row( resource result\_id

[, int row\_number] )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |
| row\_number (I) | Optional row number of the result set to fetch. |

Remarks

ads\_fetch\_row returns True if a row was successfully fetched. In the event of an error or no rows fetched, False is returned. Use [ads\_result](php_ads_result.htm) to retrieve the value of an individual field after ads\_fetch\_row has retrieved the row from the result set.

If the optional row number is not specified, the next row in the result set will be returned. To read the values from a result set again, call ads\_fetch\_row with a value of 1. This moves the current position to the top of the result set. Subsequent calls to ads\_fetch\_row without a row\_number will fetch the next row in the result set.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Preparing a statement with a parameter<br>\n";

$rStmt = ads\_prepare( $rConn, "SELECT \* FROM customers WHERE company LIKE ?" );

echo "Statement prepared<br>\n";

 

echo "Executing the statement. Notice the array of parameters<br>\n";

$aParams = array( 1 => 'A%' );

$rResult = ads\_execute( $rStmt, $aParams );

echo "Execution was successful<br>\n";

 

echo "Retrieve the Company Name and Credit Limit<br>\n";

while ( ads\_fetch\_row( $rStmt ) )

{

$strCompanyName = ads\_result( $rStmt, "COMPANY" );

$strCreditLimit = ads\_result( $rStmt, "CREDIT\_LIMIT" );

echo $strCompanyName . " can spend up to $" . $strCreditLimit . "<br>\n";

}

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_execute](php_ads_execute.htm)

[ads\_exec](php_ads_exec.htm)

[ads\_do](php_ads_do.htm)

[ads\_fetch\_row](php_ads_fetch_row.htm)

[ads\_fetch\_array](php_ads_fetch_array.htm)

[ads\_result](php_ads_result.htm)