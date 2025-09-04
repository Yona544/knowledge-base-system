ads\_close\_all




Advantage Database Server 12  

ads\_close\_all

Advantage PHP Extension

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ads\_close\_all  Advantage PHP Extension |  |  | Feedback on: Advantage Database Server 12 - ads\_close\_all Advantage PHP Extension php\_Ads\_close\_all Advantage PHP Extension > Extension Functions > ads\_close\_all / Dear Support Staff, |  |
| ads\_close\_all  Advantage PHP Extension |  |  |  |  |

Closes all connections to the Advantage Database Server.

Syntax

void ads\_close\_all( void )

Parameters

None.

Remarks

ads\_close\_all is used to close all connections to the server. All active transactions will be rolled back before all connections are closed

Example

<?php

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connect<br>\n";

ads\_close\_all();

echo "Closed All Transactions<br>\n";

?>

See Also

[ads\_close](php_ads_close.htm)

[ads\_connect](php_ads_connect.htm)