ads\_commit




Advantage Database Server 12  

ads\_commit

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_commit  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_commit Advantage PHP Extension php\_Ads\_commit Advantage PHP Extension > Extension Functions > ads\_commit / Dear Support Staff, |  |
| ads\_commit  Advantage PHP Extension |  |  |  |  |

Commits the active transaction on the specified connection.

Syntax

boolean ads\_commit( int connection\_id )

Parameters

|  |  |
| --- | --- |
| connection\_id (I) | ID of a connection to the Advantage Database Server. |

Remarks

Calling ads\_commit when the Advantage PHP Extension is not in auto-commit mode commits the active transaction on the given connection and begins a new transaction. If the Advantage PHP Extension is in auto-commit mode, calling ads\_commit has no effect and returns True. If the active transaction is successfully committed, True is returned. False is returned in the event of an error.

Example

<?

echo "Connecting to Server<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connected<br>\n";

 

echo "Turning off auto-commit. Starts a transactions.<br>\n";

ads\_autocommit( $rConn, False );

 

echo "Updating the customers credit limit.<br>\n";

$rResult = ads\_do( $rConn, "UPDATE customers SET credit\_limit = ( credit\_limit \* 2 )" );

 

echo "Committing the changes.<br>\n";

ads\_commit( $rConn );

 

echo "Closing the connection<br>\n";

ads\_close( $rConn );

echo "Disconnected<br>\n";

?>

See Also

[ads\_autocommit](php_ads_autocommit.htm)

[ads\_rollback](php_ads_rollback.htm)

[ads\_connect](php_ads_connect.htm)