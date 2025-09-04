ads\_prepare




Advantage Database Server 12  

ads\_prepare

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_prepare  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_prepare Advantage PHP Extension php\_Ads\_prepare Advantage PHP Extension > Extension Functions > ads\_prepare / Dear Support Staff, |  |
| ads\_prepare  Advantage PHP Extension |  |  |  |  |

Prepares an SQL statement for execution.

Syntax

resource ads\_prepare( resource connection\_id,

string query )

Parameters

|  |  |
| --- | --- |
| connection\_id (I) | ID of a connection to the Advantage Database Server. |
| query (I) | The SQL statement to be prepared. |

Remarks

Use ads\_prepare when executing SQL statements containing parameters. To execute the SQL statement, call ads\_execute with the result set identifier returned by ads\_prepare. If the statement could not be prepared, False is returned.

Named and unnamed parameters are supported. Named parameters are represented with a string preceded by a colon. The "string" portion may contain the characters 0..9, A..Z, a..z, or the underscore character (\_). Unnamed parameters are represented by a question mark (?).

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

[ads\_connect](php_ads_connect.htm)

[ads\_execute](php_ads_execute.htm)