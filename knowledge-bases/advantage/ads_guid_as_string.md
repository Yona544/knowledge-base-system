ads\_guid\_to\_string




Advantage Database Server 12  

ads\_guid\_to\_string

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_guid\_to\_string |  |  | Feedback on: Advantage Database Server 12 - ads\_guid\_to\_string Ads\_guid\_as\_string Advantage PHP Extension > Extension Functions > ads\_guid\_to\_string / Dear Support Staff, |  |
| ads\_guid\_to\_string |  |  |  |  |

Retrieves GUID in bracelet format.

{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}

Syntax

int ads\_guid\_to\_string( string str\_guid )

Parameters

|  |  |
| --- | --- |
| str\_guid (I) | guid retrived from ads\_result command |

Remarks

ads\_guid\_to\_string returns the Bracelet format for the input string. Input is the 32 bit string retrived from the ads\_result function call. Returns NULL for any wrong input.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Preparing a statement with a parameter<br>\n";

$rStmt = ads\_prepare( $rConn, "SELECT \* FROM company" );

echo "Statement prepared<br>\n";

 

echo "Executing the statement.<br>\n";

$rResult = ads\_execute( $rStmt, $aParams );

echo "Execution was successful<br>\n";

 

echo "Retrieve the Company Name and its GUID Code<br>\n";

while ( ads\_fetch\_row( $rStmt ) )

{

$strCompanyName = ads\_result( $rStmt, "COMPANY" );

$strCompanyCode = ads\_result( $rStmt, "COMPANY\_GUID\_CODE" );

echo $strCompanyName . " has GUID code" . ads\_guid\_to\_string($strCompanyCode) . "<br>\n";

}

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

 

See Also

[ads\_execute](php_ads_execute.htm)

[ads\_connect](php_ads_connect.htm)

[ads\_result](php_ads_result.htm)