ads\_errormsg




Advantage Database Server 12  

ads\_errormsg

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_errormsg  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_errormsg Advantage PHP Extension php\_Ads\_errormsg Advantage PHP Extension > Extension Functions > ads\_errormsg / Dear Support Staff, |  |
| ads\_errormsg  Advantage PHP Extension |  |  |  |  |

Returns the last Advantage error message.

Syntax

string ads\_errormsg( [int connection\_id] )

Parameters

|  |  |
| --- | --- |
| connection\_id (I) | Optional ID of a connection to the Advantage Database Server. |

Remarks

ads\_errormsg returns a string containing the last error message if an error occurred or an empty string if no error occurred in last Advantage API that was performed. Unless a connection ID is specified, the last error message of any connection is returned.

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

[ads\_error](php_ads_error.htm)