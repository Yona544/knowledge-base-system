ads\_close




Advantage Database Server 12  

ads\_close

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_close  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_close Advantage PHP Extension php\_Ads\_close Advantage PHP Extension > Extension Functions > ads\_close / Dear Support Staff, |  |
| ads\_close  Advantage PHP Extension |  |  |  |  |

Closes a connection to the Advantage Database Server.

Syntax

void ads\_close( int connection\_id )

Parameters

|  |  |
| --- | --- |
| connection\_id (I) | ID of a connection to the Advantage Database Server. |

Remarks

ads\_close is used to close a connection to the specified server. If ads\_close is called on a connection with a transaction active, the transaction will be rolled back and then the connection closed.

Example

<?php

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connect<br>\n";

ads\_close( $rConn );

echo "Closed<br>\n";

?>

See Also

[ads\_close\_all](php_ads_close_all.htm)

[ads\_connect](php_ads_connect.htm)