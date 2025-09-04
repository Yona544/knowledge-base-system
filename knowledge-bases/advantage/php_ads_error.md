ads\_error




Advantage Database Server 12  

ads\_error

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_error  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_error Advantage PHP Extension php\_Ads\_error Advantage PHP Extension > Extension Functions > ads\_error / Dear Support Staff, |  |
| ads\_error  Advantage PHP Extension |  |  |  |  |

Returns the last Advantage error code.

Syntax

string ads\_error( [int connection\_id] )

Parameters

|  |  |
| --- | --- |
| connection\_id (I) | Optional ID of a connection to the Advantage Database Server. |

Remarks

ads\_error returns an error code if an error occurred or an empty string if no error occurred in last Advantage API that was performed. If a connection ID is not specified, the last error of any connection is returned.

Example

<?

echo "Connecting to a Server that does not exist.<br>\n";

echo "This connect should FAIL!<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\NOServer\\NonExistantShare\\;ServerTypes=2", "", "" );

 

if ( $rConn == False )

{

$strErrCode = ads\_error( );

$strErrString = ads\_errormsg( );

echo "Connection failed: " . $strErrCode . " " . $strErrString . "<br>\n";

}

else

{

echo "Connection successful!<br>\n";

ads\_close( $rConn );

echo "Connection closed<br>\n";

}

?>

See Also

[ads\_connect](php_ads_connect.htm)

[ads\_errormsg](php_ads_errormsg.htm)