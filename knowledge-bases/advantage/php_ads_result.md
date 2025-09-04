ads\_result




Advantage Database Server 12  

ads\_result

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_result  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_result Advantage PHP Extension php\_Ads\_result Advantage PHP Extension > Extension Functions > ads\_result / Dear Support Staff, |  |
| ads\_result  Advantage PHP Extension |  |  |  |  |

Retrieves the value of a field as a string.

Syntax

string ads\_result( resource result\_id,

string field )

OR

string ads\_result( resource result\_id,

int field )

Parameters

|  |  |
| --- | --- |
| result\_id (I) | ID of a result set. |
| field (I) | Name of the field in the result set. |

or

|  |  |
| --- | --- |
| field (I) | Number (position) of the field in the result set. |

Remarks

ads\_result retrieves the value of the specified field from the current row. The field can be identified in the result by either its name or position. The index of the first field of a result set is 1. In the event of an error, False is returned.

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

[ads\_field\_len](php_ads_field_len.htm)